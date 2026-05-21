import json
import os

BASE = r"c:\Users\antho\OneDrive\Área de Trabalho\testPilotAI"
FINAL_DATASET = os.path.join(BASE, "dataset", "final_dataset.json")
OUTPUT_DIR = os.path.join(BASE, "dataset", "output")
NEW_DATASET = os.path.join(BASE, "dataset", "final_dataset_enriched.json")

PROMPT_MAP = {
    "zero_shot": "zero-shot",
    "few_shot": "few-shot",
    "cot": "cot",
}

with open(FINAL_DATASET, encoding="utf-8") as f:
    entries = json.load(f)

output_cache = {}

def get_output(task_id):
    if task_id not in output_cache:
        path = os.path.join(OUTPUT_DIR, f"output_task_{task_id}.json")
        with open(path, encoding="utf-8") as f:
            output_cache[task_id] = json.load(f)
    return output_cache[task_id]

def extract_smells(test_smells_dict):
    if not test_smells_dict:
        return []
    return list(test_smells_dict.keys())

new_entries = []
for entry in entries:
    new_entry = dict(entry)
    if "test_smells" not in entry:
        task_id = entry["task_id"]
        llm = entry["llm"]
        prompt_type_raw = entry["prompt_type"]
        prompt_type = PROMPT_MAP.get(prompt_type_raw, prompt_type_raw)

        try:
            output = get_output(task_id)
            llm_data = output.get(llm, {})
            pt_data = llm_data.get(prompt_type, {})

            if pt_data:
                new_entry["test_smells"] = extract_smells(pt_data.get("test_smells", {}))
                new_entry["functions_tested"] = pt_data.get("functions_tested", None)
                new_entry["total_functions"] = pt_data.get("total_functions", None)
                new_entry["assert_types"] = pt_data.get("assert_types", [])
                new_entry["edge_case_found"] = pt_data.get("edge_case_found", None)
            else:
                print(f"WARNING: No data found for task={task_id}, llm={llm}, prompt_type={prompt_type}")
                new_entry["test_smells"] = []
                new_entry["functions_tested"] = None
                new_entry["total_functions"] = None
                new_entry["assert_types"] = []
                new_entry["edge_case_found"] = None
        except FileNotFoundError:
            print(f"WARNING: Output file not found for task={task_id}")
            new_entry["test_smells"] = []
            new_entry["functions_tested"] = None
            new_entry["total_functions"] = None
            new_entry["assert_types"] = []
            new_entry["edge_case_found"] = None

    new_entries.append(new_entry)

with open(NEW_DATASET, "w", encoding="utf-8") as f:
    json.dump(new_entries, f, indent=2, ensure_ascii=False)

print(f"Done! Wrote {len(new_entries)} entries to {NEW_DATASET}")
