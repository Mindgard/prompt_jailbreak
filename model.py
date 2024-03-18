import requests

class Model():
    """
    This class creates a 'Model' which uses a deployed / free HuggingFace
    Inference Endpoint. For example - https://huggingface.co/google/gemma-7b-it?inference_api=true
    """
    def __init__(self, API_URL=None, HF_TOKEN=None):
        assert API_URL, "A HF Inference Endpoint URL is required."
        assert HF_TOKEN, "Please provide a HF Token in jailbreak.py"

        self.API_URL = API_URL
        self.headers = {"Authorization": f"Bearer {HF_TOKEN}"}

    def __call__(self, prompt):
        payload= {
            "inputs": prompt,
            "options": {
                "use_cache": False
            }
        }

        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        generated_text = response.json()[0]['generated_text']
        clean_reponse = generated_text.replace(prompt, "") # Some LLMs like to reply with the original prompt so we clean it up.

        return generated_text
	
