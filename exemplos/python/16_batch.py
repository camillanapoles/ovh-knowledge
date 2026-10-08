"""Uso 16 — Batch API: ciclo completo (JSONL → upload → batch → poll → download).

Uso:
    export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"   # Batch EXIGE key
    pip install openai
    python 16_batch.py
"""
import json
import os
import time
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
    api_key=os.environ["OVH_AI_ENDPOINTS_ACCESS_TOKEN"],
)

# 1) Preparar JSONL (custom_id único por linha, MESMO endpoint em todas)
requests = [
    {"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions",
     "body": {"model": "gpt-oss-20b",
              "messages": [{"role": "user", "content": "Resuma Hamlet em 2 frases."}]}},
    {"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions",
     "body": {"model": "gpt-oss-20b",
              "messages": [{"role": "user", "content": "Traduza 'Bom dia' para francês, espanhol e alemão."}]}},
]
with open("requests.jsonl", "w", encoding="utf-8") as f:
    for r in requests:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

# 2) Upload
f = client.files.create(file=open("requests.jsonl", "rb"), purpose="batch")
print("file:", f.id)

# 3) Criar batch
batch = client.batches.create(
    input_file_id=f.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",  # ou 48h / 72h
    metadata={"description": "Exemplo batch - out/2026"},
)
print("batch:", batch.id, batch.status)

# 4) Poll até estado terminal
while True:
    cur = client.batches.retrieve(batch.id)
    print(cur.status, cur.request_counts)
    if cur.status in ("completed", "failed", "expired", "cancelled"):
        break
    time.sleep(30)

# 5) Download (ordem NÃO garantida → correlacione por custom_id)
final = client.batches.retrieve(batch.id)
if final.output_file_id:
    out = client.files.content(final.output_file_id)
    open("results.jsonl", "wb").write(out.read())
    print("✅ results.jsonl salvo")
if final.error_file_id:
    err = client.files.content(final.error_file_id)
    open("errors.jsonl", "wb").write(err.read())
    print("⚠️ errors.jsonl salvo (algumas requests falharam)")
