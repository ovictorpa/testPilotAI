# generate_prompts.py

import json
import os
from agents.prompt_generator_agent import PromptGeneratorAgent

def load_code():
    with open("prompts/code.py", "r", encoding="utf-8") as file:
        return file.read()

def generate_prompts(code: str, num_variations: int = 3):
    agent = PromptGeneratorAgent(base_code=code, num_variations=num_variations)
    prompt_variants = agent.generate_prompts()

    # Adaptar para o formato compatível com o restante da automação
    prompts = {
        variant["strategy"]: variant["prompt"]
        for variant in prompt_variants
    }

    save_path = os.path.join("prompts", "generated_prompts.json")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(prompts, f, indent=4)

    return prompts

if __name__ == "__main__":
    code = load_code()
    prompts = generate_prompts(code)
    print("Prompts gerados:")
    for strategy, prompt in prompts.items():
        print(f"\n[{strategy}]\n{prompt}\n")
