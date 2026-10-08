// Uso 9 — Streaming em Node.js
// Uso:
//   export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
//   npm install openai
//   node 09_stream.mjs
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
  apiKey: process.env.OVH_AI_ENDPOINTS_ACCESS_TOKEN,
});

const stream = await client.chat.completions.create({
  model: "gpt-oss-20b",
  messages: [{ role: "user", content: "Conte uma história curta sobre um robô, em português." }],
  stream: true,
  max_tokens: 500,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
console.log();
