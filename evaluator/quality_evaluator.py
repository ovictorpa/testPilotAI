import os
import re
import ast
import subprocess
from xml.etree import ElementTree as ET

PROD_CODE_FILE = 'prompts/code.py'
TEMP_DIR = 'test_outputs'
os.makedirs(TEMP_DIR, exist_ok=True)

class QualityEvaluator:
    def __init__(self, weights=None):
        self.weights = weights or {
            "pass_bonus": 1.5,
            "coverage": {
                "0": -1.0,
                "1-25": 0.2,
                "26-50": 0.5,
                "51-75": 0.8,
                "76-100": 1.0,
            },
            "assert_diversity": {
                "4+": 0.3,
                "3": 0.2,
                "2": 0.1,
            },
            "edge_case": 0.3,
            "functions_tested_ratio": 0.7,
            "test_smell_penalty": 0.3,
            "fatal_smell_penalty": 1.0,
        }

    def detect_test_smells(self, test_code):
        smells = {}
        try:
            tree = ast.parse(test_code)
        except SyntaxError:
            smells['syntax_error'] = 1
            return smells

        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute) and node.func.attr.startswith('assert'):
                    if len(node.args) == 1:
                        smells['assertion_roulette'] = smells.get('assertion_roulette', 0) + 1
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                if node.value not in (0, 1):
                    smells['magic_number'] = smells.get('magic_number', 0) + 1
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == 'sleep':
                    smells['sleepy_test'] = smells.get('sleepy_test', 0) + 1
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id == 'print':
                    smells['print_statement'] = smells.get('print_statement', 0) + 1
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute) and node.func.attr.startswith('assert'):
                    for arg in node.args:
                        if isinstance(arg, ast.Constant) and arg.value in [True, False]:
                            smells['redundant_assertion'] = smells.get('redundant_assertion', 0) + 1
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
                if not node.body or all(isinstance(stmt, ast.Pass) for stmt in node.body):
                    smells['empty_test'] = smells.get('empty_test', 0) + 1
            if isinstance(node, ast.FunctionDef):
                for decorator in node.decorator_list:
                    if isinstance(decorator, ast.Attribute) and 'skip' in decorator.attr.lower():
                        smells['ignored_test'] = smells.get('ignored_test', 0) + 1
        return smells

    def extract_code_blocks(self, text):
        return re.findall(r"```(?:python)?\s*(.*?)```", text, re.DOTALL)

    def run_test_code_with_coverage(self, code_str, filename):
        filepath = os.path.join(TEMP_DIR, filename)
        forced_import = "from prompts.code import *\n\n"
        full_code = forced_import + code_str

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_code)

        env = os.environ.copy()
        env['PYTHONPATH'] = os.path.abspath('.')
        subprocess.run(["coverage", "erase"], env=env)

        try:
            result = subprocess.run(
                ['coverage', 'run', '--source=prompts', filepath],
                capture_output=True,
                text=True,
                timeout=10,
                cwd='.',
                env=env
            )
            if result.returncode != 0:
                print(f"[ERROR] Código falhou: {filename}")
                print("[STDOUT]", result.stdout)
                print("[STDERR]", result.stderr)
                return False, result.stdout, result.stderr, "-"
        except subprocess.TimeoutExpired:
            print(f"[TIMEOUT] Teste travou e foi abortado: {filename}")
            return False, "", "Timeout", "-"
        except Exception as e:
            print(f"[EXCEPTION] Erro ao executar teste {filename}: {e}")
            return False, "", str(e), "-"

        subprocess.run(['coverage', 'xml'], capture_output=True, text=True, cwd='.', env=env)

        coverage_percent = "-"
        if os.path.exists("coverage.xml"):
            try:
                tree = ET.parse("coverage.xml")
                root = tree.getroot()
                line_rate = root.attrib.get('line-rate')
                if line_rate:
                    coverage_percent = f"{round(float(line_rate) * 100)}%"
            except Exception as e:
                print(f"[ERROR] Falha ao processar coverage.xml: {e}")

        return True, result.stdout, result.stderr, coverage_percent

    def extract_assert_types(self, code_str):
        return re.findall(r'self\\.(assert\\w+)', code_str)

    def detect_edge_cases(self, code_str):
        edge_indicators = ['0', '-1', '""', "''", '[]', '{}', 'None']
        return any(e in code_str for e in edge_indicators)

    def count_functions_tested(self, code_str, prod_functions):
        return sum(1 for func in prod_functions if func in code_str)

    def evaluate(self, code, model, prompt_type, prod_functions):
        filename = f"{model}_{prompt_type}.py"
        passed, stdout, stderr, coverage_percent = self.run_test_code_with_coverage(code, filename)
        assert_types = self.extract_assert_types(code)
        edge_case_found = self.detect_edge_cases(code)
        tested_funcs = self.count_functions_tested(code, prod_functions)
        smells_found = self.detect_test_smells(code)

        score = 0.0
        if passed:
            score += self.weights["pass_bonus"]

        try:
            coverage_value = float(coverage_percent.strip('%'))
        except ValueError:
            coverage_value = -1

        for key, value in self.weights["coverage"].items():
            if '-' in key:
                start, end = map(int, key.split('-'))
                if start <= coverage_value <= end:
                    score += value
                    break
            elif key == str(int(coverage_value)):
                score += value
                break

        unique_asserts = len(set(assert_types))
        for key, value in self.weights["assert_diversity"].items():
            if '+' in key:
                if unique_asserts >= int(key.strip('+')):
                    score += value
                    break
            elif unique_asserts == int(key):
                score += value
                break

        if edge_case_found:
            score += self.weights["edge_case"]

        if prod_functions:
            score += self.weights["functions_tested_ratio"] * (tested_funcs / len(prod_functions))

        if smells_found and "syntax_error" not in smells_found:
            score -= self.weights["test_smell_penalty"] * len(smells_found)
        elif "syntax_error" in smells_found:
            score -= self.weights["fatal_smell_penalty"]

        return {
            "status": "passed" if passed else "failed",
            "coverage": coverage_percent,
            "assert_types": list(set(assert_types)),
            "edge_case_found": edge_case_found,
            "functions_tested": tested_funcs,
            "total_functions": len(prod_functions),
            "score": round(score, 2),
            "stdout": stdout,
            "stderr": stderr,
            "test_smells": smells_found
        }
