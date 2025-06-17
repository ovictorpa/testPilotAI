import os
import json
from evaluator.quality_evaluator import QualityEvaluator

class QualityEvaluatorAgent:
    def __init__(self, weights: dict = None):
        self.evaluator = QualityEvaluator(weights)

    def evaluate(self, test_data: dict, prod_code_path: str = "prompts/code.py"):
        results = {}

        for model, prompts in test_data.items():
            results[model] = {}
            for prompt_type, full_text in prompts.items():
                print(f"[AGENT] Avaliando: {model} - {prompt_type}...")
                try:
                    result = self.evaluator.evaluate(full_text, model, prompt_type, prod_code_path)
                    print(f"[AGENT] Avaliação concluída para: {model} - {prompt_type}")
                except Exception as e:
                    print(f"[AGENT] Erro ao avaliar {model} - {prompt_type}: {e}")
                    result = {"status": "error", "message": str(e)}
                results[model][prompt_type] = result

        return results
