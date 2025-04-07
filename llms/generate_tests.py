from prompts.generator import generate_prompts, load_code
from llms.interact import query_gpt, query_ollama
import json
from datetime import datetime
import os


def generate_tests_from_all_llms():
    code = load_code()
    prompts = generate_prompts(code)

    results = {}

    llms = {
        # "GPT-4": lambda prompt: query_gpt(prompt, model="gpt-4"),  # se ativar futuramente
        #"LLaMA3": lambda prompt: query_ollama(prompt, model='llama3'),
        "CodeLLaMA": lambda prompt: query_ollama(prompt, model='codellama'),
        "Deepseek": lambda prompt: query_ollama(prompt, model='deepseek-coder')
    }

    for llm_name, llm_func in llms.items():
        results[llm_name] = {}
        for prompt_type, prompt_text in prompts.items():
            try:
                test_code = llm_func(prompt_text)
                results[llm_name][prompt_type] = test_code
            except Exception as e:
                results[llm_name][prompt_type] = f"Erro: {e}"

    file_path = save_generated_tests(results)
    print(f"✔️ Testes salvos em: {file_path}")
    return results


def save_generated_tests(results):
    os.makedirs("generated_tests", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"generated_tests/tests_{timestamp}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    return file_path