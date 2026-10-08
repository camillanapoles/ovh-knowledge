"""Uso 5 — Embeddings com bge-m3 (base para busca semântica / RAG).

Uso:
    export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
    pip install openai
    python 05_embeddings.py
"""
import math
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
    api_key=os.environ["OVH_AI_ENDPOINTS_ACCESS_TOKEN"],
)

texts = ["Gosto de futebol.", "O tempo está bom hoje.", "Receita de bolo de chocolate."]
emb = client.embeddings.create(model="bge-m3", input=texts)
vecs = [d.embedding for d in emb.data]
print("textos:", len(vecs), "| dimensões:", len(vecs[0]))


def cos(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb)


q = client.embeddings.create(model="bge-m3", input=["Qual seu esporte favorito?"]).data[0].embedding
ranked = sorted(zip(texts, [cos(q, v) for v in vecs]), key=lambda t: t[1], reverse=True)
for t, s in ranked:
    print(f"{s:.3f}  {t}")
