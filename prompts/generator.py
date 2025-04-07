import json
import os

def load_code():
    with open("prompts/code.py", "r", encoding="utf-8") as file:
        return file.read()


def generate_prompts(code: str):
    base_instruction = "Write unit tests in Python for the following function."

    prompts = {
        "zero-shot": f"{base_instruction}\n\n{code}",
        "few-shot": (
            f"{base_instruction} Here are some examples:\n"
            "Example:\n"
            "def add(a, b): return a + b\n\n"
            "Test:\n"
            "import unittest\n"
            "class TestAdd(unittest.TestCase):\n"
            "    def test_add(self):\n"
            "        self.assertEqual(add(1, 2), 3)\n\n"
            f"Now for the function:\n{code}"
        ),
        "cot": (
            f"{base_instruction} First, think step-by-step about the possible edge cases and logic involved. "
            f"Then write complete tests using unittest.\n\nFunction:\n{code}"
        ),
    }

    save_path = os.path.join("prompts", "generated_prompts.json")

    with open(save_path, "w") as f:
        json.dump(prompts, f, indent=4)

    return prompts
