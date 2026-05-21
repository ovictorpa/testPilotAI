import os
import re
import sys
import json
import shutil
import subprocess
import tempfile

CODES_DIR = "tests_final/"
OUTPUT_JSON = "mutation_scores_pyproteum.json"

PROMPT_TYPES = sorted(["zero_shot", "few_shot", "cot"], key=len, reverse=True)

TIMEOUT_BASELINE = 30   
TIMEOUT_TESTNEW = 30
TIMEOUT_TCASE = 30
TIMEOUT_MUTAGEN = 120
TIMEOUT_EXEMUTA = 300    


def win_to_wsl(path):
    drive, rest = os.path.splitdrive(path)
    return f"/mnt/{drive[0].lower()}{rest.replace(chr(92), '/')}"


def parsear_nome_teste(filename):
    base = filename[5:-3]  
    for pt in PROMPT_TYPES:
        if base.endswith(f"_{pt}"):
            return base[: -len(f"_{pt}")], pt
    return base, "unknown"


def verificar_baseline(task_path, test_file):
    env = os.environ.copy()
    env["PYTHONPATH"] = task_path
    try:
        r = subprocess.run(
            ["python3", "-m", "pytest", test_file, "--tb=no", "-q"],
            cwd=task_path,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_BASELINE,
            env=env,
        )
        return r.returncode == 0
    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False


def parsear_score(output):
    m = re.search(
        r'[Ss]core\s+de\s+[Mm]uta[çc][aã]o\s*[:\-=]?\s*([\d.,]+)\s*%?', output
    )
    if m:
        score = float(m.group(1).replace(",", "."))
        if score > 1.0:
            score /= 100.0
        return {"score": round(score, 4)}

    m = re.search(r'[Mm]utation\s+[Ss]core\s*[:\-=]?\s*([\d.,]+)\s*%?', output)
    if m:
        score = float(m.group(1).replace(",", "."))
        if score > 1.0:
            score /= 100.0
        return {"score": round(score, 4)}

    m_k = re.search(r'[Mm]utantes?\s+[Mm]ortos?\s*[:\-=]?\s*(\d+)', output)
    m_v = re.search(r'[Mm]utantes?\s+[Vv]ivos?\s*[:\-=]?\s*(\d+)', output)
    if m_k and m_v:
        killed = int(m_k.group(1))
        survived = int(m_v.group(1))
        total = killed + survived
        return {
            "score": round(killed / total, 4) if total > 0 else 0.0,
            "killed": killed,
            "survived": survived,
            "total": total,
        }

    m_k = re.search(r'[Kk]illed\s*[:\-=]?\s*(\d+)', output)
    m_s = re.search(r'(?:[Ss]urvived|[Aa]live)\s*[:\-=]?\s*(\d+)', output)
    if m_k and m_s:
        killed = int(m_k.group(1))
        survived = int(m_s.group(1))
        total = killed + survived
        return {
            "score": round(killed / total, 4) if total > 0 else 0.0,
            "killed": killed,
            "survived": survived,
            "total": total,
        }

    m = re.search(r'(\d+)\s+(?:of\s+)?(\d+)\s+[Mm]utants?\s+[Kk]illed', output)
    if m:
        killed = int(m.group(1))
        total = int(m.group(2))
        return {
            "score": round(killed / total, 4) if total > 0 else 0.0,
            "killed": killed,
            "total": total,
        }

    return None


def rodar_pyproteum(task_path, source_file, test_file):
    session_name = test_file[:-3]   
    nome_funcao = source_file[:-3]  

    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(os.path.join(task_path, source_file), os.path.join(tmp, source_file))

        with open(os.path.join(task_path, test_file), "r", encoding="utf-8") as f:
            codigo_teste = f.read()

        codigo_teste = re.sub(
            r"from\s+[a-zA-Z0-9_]+\s+import\s+" + nome_funcao,
            f"from {nome_funcao} import {nome_funcao}",
            codigo_teste,
        )
        if (
            f"from {nome_funcao} import" not in codigo_teste
            and f"import {nome_funcao}" not in codigo_teste
        ):
            codigo_teste = f"from {nome_funcao} import *\n" + codigo_teste

        with open(os.path.join(tmp, test_file), "w", encoding="utf-8", newline="\n") as f:
            f.write(codigo_teste)

        passos = [
            {
                "nome": "testnew",
                "cmd": ["python3", "-m", "pyproteum", "testnew", "--D", ".", "--S", source_file, session_name],
                "timeout": TIMEOUT_TESTNEW,
                "fatal": True,
            },
            {
                "nome": "tcase",
                "cmd": ["python3", "-m", "pyproteum", "tcase", "--add", "--S", test_file, session_name],
                "timeout": TIMEOUT_TCASE,
                "fatal": True,
            },
            {
                "nome": "mutagen",
                "cmd": ["python3", "-m", "pyproteum", "mutagen", "--create", session_name],
                "timeout": TIMEOUT_MUTAGEN,
                "fatal": True,
            },
            {
                "nome": "exemuta",
                "cmd": ["python3", "-m", "pyproteum", "exemuta", "--exec", session_name],
                "timeout": TIMEOUT_EXEMUTA,
                "fatal": False,
            },
        ]

        output_completo = ""
        output_exemuta = ""

        for passo in passos:
            try:
                r = subprocess.run(
                    passo["cmd"],
                    cwd=tmp,
                    capture_output=True,
                    text=True,
                    timeout=passo["timeout"],
                )
                saida = (r.stdout or "") + (r.stderr or "")
                output_completo += saida

                if passo["nome"] == "exemuta":
                    output_exemuta = saida

                if r.returncode != 0 and passo["fatal"]:
                    print(f" [ERRO:{passo['nome']} rc={r.returncode}]", end="")
                    return None, output_completo

            except subprocess.TimeoutExpired:
                print(f" [TIMEOUT:{passo['nome']}]", end="")
                return None, output_completo
            except Exception as e:
                print(f" [EXCECAO:{passo['nome']}:{e}]", end="")
                return None, output_completo

        resultado = parsear_score(output_exemuta) or parsear_score(output_completo)
        return resultado, output_completo


def main():
    task_dirs = sorted(
        [
            d for d in os.listdir(CODES_DIR)
            if d.startswith("task_") and os.path.isdir(os.path.join(CODES_DIR, d))
        ],
        key=lambda x: int(re.search(r"\d+", x).group()),
    )

    resultados = []
    total_tasks = len(task_dirs)

    for idx, task_dir in enumerate(task_dirs):
        task_id = re.search(r"\d+", task_dir).group()
        task_path = os.path.abspath(os.path.join(CODES_DIR, task_dir))
        arquivos = os.listdir(task_path)

        source_files = [f for f in arquivos if f.endswith(".py") and not f.startswith("test_")]
        test_files = sorted([f for f in arquivos if f.startswith("test_") and f.endswith(".py")])

        if not source_files:
            print(f"[{idx+1}/{total_tasks}] Task {task_id}: sem arquivo fonte, pulando")
            continue

        source_file = source_files[0]
        print(f"\n[{idx+1}/{total_tasks}] Task {task_id} | {source_file} | {len(test_files)} testes")

        for test_file in test_files:
            llm, prompt_type = parsear_nome_teste(test_file)
            print(f"  {llm:15s} / {prompt_type:12s} ...", end="", flush=True)

            baseline_ok = verificar_baseline(task_path, test_file)
            if not baseline_ok:
                print(" [BASELINE FAIL]")
                resultados.append({
                    "task_id": int(task_id),
                    "llm": llm,
                    "prompt_type": prompt_type,
                    "baseline_passed": False,
                    "mutation_score": None,
                    "dead": None,
                    "alive": None,
                    "total_mutants": None,
                })
                continue

            resultado, raw_output = rodar_pyproteum(task_path, source_file, test_file)

            if resultado:
                score = resultado.get("score", 0.0)
                killed = resultado.get("killed")
                survived = resultado.get("survived")
                total = resultado.get("total")
                extra = ""
                if killed is not None:
                    extra = f" killed={killed} survived={survived} total={total}"
                print(f" {score * 100:.1f}%{extra}")
            else:
                score = killed = survived = total = None
                print(" [NAO PARSEOU]")
                for line in raw_output.split("\n")[-8:]:
                    if line.strip():
                        print(f"    | {line}")

            resultados.append({
                "task_id": int(task_id),
                "llm": llm,
                "prompt_type": prompt_type,
                "baseline_passed": True,
                "mutation_score": score,
                "mutants_killed": killed,
                "mutants_survived": survived,
                "total_mutants": total,
            })

        with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)

    total_ok = sum(1 for r in resultados if r["mutation_score"] is not None)
    total_baseline_fail = sum(1 for r in resultados if not r["baseline_passed"])
    total_pyproteum_fail = sum(
        1 for r in resultados if r["baseline_passed"] and r["mutation_score"] is None
    )
    scores = [r["mutation_score"] for r in resultados if r["mutation_score"] is not None]

    print(f"\n[OK] Concluido!")
    print(f"  Total de entradas        : {len(resultados)}")
    print(f"  Baseline falhou (pulados): {total_baseline_fail}")
    print(f"  pyproteum falhou         : {total_pyproteum_fail}")
    print(f"  Com mutation score       : {total_ok}")
    if scores:
        print(f"  Score medio              : {sum(scores) / len(scores) * 100:.1f}%")
    print(f"  Resultados em            : {OUTPUT_JSON}")


if __name__ == "__main__":
    if sys.platform == "win32":
        script = win_to_wsl(os.path.abspath(__file__))
        cwd = win_to_wsl(os.path.abspath("dataset"))
        result = subprocess.run(
            ["wsl.exe", "-e", "bash", "-c", f"cd '{cwd}' && python3 '{script}'"]
        )
        sys.exit(result.returncode)
    main()
