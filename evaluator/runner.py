import os
import json
import glob
from datetime import datetime
from agents.quality_evaluator_agent import QualityEvaluatorAgent

TESTS_DIR = 'generated_tests'
RESULTS_DIR = 'evaluation_results'

os.makedirs(RESULTS_DIR, exist_ok=True)

def run_all_tests():
    json_files = sorted(glob.glob(os.path.join(TESTS_DIR, "tests_*.json")), reverse=True)
    if not json_files:
        raise FileNotFoundError("Nenhum arquivo JSON encontrado em generated_tests/")

    with open(json_files[0], 'r', encoding='utf-8') as f:
        test_data = json.load(f)

    print("[RUNNER] Iniciando avaliação com QualityEvaluatorAgent...")
    agent = QualityEvaluatorAgent()
    results = agent.evaluate(test_data, prod_code_path="prompts/code.py")
    print("[RUNNER] Avaliação finalizada com sucesso.")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(RESULTS_DIR, f"evaluation_{timestamp}.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    return results, output_file

if __name__ == "__main__":
    res, file = run_all_tests()
    print(f"Resultados salvos em {file}")
