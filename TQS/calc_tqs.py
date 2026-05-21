import json
import os

BASE = r"c:\Users\antho\OneDrive\Área de Trabalho\testPilotAI"
INPUT = os.path.join(BASE, "TQS", "final_dataset_tqs.json")
OUTPUT = os.path.join(BASE, "TQS", "final_dataset_tqs_final.json")

MAX_ASSERT_TYPES = 3  # max observed in dataset

def calc_tqs(entry):
    baseline_passed = entry.get("baseline_passed")
    edge_case_found = entry.get("edge_case_found")
    coverage = entry.get("coverage")
    functions_tested = entry.get("functions_tested")
    total_functions = entry.get("total_functions")
    assert_types = entry.get("assert_types") or []
    test_smells = entry.get("test_smells") or []

    # A1: Execution Success
    a1 = 1.0 if baseline_passed is True else 0.0

    # A2: Edge Cases
    a2 = 1.5 if edge_case_found is True else 0.0

    # A3: Code Coverage (already 0-1 scale)
    a3 = float(coverage) if coverage is not None else 0.0

    # A4: Functional Coverage = 0.5 * (functions_tested / total_functions)
    if functions_tested and total_functions:
        a4 = 1.0 * (functions_tested / total_functions)
    else:
        a4 = 0.0

    # A5: Assertion Diversity — stronger weight as best proxy for mutation killing ability
    a5 = min(len(assert_types) / MAX_ASSERT_TYPES, 1.0) * 3.0

    # A6: Execution Failure
    a6 = -1.0 if baseline_passed is False else 0.0

    # A7: Syntax Error — not distinguishable from current JSON fields
    a7 = 0.0

    # A8: Test Smells (-0.5 per type)
    a8 = len(test_smells) * -0.5

    # A9: No-assertion penalty — test with no assertions cannot kill any mutant
    a9 = -1.5 if len(assert_types) == 0 else 0.0

    tqs = round(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9, 4)

    return {
        "a1_exec_success": round(a1, 4),
        "a2_edge_cases": round(a2, 4),
        "a3_coverage": round(a3, 4),
        "a4_func_coverage": round(a4, 4),
        "a5_assert_diversity": round(a5, 4),
        "a6_exec_failure": round(a6, 4),
        "a8_test_smells": round(a8, 4),
        "a9_no_assertion": round(a9, 4),
        "tqs": tqs,
    }

with open(INPUT, encoding="utf-8") as f:
    data = json.load(f)

result = []
for entry in data:
    new_entry = dict(entry)
    scores = calc_tqs(entry)
    new_entry["tqs"] = scores["tqs"]
    result.append(new_entry)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

# Print summary
tqs_vals = [e["tqs"] for e in result]
print(f"TQS calculado para {len(result)} entradas")
print(f"Min TQS: {min(tqs_vals):.4f}")
print(f"Max TQS: {max(tqs_vals):.4f}")
print(f"Média TQS: {sum(tqs_vals)/len(tqs_vals):.4f}")
print()
print("Exemplo (primeira entrada):")
e = result[0]
print(json.dumps({k: e[k] for k in ["task_id","llm","prompt_type","tqs"]}, indent=2))
