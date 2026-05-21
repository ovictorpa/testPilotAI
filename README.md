# Towards a Multidimensional Diagnostic Framework for Automated Test Quality Assessment

### We introduce a fully automated pipeline that

1. **Generates unit tests** for any Python function/class using multiple open‑source LLMs.  
2. **Applies three prompt strategies** (*zero‑shot*, *few‑shot*, *chain‑of‑thought*).  
3. **Evaluates each test** on eight objective attributes (execution result, statement & function coverage, assert diversity, edge‑case handling, and six AST‑based test‑smells).  
4. **Computes a Test Quality Score (TQS)** and exports ready‑to‑analyze datasets.

The infrastructure is reproducible on local hardware, vendor‑neutral, and easily extensible to new models or metrics.

## Available Data

The data extracted from the empirical study is available in the ``tqs_paper/`` directory

## Quick Requirements

- Python ≥ 3.10
- ollama CLI
- coverage, flake8, pandas, seaborn, matplotlib
- 16 GB RAM (minimum) for 7-13 B models
- OS: Linux/macOS/Windows tested

## Quick-start (local execution)

1. Install the dependencies
```
pip install -r requirements.txt
```


3. Define the LLMs

 Install the LLMs with ollama, see available models in https://ollama.com/search, example:
 ```
 ollama pull llama3.3
```

   
 Open the file ```llms/generate_tests.py/``` and define the llm you want, for example:
 ```
 "LLaMA3": lambda prompt: query_ollama(prompt, model='llama3. 3'),
 "CodeLLaMA": lambda prompt: query_ollama(prompt, model='codellama'),
 ```
 The 6 LLMs used in the search are already configured by default (LLaMa3, CodeLLaMa, Gemma, CodeGemma, WizardLM and WizardCoder)

3. Run ```app.py``` and submit the production code to the interface
4. After submitting the production code, a folder will be created with the results ```evaluation_results/```

(Processing time can be high, especially for machines outside the recommendations)

This README omits author names, affiliations and institutional URLs for review‑blindness.
