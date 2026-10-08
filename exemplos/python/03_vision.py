"""Uso 3 — Visual LLM: OCR/descrição de imagem local.

Uso:
    export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
    pip install openai
    python 03_vision.py nota_fiscal.jpg
"""
import base64
import mimetypes
import os
import sys
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
    api_key=os.environ["OVH_AI_ENDPOINTS_ACCESS_TOKEN"],
)


def to_data_url(path: str) -> str:
    mime, _ = mimetypes.guess_type(path)
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:{mime or 'image/jpeg'};base64,{b64}"


image = sys.argv[1] if len(sys.argv) > 1 else "nota_fiscal.jpg"
resp = client.chat.completions.create(
    model="Qwen3.8-27B",  # Vision + Reasoning + Function calling, 262K ctx
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Transcreva todo o texto visível (OCR) e resuma em 1 frase, em português."},
            {"type": "image_url", "image_url": {"url": to_data_url(image)}},
        ],
    }],
    max_tokens=1024,
)
print(resp.choices[0].message.content)
