#!/usr/bin/env bash
# Uso 12 — Speech-to-Text em cURL (transcrição + diarização)
# Uso: export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key" && bash 12_transcribe.sh reuniao.mp3
set -euo pipefail

AUDIO="${1:-reuniao.mp3}"

curl https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/audio/transcriptions \
  -H "Authorization: Bearer $OVH_AI_ENDPOINTS_ACCESS_TOKEN" \
  -F file="@${AUDIO}" \
  -F model="whisper-large-v3-turbo" \
  -F language="pt" \
  -F diarize="true" \
  -F response_format="verbose_json"
echo
