# ovh-knowledge — OVHcloud AI Endpoints 🇧🇷

Base de conhecimento em português sobre **como a OVH fornece modelos LLM e endpoints (AI Endpoints) e como utilizá-los** — do zero ao código de produção.

## Comece por aqui

| Documento | O que é |
|---|---|
| **[docs/GUIA-COMPLETO-OVH-AI-ENDPOINTS.md](docs/GUIA-COMPLETO-OVH-AI-ENDPOINTS.md)** | 📘 Guia completo: visão executiva → **mapa diagramático de etapas** → 18 tipos de uso com explicação + código (Python/JS/cURL) → limites, preços, troubleshooting |
| **[docs/CATALOGO-MODELOS.md](docs/CATALOGO-MODELOS.md)** | 📚 Os 20 modelos do catálogo: preço, licença, contexto, capacidades |
| **[docs/CHEAT-SHEET.md](docs/CHEAT-SHEET.md)** | ⚡ 1 página: URLs, rotas, snippets mínimos, limites, erros |
| **[exemplos/](exemplos)** | 💻 Código executável: `python/` (8 scripts), `javascript/` (2), `curl/` (3) |

## Em 30 segundos

```bash
export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"  # Manager → Public Cloud → AI & ML → AI Endpoints → API keys
pip install openai
python exemplos/python/01_chat.py
```

API unificada (OpenAI-compatível): `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`

## Mapa de etapas (resumo)

```
ETAPA 0 (conta+projeto+pagamento) → ETAPA 1 (API key) → ETAPA 2 (catálogo+playground)
  → ETAPA 3A (BASE, tempo real: /v1/*) ou 3B (BATCH async −50%: /v1/files+/v1/batches)
  → ETAPA 4 (produção: billing, limites, lifecycle)
```

Ver diagrama completo (mermaid) no guia. Pesquisa consolidada em 08/10/2026 a partir da página oficial, catálogo e documentação OVHcloud.
