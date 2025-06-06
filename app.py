from flask import Flask, render_template, request, flash, send_from_directory, redirect
from prompts.generator import load_code, generate_prompts
from llms.interact import query_gpt
from llms.generate_tests import generate_tests_from_all_llms
from dotenv import load_dotenv
from evaluator.runner import run_all_tests
import ast
import os
import json
import subprocess
import glob
import threading
from flask import jsonify
from datetime import datetime

generation_status = {"done": False}
app = Flask(__name__)
app.secret_key = 'segredo-super-seguro'

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

TESTS_DIR = 'generated_tests'
RESULTS_DIR = 'evaluation_results'


def get_latest_file(path_pattern):
    files = sorted(glob.glob(path_pattern), reverse=True)
    if not files:
        return None
    return files[0]

def background_generate_tests():
    global generation_status
    try:
        generate_tests_from_all_llms()
        with open("generation_output.json", "w", encoding="utf-8") as f:
            json.dump(tests, f)
        generation_status["done"] = True
    except Exception as e:
        generation_status["error"] = str(e)
        generation_status["done"] = True

@app.route('/start-generate-tests')
def start_generate_tests():
    global generation_status
    generation_status = {
        "done": False,
        "start_time": datetime.now().strftime("%Y%m%d_%H%M%S")
    }
    threading.Thread(target=background_generate_tests).start()
    return render_template("loading.html")

@app.route('/check-status')
def check_status():
    from datetime import datetime

    start_time = generation_status.get("start_time")
    if not start_time:
        return jsonify({"done": False})

    # busca arquivos mais recentes que a geração
    latest_file = get_latest_file(os.path.join(RESULTS_DIR, 'evaluation_*.json'))
    if latest_file:
        filename = os.path.basename(latest_file)
        timestamp_str = filename.replace("evaluation_", "").replace(".json", "")
        if timestamp_str > start_time:
            return jsonify({"done": True})

    return jsonify({"done": False})


@app.route('/', methods=['GET', 'POST'])
def input_handler():
    if request.method == 'POST':
        code = request.form['code']
        try:
            ast.parse(code)
            os.makedirs('prompts', exist_ok=True)
            with open('prompts/code.py', 'w', encoding='utf-8') as f:
                f.write(code)

            flash('✅ Código válido! Pronto para gerar os prompts.', 'success')
            return render_template('index.html', code=code, valid=True)
        except SyntaxError as e:
            flash(f'❌ Erro de sintaxe: {e}', 'danger')
            return render_template('index.html', code=code, valid=False)

    return render_template('index.html', code='', valid=None)


@app.route("/generate-prompts")
def generate_prompts_route():
    try:
        code = load_code()
        prompts = generate_prompts(code)
        return render_template("prompts.html", prompts=prompts)
    except Exception as e:
        return f"Erro ao gerar prompts: {e}"


@app.route('/generate-tests')
def generate_tests_route():
    try:
        with open("generation_output.json", "r", encoding="utf-8") as f:
            tests = json.load(f)
        return render_template("tests.html", tests=tests)
    except Exception as e:
        return f"Erro ao carregar testes gerados: {e}"



@app.route('/dashboard')
def dashboard():
    # Carrega os arquivos mais recentes
    tests_file = get_latest_file(os.path.join(TESTS_DIR, 'tests_*.json'))
    results_file = get_latest_file(os.path.join(RESULTS_DIR, 'evaluation_*.json'))

    if not tests_file or not results_file:
        return "Testes ou resultados não encontrados."

    with open(tests_file, 'r', encoding='utf-8') as f:
        tests_data = json.load(f)

    with open(results_file, 'r', encoding='utf-8') as f:
        results_data = json.load(f)

    # Identifica o teste com maior score
    top_model = None
    top_prompt = None
    top_score = -1
    for model, prompts in results_data.items():
        for prompt_type, result in prompts.items():
            if result['score'] > top_score:
                top_score = result['score']
                top_model = model
                top_prompt = prompt_type

    # Recupera o conteúdo do teste campeão
    best_test = tests_data[top_model][top_prompt]
    best_result = results_data[top_model][top_prompt]

    return render_template('dashboard.html',
                           best_model=top_model,
                           best_prompt=top_prompt,
                           best_test=best_test,
                           best_result=best_result,
                           all_results=results_data,
                           tests_filename=os.path.basename(tests_file))


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(TESTS_DIR, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
