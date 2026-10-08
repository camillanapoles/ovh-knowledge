# Catálogo de Modelos — OVHcloud AI Endpoints (20 modelos, 10/2026)

> Fonte: `https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/` + Catalog API.
> Preços e disponibilidade mudam — confirme sempre no catálogo oficial ou via [Catalog API](GUIA-COMPLETO-OVH-AI-ENDPOINTS.md#uso-17--catalog-api-descoberta-programática-de-modelos).
>
> API unificada: `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1` · Mtoken = milhão de tokens.

## Visual LLM (4) — imagem + texto, todos 262K ctx, Apache 2.0, fp8 (exceto 9B bf16)

| Modelo | Preço in / out (por Mtok) | Params | Capacidades |
|---|---|---|---|
| `Qwen3.8-27B` 🆕 | €0.40 / €2.70 | 27B | Function calling, Vision, Reasoning |
| `Qwen3.6-27B` 🆕 | €0.40 / €2.70 | 27B | Function calling, Vision, Reasoning |
| `Qwen3.5-397B-A17B` 🆕 (MoE gigante) | €0.60 / €3.60 | 397B | Function calling, Vision, Reasoning |
| `Qwen3.5-9B` 🆕 (custo-benefício) | €0.10 / €0.15 | 9.7B | Function calling, Vision, Reasoning |
| `Qwen2.5-VL-72B-Instruct` | €0.91 / €0.91 | 72B, ctx 32K, licença Qwen | Vision |

## Reasoning LLM (2) — gpt-oss, Apache 2.0, fp4, 131K ctx

| Modelo | Preço in / out | Params | Capacidades |
|---|---|---|---|
| `gpt-oss-120b` (forte) | €0.08 / €0.40 | 117B | Function calling, Reasoning |
| `gpt-oss-20b` (barato) | €0.04 / €0.15 | 21B | Function calling, Reasoning |

## LLM clássico (1)

| Modelo | Preço in / out | Params | Capacidades |
|---|---|---|---|
| `Meta-Llama-3_3-70B-Instruct` | €0.67 / €0.67 | 70B, fp8, 131K, Llama 3.3 Community | Function calling |

## Embeddings (3)

| Modelo | Preço (por Mtok in) | Params / licença | Notas |
|---|---|---|---|
| `bge-m3` | €0.01 | 0.567B, MIT, fp16 | multilíngue 100+ idiomas, denso+sparse |
| `bge-multilingual-gemma2` | €0.01 | 0.567B, Gemma, fp16 | SOTA multilíngue (MIRACL/MTEB) |
| `Qwen3-Embedding-8B` 🆕 | €0.10 | 7.6B, Apache 2.0, fp16 | maior qualidade |

## Speech-to-Text (2) — Whisper, Apache 2.0, fp16

| Modelo | Preço (por segundo) | Params | Capacidades |
|---|---|---|---|
| `whisper-large-v3` | €0.00004083 | 1.54B | ASR, Diarização, Tradução |
| `whisper-large-v3-turbo` | €0.00001278 (~3× mais barato) | 0.81B | ASR, Diarização, Tradução |

## Text-to-Speech (4) — NVIDIA Riva, licença Riva, **grátis**

| Modelo | Idioma | Capacidades |
|---|---|---|
| `nvr-tts-en-us` | inglês (EUA) | TTS, Multi-speaker |
| `nvr-tts-de-de` | alemão | TTS, Multi-speaker |
| `nvr-tts-es-es` | espanhol (UE) | TTS, Multi-speaker |
| `nvr-tts-it-it` | italiano | TTS, Multi-speaker |

## Geração de imagem (1) — **grátis**

| Modelo | Params / licença | Capacidades |
|---|---|---|
| `stable-diffusion-xl-base-v10` | 3.5B, OpenRail++, fp32 | Image Generation |

## LLM Guard / Moderação (2) — **beta, grátis**, Apache 2.0, fp16, 32K ctx

| Modelo | Params | Uso |
|---|---|---|
| `Qwen3Guard-Gen-8B` | 8B | moderação precisa |
| `Qwen3Guard-Gen-0.6B` | 0.6B | moderação rápida/leve |

## Filtros úteis do catálogo web

- **Por categoria:** Embeddings · Image Generation · LLM Guard · LLM · Reasoning LLM · Speech To Text · Text To Speech · Visual LLM
- **Por contexto:** 32K · 131K · 262K · **Por série:** bge · gpt-oss · llama · qwen · whisper · stable-diffusion · NVIDIA Riva · qwen3guard
- **Por use-case:** code_chat · code_completion · code_explanation · summarization · translation · sentiment_analysis · entity_extraction · vision · multimodal · speech_to_text · text-to-speech · diarisation · multi-speaker · image_generation · moderation · function calling · structured output · text generation · multilingual…
- **Por tamanho:** Small · Medium · Large · Huge · **Status:** live · new · beta

## Recomendação rápida por objetivo

| Objetivo | 1ª escolha | Alternativa premium |
|---|---|---|
| Chat geral barato | `gpt-oss-20b` | `Meta-Llama-3_3-70B-Instruct` |
| Raciocínio/código difícil | `gpt-oss-120b` | `Qwen3.5-397B-A17B` |
| Visão/OCR/documentos | `Qwen3.8-27B` | `Qwen2.5-VL-72B-Instruct` |
| Código no IDE | `Qwen3.8-27B` | `Qwen3.6-27B` |
| Embeddings/RAG | `bge-m3` | `Qwen3-Embedding-8B` |
| Transcrição | `whisper-large-v3-turbo` | `whisper-large-v3` |
| Fala | `nvr-tts-*` do idioma | — |
| Imagem | `stable-diffusion-xl-base-v10` | — |
| Moderação | `Qwen3Guard-Gen-8B` | `Qwen3Guard-Gen-0.6B` (rápida) |
| Massa/offline | qualquer acima via **Batch −50%** | — |
