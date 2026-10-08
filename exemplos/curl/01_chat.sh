#!/usr/bin/env bash
# Uso 1 — Chat mínimo em cURL
# Uso: export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key" && bash 01_chat.sh
set -euo pipefail

curl https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OVH_AI_ENDPOINTS_ACCESS_TOKEN" \
  -d '{
    "model": "Meta-Llama-3_3-70B-Instruct",
    "messages": [
      {"role": "system", "content": "Você é um assistente prestativo que responde em português."},
      {"role": "user", "content": "Resuma em 2 frases: o que é a OVHcloud AI Endpoints?"}
    ],
    "temperature": 0.2,
    "max_tokens": 300
  }'
echo
