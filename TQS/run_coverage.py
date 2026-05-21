import json
import os
import subprocess
import glob
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = os.path.join(BASE_DIR, "tests_final")
JSON_PATH = os.path.join(BASE_DIR, "mutation_scores_pyproteum.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    entries = json.load(f)

def get_source_file(task_dir):
    py_files = [
        f for f in os.listdir(task_dir)
        if f.endswith(".py") and not f.startswith("test_")
    ]
    if len(py_files) == 1:
        return py_files[0].replace(".py", "")
    return None

def run_coverage(task_dir, test_file, source_module):
    cov_json = os.path.join(task_dir, "coverage.json")
    if os.path.exists(cov_json):
        os.remove(cov_json)

    result = subprocess.run(
        [
            "python", "-m", "pytest", test_file,
            f"--cov={source_module}",
            "--cov-report=json",
            "--quiet", "--tb=no", "--no-header"
        ],
        cwd=task_dir,
        capture_output=True,
        text=True,
        timeout=60
    )

    if os.path.exists(cov_json):
        with open(cov_json, "r") as f:
            data = json.load(f)
        return round(data["totals"]["percent_covered"] / 100, 4)
    return None

for entry in entries:
    task_id = entry["task_id"]
    llm = entry["llm"]
    prompt_type = entry["prompt_type"]

    task_dir = os.path.join(TESTS_DIR, f"task_{task_id}")
    test_file = f"test_{llm}_{prompt_type}.py"
    test_path = os.path.join(task_dir, test_file)

    if not os.path.exists(test_path):
        print(f"[SKIP] {test_path} not found")
        entry["coverage"] = None
        continue

    if not entry.get("baseline_passed", False):
        print(f"[SKIP] task_{task_id}/{test_file} — baseline_passed=False")
        entry["coverage"] = None
        continue

    source_module = get_source_file(task_dir)
    if source_module is None:
        print(f"[SKIP] task_{task_id} — could not determine source file")
        entry["coverage"] = None
        continue

    print(f"[RUN] task_{task_id}/{test_file} covering {source_module}.py ...", end=" ")
    try:
        cov = run_coverage(task_dir, test_file, source_module)
        entry["coverage"] = cov
        print(f"{cov}")
    except Exception as e:
        print(f"ERROR: {e}")
        entry["coverage"] = None

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print("\nDone. JSON updated.")
