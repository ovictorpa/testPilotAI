# Process — Test Generation & Evaluation Pipeline (auxiliary)

This folder holds the Flask application and LLM-orchestration code that **generated** the raw test suites
later analyzed in [`../tqs_paper/`](../tqs_paper/). It is kept for provenance and transparency, but it is
**not** required to reproduce the paper's reported results — that only needs `tqs_paper/`, whose dataset is
already frozen. Everything in this folder used to live at the repository root; it was moved here so the root
of the repository only contains the `README.md` and `LICENSE` required for the artifact submission.

## What it does

1. You submit a Python function/class through the web UI (`app.py`).
2. The tool builds three prompts (zero-shot, few-shot, chain-of-thought) from that code
   (`prompts/generator.py`).
3. Each prompt is sent to six local LLMs served through [Ollama](https://ollama.com/) — LLaMA 3, CodeLLaMA,
   Gemma, CodeGemma, WizardLM, WizardCoder (`llms/generate_tests.py`, `llms/interact.py`).
4. Each generated test suite is executed and scored (execution status, coverage, assertion types, edge
   cases) by `evaluator/runner.py`.
5. Results are written to `evaluation_results/` and can be inspected via the `/dashboard` route.

This is the tool that produced the raw material in `tqs_paper/tests_final/`; the TQS metric itself is
computed and validated entirely inside `tqs_paper/`, not here.

## Requirements

- Python ≥ 3.10
- [Ollama](https://ollama.com/) installed locally, with the models pulled, e.g.:
  ```
  ollama pull llama3.2
  ollama pull codellama
  ollama pull gemma
  ollama pull codegemma
  ollama pull wizardlm2
  ollama pull wizardcoder
  ```
- An OpenAI API key only if you intend to use `query_gpt` (optional, GPT is not part of the default LLM list
  used in the paper).
- 16 GB RAM (minimum) recommended for running 7–13B local models.
- OS: Linux/macOS/Windows (tested on all three).

## Installation

From the repository root:

```bash
cd process
pip install -r requirements.txt
cp ../.env.example .env   # then fill in your own API keys — never commit this file
```

`.env` variables:

| Variable | Required for |
|---|---|
| `OPENAI_API_KEY` | `llms.interact.query_gpt` (GPT-4o), optional |
| `FIREWORKS_API_KEY` | `llms.interact.query_fireworks` (DeepSeek-V3 via Fireworks), optional |

> **Security note:** earlier revisions of this repository had a `.env` file and a hard-coded API key
> committed to git history. Both have been removed from the tracked files and replaced with environment
> variables read via `python-dotenv`. If you are reusing credentials that were ever present in this
> repository's history, rotate/revoke them — removing a secret from the current tree does not erase it from
> past commits.

## Running

All file paths in this app (`prompts/code.py`, `generated_tests/`, `evaluation_results/`,
`generation_output.json`) are relative to the current working directory, so **run it from inside this
folder**:

```bash
cd process
python app.py
```

Then open `http://127.0.0.1:5000/` in a browser, paste a Python function, and follow the on-screen flow
(`Generate prompts` → `Generate tests` → `Dashboard`). Expected confirmation that it's working: submitting
valid Python code shows a "✅ Código válido!" message and a `prompts/code.py` file appears in this folder.

Processing time can be high, especially on machines without a discrete GPU — this step is optional for
verifying the paper's results, which only depend on the already-collected data in `tqs_paper/`.
