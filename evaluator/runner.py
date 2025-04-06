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

def extract_code_blocks(text):
    matches = re.findall(r"```(?:python)?\s*(.*?)```", text, re.DOTALL)
    return matches

def run_test_code_with_coverage(code_str, filename):
    filepath = os.path.join(TEMP_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code_str)

    try:
        result = subprocess.run(
            ['coverage', 'run', '--source=.', filepath],
            capture_output=True,
            text=True,
            timeout=10
        )
        subprocess.run(['coverage', 'report'], cwd=TEMP_DIR, capture_output=True)
        coverage_output = subprocess.run(
            ['coverage', 'report', '-m'],
            cwd=TEMP_DIR,
            capture_output=True,
            text=True
        )
        passed = result.returncode == 0
        return passed, result.stdout, result.stderr, coverage_output.stdout
    except subprocess.TimeoutExpired:
        return False, "", "Timeout", ""
    except Exception as e:
        return False, "", str(e), ""

def run_flake8_linter(code_str):
    with tempfile.NamedTemporaryFile(suffix='.py', delete=False, mode='w', encoding='utf-8') as tmp:
        tmp.write(code_str)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ['flake8', tmp_path],
            capture_output=True,
            text=True
        )
        lint_passed = result.returncode == 0
        return lint_passed, result.stdout.strip()
    finally:
        os.unlink(tmp_path)

def get_prod_functions():
    try:
        with open(PROD_CODE_FILE, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    except:
        return []

def analyze_test_smells(code_str):
    smells = []
    if 'assert' not in code_str:
        smells.append('no_assert')
    if re.search(r'def test_?(1|func)?\s*\(', code_str):
        smells.append('bad_name')
    if re.search(r'assert\s+(True|1\s*==\s*1)', code_str):
        smells.append('always_true')
    return smells

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

            passed, stdout, stderr, coverage = run_test_code_with_coverage(code, filename)
            lint_passed, lint_output = run_flake8_linter(code)
            smells = analyze_test_smells(code)
            assert_types = extract_assert_types(code)
            edge_case_found = detect_edge_cases(code)
            tested_funcs = count_functions_tested(code, prod_functions)

            score = 0.0
            if passed:
                score += 0.5
            if lint_passed:
                score += 0.25
            if "100%" in coverage:
                score += 0.25
            if len(set(assert_types)) >= 3:
                score += 0.25
            elif len(set(assert_types)) == 2:
                score += 0.15
            if edge_case_found:
                score += 0.25
            if 'no_assert' in smells:
                score -= 0.3
            if 'bad_name' in smells:
                score -= 0.1
            if 'always_true' in smells:
                score -= 0.1
            if prod_functions:
                score += 0.1 * (tested_funcs / len(prod_functions))

            results[model][prompt_type] = {
                "status": "passed" if passed else "failed",
                "coverage": coverage.strip(),
                "lint_passed": lint_passed,
                "lint_output": lint_output,
                "assert_types": list(set(assert_types)),
                "edge_case_found": edge_case_found,
                "test_smells": smells,
                "functions_tested": tested_funcs,
                "total_functions": len(prod_functions),
                "score": round(score, 2),
                "stdout": stdout,
                "stderr": stderr
            }

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(RESULTS_DIR, f"evaluation_{timestamp}.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    return results, output_file

if __name__ == "__main__":
    res, file = run_all_tests()
    print(f"Resultados salvos em {file}")