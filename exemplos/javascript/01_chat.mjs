// Uso 1 — Chat mínimo em Node.js
// Uso:
//   export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
//   npm install openai
//   node 01_chat.mjs
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
  apiKey: process.env.OVH_AI_ENDPOINTS_ACCESS_TOKEN,
});

const resp = await client.chat.completions.create({
  model: "Meta-Llama-3_3-70B-Instruct", // barato: "gpt-oss-20b"
  messages: [
    { role: "system", content: "Você é um assistente prestativo que responde em português." },
    { role: "user", content: "Resuma em 2 frases: o que é a OVHcloud AI Endpoints?" },
  ],
  temperature: 0.2,
  max_tokens: 300,
});
console.log(resp.choices[0].message.content);
console.log(`\ntokens: prompt=${resp.usage.prompt_tokens} completion=${resp.usage.completion_tokens}`);
