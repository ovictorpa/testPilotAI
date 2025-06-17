# agents/prompt_generator_agent.py

import random

class PromptGeneratorAgent:
    def __init__(self, base_code: str, num_variations: int = 3):
        self.base_code = base_code
        self.num_variations = num_variations
        self.strategies = ["zero-shot", "few-shot", "cot"]

    def generate_prompts(self):
        selected = random.sample(self.strategies, min(self.num_variations, len(self.strategies)))
        prompts = []

        for strategy in selected:
            prompt = self.apply_strategy(strategy)
            prompts.append({
                "strategy": strategy,
                "prompt": prompt
            })

        return prompts

    def apply_strategy(self, strategy: str) -> str:
        if strategy == "zero-shot":
            return f"Write unit tests in Python for the following function \n avoid returning imports like 'from your_module import you_function' let me do it manually:\n\n{self.base_code}"

        elif strategy == "few-shot":
            example = (
                "Example of basic unit test:\n"
                "def add(a, b): return a + b\n\n"
                "Test:\n"
                "import unittest\n"
                "class TestAdd(unittest.TestCase):\n"
                "    def test_add(self):\n"
                "        self.assertEqual(add(1, 2), 3)\n\n"
            )
            return (
                f"Write unit tests in Python for the following function. Avoid returning imports like 'from your_module import you_function' Here are some examples:\n\n"
                f"{example}"
                f"Now for the function:\n{self.base_code}"
            )

        elif strategy == "cot":
            return (
                "Write unit tests in Python for the following function. "
                "First, think step-by-step about the possible edge cases, scenarios, assertions and logic involved. avoid returning imports like 'from your_module import you_function'"
                f"Then write complete tests using unittest.\n\nFunction:\n{self.base_code}"
            )

        else:
            raise ValueError(f"Unknown strategy: {strategy}")
