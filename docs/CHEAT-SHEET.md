# Cheat Sheet — OVHcloud AI Endpoints (1 página)

## URLs
```text
API (OpenAI-compatível): https://oai.endpoints.kepler.ai.cloud.ovh.net/v1
Catálogo (sem auth):     https://catalog.endpoints.ai.ovh.net/rest/v1/models_v2
Manager → Public Cloud → AI & Machine Learning → AI Endpoints → API keys
```

## Setup (30 segundos)
```bash
export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
export OVH_BASE="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1"
curl $OVH_BASE/models -H "Authorization: Bearer $OVH_AI_ENDPOINTS_ACCESS_TOKEN"
# pip install openai | npm install openai
```

## Rotas
| Rota | Uso |
|---|---|
| `POST /v1/chat/completions` | chat, reasoning, visão, tools, JSON, stream, virtual models |
| `POST /v1/responses` | API moderna (input/instructions/output_text) |
| `POST /v1/embeddings` | vetores (1–25 textos/chamada) |
| `POST /v1/audio/transcriptions` | Whisper (multipart: file, language, diarize, response_format) |
| TTS / imagem / guard | endpoint próprio — ver aba API na página do modelo |
| `POST /v1/files` + `/v1/batches` | Batch async (−50%): JSONL → upload → create → poll → download |
| `GET /v1/models` | listar modelos da sua key |

## Snippets mínimos
```python
from openai import OpenAI
import os
c = OpenAI(base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
           api_key=os.environ["OVH_AI_ENDPOINTS_ACCESS_TOKEN"])
# chat
c.chat.completions.create(model="gpt-oss-20b",
    messages=[{"role": "user", "content": "Olá!"}])
# stream: + stream=True, iterar chunk.choices[0].delta.content
# tools: + tools=[...], tool_choice="auto"
# JSON: + response_format={"type": "json_object"}  # ou json_schema
# visão: content=[{"type":"text",...},{"type":"image_url","image_url":{"url":data_url}}]
# embeddings: c.embeddings.create(model="bge-m3", input=["a","b"])
# responses: c.responses.create(model="gpt-oss-20b", instructions="...", input="...", store=False)
# virtual: model="qwen@latest?input_cost<0.5"  → resposta diz qual modelo usou
# STT: c.audio.transcriptions.create(file=open("a.mp3","rb"), model="whisper-large-v3-turbo",
#        language="pt", diarize=True, response_format="verbose_json")
```

## Modelos (atalho)
```text
barato: gpt-oss-20b · Qwen3.5-9B · bge-m3 · whisper-turbo
forte:  gpt-oss-120b · Llama-3.3-70B · Qwen3.8-27B (visão+tools+raciocínio, 262K)
grátis: nvr-tts-* · SDXL · Qwen3Guard-*
```

## Limites
```text
2 req/min anônimo · 400 req/min com key · 2MB payload (10MB VLM)
playground LLM: 1024 tokens saída · batch: 200MB/50k/5 simult · saída batch some em 15 dias
```

## Erros
```text
403 → key inválida/expirada/sem pagamento · 429 → backoff+jitter · 413 → fatiar/comprimir
batch failed → JSONL/ids únicos/mesmo endpoint · expired → janela 48/72h ou fatiar
```

Guia completo: [`docs/GUIA-COMPLETO-OVH-AI-ENDPOINTS.md`](GUIA-COMPLETO-OVH-AI-ENDPOINTS.md)
