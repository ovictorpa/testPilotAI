import os
import json
import subprocess
import re
import glob
import tempfile
import ast
from datetime import datetime


TESTS_DIR = 'generated_tests'
TEMP_DIR = 'test_outputs'
RESULTS_DIR = 'evaluation_results'
PROD_CODE_FILE = 'prompts/code.py'

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)


import ast

import ast

def detect_test_smells(test_code: str) -> dict:
    smells = {}

    try:
        tree = ast.parse(test_code)
    except SyntaxError:
        smells['syntax_error'] = 1
        return smells

    for node in ast.walk(tree):
        # Assertion Roulette
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr.startswith('assert'):
                if len(node.args) == 1:
                    smells['assertion_roulette'] = smells.get('assertion_roulette', 0) + 1

        # Magic Number
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            if node.value not in (0, 1):
                smells['magic_number'] = smells.get('magic_number', 0) + 1

        # Sleepy Test
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == 'sleep':
                smells['sleepy_test'] = smells.get('sleepy_test', 0) + 1

        # Print Statement
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == 'print':
                smells['print_statement'] = smells.get('print_statement', 0) + 1

        # Redundant Assertion
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr.startswith('assert'):
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and arg.value in [True, False]:
                        smells['redundant_assertion'] = smells.get('redundant_assertion', 0) + 1

        # Empty Test
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
            if not node.body or all(isinstance(stmt, ast.Pass) for stmt in node.body):
                smells['empty_test'] = smells.get('empty_test', 0) + 1

        # Ignored Test
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Attribute) and 'skip' in decorator.attr.lower():
                    smells['ignored_test'] = smells.get('ignored_test', 0) + 1

    return smells


def extract_code_blocks(text):
    matches = re.findall(r"```(?:python)?\s*(.*?)```", text, re.DOTALL)
    return matches

def run_test_code_with_coverage(code_str, filename):
    filepath = os.path.join(TEMP_DIR, filename)

    try:
        # Força o import do código de produção
        forced_import = "from prompts.code import *\n\n"
        full_code = forced_import + code_str

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_code)

        env = os.environ.copy()
        env['PYTHONPATH'] = os.path.abspath('.')

        subprocess.run(["coverage", "erase"], env=env)

        result = subprocess.run(
            ['coverage', 'run', '--source=prompts', filepath],
            capture_output=True,
            text=True,
            timeout=10,
            cwd='.',
            env=env
        )

        if result.returncode != 0:
            return False, result.stdout, result.stderr, "-"

        subprocess.run(['coverage', 'xml'], capture_output=True, text=True, cwd='.', env=env)

        coverage_percent = "-"
        if os.path.exists("coverage.xml"):
            import xml.etree.ElementTree as ET
            tree = ET.parse("coverage.xml")
            root = tree.getroot()
            line_rate = root.attrib.get('line-rate')
            if line_rate:
                coverage_percent = f"{round(float(line_rate) * 100)}%"

        return True, result.stdout, result.stderr, coverage_percent

    except subprocess.TimeoutExpired:
        return False, "", "Timeout", "-"
    except Exception as e:
        return False, "", str(e), "-"

def get_prod_functions():
    try:
        with open(PROD_CODE_FILE, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    except:
        return []

def extract_assert_types(code_str):
    return re.findall(r'self\.(assert\w+)', code_str)

def detect_edge_cases(code_str):
    edge_indicators = ['0', '-1', '""', "''", '[]', '{}', 'None']
    return any(e in code_str for e in edge_indicators)

def count_functions_tested(code_str, prod_functions):
    return sum(1 for func in prod_functions if func in code_str)

def run_all_tests():
    json_files = sorted(glob.glob(os.path.join(TESTS_DIR, "tests_*.json")), reverse=True)
    if not json_files:
        raise FileNotFoundError("Nenhum arquivo JSON encontrado em generated_tests/")

    with open(json_files[0], 'r', encoding='utf-8') as f:
        test_data = json.load(f)

    prod_functions = get_prod_functions()
    results = {}

    for model, prompts in test_data.items():
        results[model] = {}
        for prompt_type, full_text in prompts.items():
            code_blocks = extract_code_blocks(full_text)
            if not code_blocks:
                results[model][prompt_type] = {
                    "status": "no_code_found",
                    "score": 0.0
                }
                continue

            code = code_blocks[0]
            filename = f"{model}_{prompt_type}.py"

            passed, stdout, stderr, coverage_percent = run_test_code_with_coverage(code, filename)
            assert_types = extract_assert_types(code)
            edge_case_found = detect_edge_cases(code)
            tested_funcs = count_functions_tested(code, prod_functions)

            score = 0.0
            if passed:
                score += 2.0
            try:
                coverage_value = float(coverage_percent.strip('%'))
            except ValueError:
                coverage_value = -1

            if coverage_value == 0:
                score -= 1.0
            elif 0 < coverage_value <= 25:
                score += 0.25
            elif 25 < coverage_value <= 50:
                score += 0.50
            elif 50 < coverage_value <= 75:
                score += 0.75
            elif coverage_value > 75:
                score += 1.0
            if len(set(assert_types)) >= 4:
                score += 0.30
            elif len(set(assert_types)) == 3:
                score += 0.15
            elif len(set(assert_types)) == 2:
                score += 0.07
            if edge_case_found:
                score += 0.25
            if prod_functions:
                score += 0.5 * (tested_funcs / len(prod_functions))

            smells_found = detect_test_smells(code)

            if smells_found and "error" not in smells_found:
                score -= 0.2 * len(smells_found)
            elif "error" in smells_found:
                score -= 1.0

            results[model][prompt_type] = {
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
            #if any(count > 0 for count in smells_found.values()):
                #result["test_smells"] = smells_found

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(RESULTS_DIR, f"evaluation_{timestamp}.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    return results, output_file

if __name__ == "__main__":
    res, file = run_all_tests()
    print(f"Resultados salvos em {file}")
