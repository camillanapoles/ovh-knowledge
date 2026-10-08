#!/usr/bin/env bash
# Uso 16 — Batch API em cURL (upload → criar → poll → download)
# Uso: export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key" && bash 16_batch.sh
set -euo pipefail

BASE="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1"

# 1) JSONL de exemplo
cat > requests.jsonl <<'EOF'
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-oss-20b", "messages": [{"role": "user", "content": "Resuma Hamlet em 2 frases."}]}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-oss-20b", "messages": [{"role": "user", "content": "Traduza 'Bom dia' para francês, espanhol e alemão."}]}}
EOF

# 2) Upload
echo "== upload =="
curl "$BASE/files" \
  -H "Authorization: Bearer $OVH_AI_ENDPOINTS_ACCESS_TOKEN" \
  -F purpose="batch" -F file="@requests.jsonl"
echo
echo "Copie o file id acima e crie o batch:"
echo "curl $BASE/batches -H \"Authorization: Bearer \$OVH_AI_ENDPOINTS_ACCESS_TOKEN\" \\"
echo "  -H 'Content-Type: application/json' \\"
echo "  -d '{\"input_file_id\": \"file-...\", \"endpoint\": \"/v1/chat/completions\", \"completion_window\": \"24h\"}'"
