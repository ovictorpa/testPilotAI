import os
import json
import random
import re
from typing import List, Dict


class PromptOptimizerAgent:
    def __init__(self, evaluation_file: str, original_prompts_file: str, top_k: int = 3, explore_ratio: float = 0.2):
        self.evaluation_file = evaluation_file
        self.original_prompts_file = original_prompts_file
        self.top_k = top_k
        self.explore_ratio = explore_ratio

        self.evaluations = self._load_json(self.evaluation_file)
        self.original_prompts = self._load_json(self.original_prompts_file)

    def _load_json(self, path: str) -> dict:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Arquivo não encontrado: {path}")
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _mutate_prompt(self, prompt: str) -> str:
        mutations = [
            lambda p: p.replace("Write tests", "Create test cases"),
            lambda p: p + "\nInclude edge case scenarios.",
            lambda p: re.sub(r'unit test[s]?', 'robust test cases', p, flags=re.I),
            lambda p: p.replace("Ensure", "Make sure to"),
            lambda p: p + "\nPrioritize coverage and correctness.",

            # 🆕 Adicionadas:
            lambda p: p + "\nFollow best practices for naming and structure.",
            lambda p: p.replace("test cases", "test functions"),
            lambda p: re.sub(r'\btest\b', 'validation', p, flags=re.I),
            lambda p: p + "\nAdd comments explaining the purpose of each test.",
            lambda p: p + "\nInclude negative tests and boundary conditions.",
            lambda p: p.replace("Create", "Develop"),
            lambda p: p + "\nUse clear and descriptive assertion messages.",
            lambda p: p + "\nFocus on simplicity and readability of the tests.",
            lambda p: p + "\nSimulate realistic data where applicable.",
            lambda p: p + "\nExplain the reasoning behind test inputs used.",
        ]
        mutation = random.choice(mutations)
        return mutation(prompt)

    def optimize(self) -> Dict[str, Dict[str, str]]:
        new_prompts = {}
        all_scores = []

        for model in self.evaluations:
            for prompt_type, metrics in self.evaluations[model].items():
                score = metrics.get("score", 0.0)
                try:
                    original_prompt = self.original_prompts[model][prompt_type]
                except KeyError:
                    print(f"⚠️ Prompt ausente para modelo '{model}', tipo '{prompt_type}'. Pulando.")
                    continue
                all_scores.append((model, prompt_type, score, original_prompt))

        if not all_scores:
            print("❌ Nenhum prompt original válido encontrado. Abortando otimização.")
            return {}

        all_scores.sort(key=lambda x: x[2], reverse=True)
        num_exploit = int((1 - self.explore_ratio) * self.top_k)
        exploit_prompts = all_scores[:num_exploit]

        for model, prompt_type, _, original_prompt in exploit_prompts:
            if model not in new_prompts:
                new_prompts[model] = {}
            new_prompts[model][prompt_type] = self._mutate_prompt(original_prompt)

        for _ in range(self.top_k - num_exploit):
            model, prompt_type, _, original_prompt = random.choice(all_scores)
            if model not in new_prompts:
                new_prompts[model] = {}
            new_prompts[model][f"{prompt_type}_explore"] = self._mutate_prompt(original_prompt)

        # Debug: salvar resultado dos prompts otimizados
        debug_path = "generated_prompts/optimized_prompts_debug.json"
        os.makedirs(os.path.dirname(debug_path), exist_ok=True)
        with open(debug_path, "w", encoding="utf-8") as f:
            json.dump(new_prompts, f, indent=2, ensure_ascii=False)
        print(f"✅ Prompts otimizados salvos em {debug_path}")

        return {"default": new_prompts}