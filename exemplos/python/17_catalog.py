"""Uso 17 — Catalog API: descoberta programática de modelos (sem auth).

Uso:
    pip install requests
    python 17_catalog.py
"""
import requests

catalog = requests.get("https://catalog.endpoints.ai.ovh.net/rest/v1/models_v2").json()
print(f"Total de modelos: {len(catalog)}\n")

for m in catalog:
    print(f"- {m['id']} | {m['category']} | available={m['available']}")

vision = [m for m in catalog
          if "image" in m["metadata"]["model_specs"]["capabilities"]["input_modality"]]
print("\nModelos com visão:", [m["id"] for m in vision])

m = next(m for m in catalog if m["id"] == "gpt-oss-20b")
print("\nDetalhe gpt-oss-20b:", m["category"], "| tags:", m["metadata"].get("tags"))
