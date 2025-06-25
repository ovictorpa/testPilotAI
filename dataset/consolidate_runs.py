import os
import json
import glob
from datetime import datetime

def load_latest_json(directory, prefix):
    """
    Carrega o JSON mais recente em um diretório com base no prefixo do nome do arquivo.
    """
    files = sorted(glob.glob(os.path.join(directory, f"{prefix}_*.json")), reverse=True)
    if not files:
        raise FileNotFoundError(f"Nenhum arquivo encontrado em {directory} com prefixo {prefix}_")
    with open(files[0], "r", encoding="utf-8") as f:
        return json.load(f), os.path.basename(files[0]).replace(f"{prefix}_", "").replace(".json", "")

def consolidate_data():
    # Carrega os dados mais recentes de cada etapa
    prompts, ts_prompts = load_latest_json("generated_prompts", "prompts")
    tests, ts_tests = load_latest_json("generated_tests", "tests")
    evaluation, ts_eval = load_latest_json("evaluation_results", "evaluation")

    # Usa o timestamp da avaliação como identificador da execução
    consolidated_ts = ts_eval

    # Carrega arquivo acumulado (ou cria um novo)
    consolidated_path = "consolidated/consolidated_data.json"
    os.makedirs("consolidated", exist_ok=True)
    if os.path.exists(consolidated_path):
        with open(consolidated_path, "r", encoding="utf-8") as f:
            consolidated = json.load(f)
    else:
        consolidated = {}

    # Adiciona dados da nova execução
    consolidated[consolidated_ts] = {
        "prompts": prompts,
        "tests": tests,
        "evaluation": evaluation
    }

    # Salva novamente, mantendo histórico
    with open(consolidated_path, "w", encoding="utf-8") as f:
        json.dump(consolidated, f, indent=2, ensure_ascii=False)

    print(f"✅ Dados consolidados para execução {consolidated_ts} em: {consolidated_path}")

if __name__ == "__main__":
    consolidate_data()
