from prompts.generator import generate_prompts, load_code
import evaluator.runner as rn
from llms.interact import query_gpt, query_ollama, query_fireworks
from agents.prompt_optimizer_agent import PromptOptimizerAgent  # INCLUIR AQUI
import json
from datetime import datetime
import os
import subprocess
import sys
import re
import glob
from concurrent.futures import ThreadPoolExecutor, as_completed

ALLOWED_IMPORTS = {"unittest", "pytest", "math", "random", "re", "datetime"}

def extract_code_from_response(response: str) -> str:
    code_blocks = re.findall(r"```(?:python)?\s*(.*?)```", response, re.DOTALL)
    if code_blocks:
        return code_blocks[0].strip()
    return response.strip()

def remove_fake_imports(code: str) -> str:
    lines = code.splitlines()
    clean_lines = []
    for line in lines:
        if re.match(r"^\s*from\s+(your_module|my_module|solution)\s+import\s+", line):
            continue
        if re.match(r"^\s*import\s+(your_module|my_module|solution)", line):
            continue
        clean_lines.append(line)
    return "\n".join(clean_lines).strip()

def remove_unwanted_imports(code: str) -> str:
    lines = code.splitlines()
    clean_lines = []
    for line in lines:
        if line.strip().startswith(("import", "from")):
            if not any(allowed in line for allowed in ALLOWED_IMPORTS):
                continue
        clean_lines.append(line)
    return "\n".join(clean_lines).strip()

def save_tests_as_py(results, output_dir="test_outputs"):
    os.makedirs(output_dir, exist_ok=True)
    for llm_name, prompt_variants in results.items():
        for prompt_type, test_code in prompt_variants.items():
            if isinstance(test_code, str) and not test_code.startswith("Erro"):
                clean_code = extract_code_from_response(test_code)
                clean_code = remove_fake_imports(clean_code)
                clean_code = remove_unwanted_imports(clean_code)
                if clean_code:
                    filename = f"{llm_name}_{prompt_type}.py".replace(" ", "_")
                    path = os.path.join(output_dir, filename)
                    header = (
                        "import sys\n"
                        "import os\n"
                        "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\n"
                    )
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(header + "\n" + clean_code)

def save_generated_tests(results):
    os.makedirs("generated_tests", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"generated_tests/tests_{timestamp}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    return file_path

def generate_tests_from_all_llms():
    code = load_code()
    prompts = generate_prompts(code)

    llms = {
        "CodeLLaMA": lambda prompt: query_ollama(prompt, model='codellama:latest'),
        "CodeGemma": lambda prompt: query_ollama(prompt, model='codegemma:latest'),
        "StarCoder2": lambda prompt: query_ollama(prompt, model='starcoder2:7b')
    }

    # 1. Preparar prompts por modelo para salvar
    prompts_per_model = {model_name: prompts for model_name in llms.keys()}

    # 2. Salvar prompts originais com nome do LLM como chave
    os.makedirs("generated_prompts", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    original_prompts_path = f"generated_prompts/prompts_{timestamp}.json"
    with open(original_prompts_path, "w", encoding="utf-8") as f:
        json.dump(prompts_per_model, f, indent=2, ensure_ascii=False)

    # 3. Carregar a última avaliação E o último arquivo de prompts compatível
    evaluation_files = sorted(glob.glob("evaluation_results/evaluation_*.json"), reverse=True)
    prompt_files = sorted(glob.glob("generated_prompts/prompts_*.json"), reverse=True)

    if evaluation_files and prompt_files:
        last_eval_file = evaluation_files[0]
        last_prompt_file = prompt_files[0]

        try:
            optimizer = PromptOptimizerAgent(
                evaluation_file=last_eval_file,
                original_prompts_file=last_prompt_file,
                top_k=3,
                explore_ratio=0.3
            )
            optimized = optimizer.optimize()
            # optimized agora deve ter chaves por modelo
            # Atualizar prompts conforme otimização
            for model_name in llms.keys():
                if model_name in optimized:
                    prompts_per_model[model_name].update(optimized[model_name])
            print("🧠 Prompts otimizados aplicados com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao aplicar otimização de prompts: {e}")
    else:
        print("⚠️ Nenhum arquivo de avaliação ou prompts encontrado. Usando prompts padrão.")

    results = {}

    def generate_for_llm(llm_name, llm_func):
        model_results = {}
        for prompt_type, prompt_text in prompts_per_model[llm_name].items():
            try:
                response = llm_func(prompt_text)
                code = extract_code_from_response(response)
                if not code:
                    model_results[prompt_type] = f"Erro: código não encontrado na resposta"
                else:
                    model_results[prompt_type] = code
            except Exception as e:
                model_results[prompt_type] = f"Erro: {e}"
        return llm_name, model_results

    from concurrent.futures import ThreadPoolExecutor, as_completed

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

    save_tests_as_py(results)
    print("📄 Arquivos .py válidos salvos em 'test_outputs/'")

    # Execução do runner
    runner_path = os.path.abspath("evaluator/runner.py")
    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.abspath('.')

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
        print("❌ Erro ao executar runner.py")
        print("📤 stdout:", e.stdout)
        print("⚠️ stderr:", e.stderr)


if __name__ == "__main__":
    generate_tests_from_all_llms()
