from prompts.generator import generate_prompts, load_code
import evaluator.runner as rn
from llms.interact import query_gpt, query_ollama, query_fireworks
import json
from datetime import datetime
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def generate_tests_from_all_llms():
    code = load_code()
    prompts = generate_prompts(code)
    results = {}

    # Lista de LLMs com suas funções
    llms = {
        # Meta
        "LLaMA3": lambda prompt: query_ollama(prompt, model='llama3.2'),
        "CodeLLaMA": lambda prompt: query_ollama(prompt, model='codellama'),

        # Microsoft
        "WizardCoder": lambda prompt: query_ollama(prompt, model='wizardcoder'),
        "WizardLM": lambda prompt: query_ollama(prompt, model='wizardlm2'),

        # Deepseek
        #"DeepSeekR1": lambda prompt: query_ollama(prompt, model='deepseek-r1')
        #"DeepSeek-Coder": lambda prompt: query_ollama(prompt, model='deepseek-coder'),

        # Google
        "Gemma": lambda prompt: query_ollama(prompt, model='gemma'),
        "CodeGemma": lambda prompt: query_ollama(prompt, model='codegemma'),
    }

    def generate_for_llm(llm_name, llm_func):
        model_results = {}
        for prompt_type, prompt_text in prompts.items():
            try:
                code = llm_func(prompt_text)
                model_results[prompt_type] = code
            except Exception as e:
                model_results[prompt_type] = f"Erro: {e}"
        return llm_name, model_results

    # Executa paralelamente usando até 4 threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(generate_for_llm, name, func): name
            for name, func in llms.items()
        }

        for future in as_completed(futures):
            llm_name, model_results = future.result()
            results[llm_name] = model_results
            print(f"✅ Testes gerados com {llm_name}")

    file_path = save_generated_tests(results)
    print(f"✔️ Testes salvos em: {file_path}")

    # ✅ Executa o runner.py
    runner_path = os.path.abspath("evaluator/runner.py")
    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.abspath('.')  # garante acesso a pacotes locais

    try:
        result = subprocess.run(
            [sys.executable, runner_path],
            check=True,
            capture_output=True,
            text=True,
            cwd=os.path.abspath('.'),
            env=env
        )
        print("✅ runner.py executado com sucesso!")
        print("📤 stdout:", result.stdout)
        print("⚠️ stderr:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar runner.py")
        print("📤 stdout:", e.stdout)
        print("⚠️ stderr:", e.stderr)


def save_generated_tests(results):
    os.makedirs("generated_tests", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"generated_tests/tests_{timestamp}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    return file_path
