"""Uso 9 — Streaming token-a-token (SSE).

Uso:
    export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
    pip install openai
    python 09_stream.py
"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
    api_key=os.environ["OVH_AI_ENDPOINTS_ACCESS_TOKEN"],
)

stream = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role": "user", "content": "Conte uma história curta sobre um robô, em português."}],
    stream=True,
    max_tokens=500,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
print()
