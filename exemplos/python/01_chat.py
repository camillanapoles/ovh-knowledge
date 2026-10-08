"""Uso 1 — Chat mínimo (LLM) na OVHcloud AI Endpoints.

Uso:
    export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
    pip install openai
    python 01_chat.py
"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
    api_key=os.environ["OVH_AI_ENDPOINTS_ACCESS_TOKEN"],
)

resp = client.chat.completions.create(
    model="Meta-Llama-3_3-70B-Instruct",  # barato: "gpt-oss-20b"
    messages=[
        {"role": "system", "content": "Você é um assistente prestativo que responde em português."},
        {"role": "user", "content": "Resuma em 2 frases: o que é a OVHcloud AI Endpoints?"},
    ],
    temperature=0.2,
    max_tokens=300,
    seed=42,
)
print(resp.choices[0].message.content)
u = resp.usage
print(f"\ntokens: prompt={u.prompt_tokens} completion={u.completion_tokens} total={u.total_tokens}")
