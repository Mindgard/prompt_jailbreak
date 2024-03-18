# Prompt Jailbreak Example - HuggingFace Inference Endpoints

This repository demonstrates the use of a prompt jailbreak to expose information within a system prompt. Specifically, we target any LLM hosted on HuggingFace Inference Endpoints. The standard example shows jailbreaks upon `google/gemma-7b-it`.

## Instructions
1. Execute `pip install -r requirements.txt` to install the necessary dependencies.
2. Set your `HF_TOKEN` environment variable in the `jailbreak.py` file - Line 28.
3. Run the jailbreak with `python jailbreak.py`.

The expected output should be two arrays - one containing the original responses from the LLM, and another with the jailbreak applied.

## Other LLMs and Examples
This repo supports any LLM hosted on HuggingFace Inference. If you wish to change the target LLM, simply modify `API_URL` on line 27 in `jailbreak.py`. Furthermore, if you wish to send different user prompts or alter/change the jailbreak or system prompt, you can also find this at the top of the script.
