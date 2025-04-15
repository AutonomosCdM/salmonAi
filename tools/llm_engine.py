import os
import requests

def ask_llm(provider: str, prompt: str) -> str:
    if provider == 'groq':
        api_key = os.getenv("GROQ_API_KEY")
        url = "https://api.groq.com/openai/v1/chat/completions"
        model = "meta-llama/llama-4-scout-17b-16e-instruct"
    elif provider == 'openai':
        api_key = os.getenv("OPENAI_API_KEY")
        url = "https://api.openai.com/v1/chat/completions"
        model = "gpt-4o"
    elif provider == 'claude':
        api_key = os.getenv("CLAUDE_API_KEY")
        url = "https://api.anthropic.com/v1/messages"
        model = "claude-3-sonnet-20240229"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        data = {
            "model": model,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()['content'][0]['text']
    else:
        raise ValueError("LLM provider no soportado.")

    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, json=data, headers=headers)
    print("DEBUG STATUS:", response.status_code)
    print("DEBUG RESPONSE:", response.text)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise requests.exceptions.HTTPError(f"API request failed with status {response.status_code}: {response.text}")
