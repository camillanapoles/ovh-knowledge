"""Uso 7 — Function/Tool calling (loop agente): clima de Paris.

Uso:
    export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
    pip install openai
    python 07_tools.py
"""
import json
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
    api_key=os.environ["OVH_AI_ENDPOINTS_ACCESS_TOKEN"],
)
MODEL = "Meta-Llama-3_3-70B-Instruct"  # tem Function calling

TOOLS = [{
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Obtém o clima atual de uma cidade.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "A cidade"},
                "country": {"type": "string", "description": "Código do país, 2 letras"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location", "country"],
        },
    },
}]


def get_current_weather(location, country, unit="celsius"):
    # Troque por sua API real (OpenWeather etc.)
    return json.dumps({"location": location, "country": country, "temp": 21, "unit": unit})


messages = [{"role": "user", "content": "Como está o clima em Paris?"}]
msg = client.chat.completions.create(
    model=MODEL, messages=messages, tools=TOOLS, tool_choice="auto", temperature=0.15
).choices[0].message
messages.append(msg)

for call in (msg.tool_calls or []):
    assert call.function.name == "get_current_weather"
    result = get_current_weather(**json.loads(call.function.arguments))
    print(f"🔧 tool_call {call.function.name}{call.function.arguments} → {result}")
    messages.append({"role": "tool", "tool_call_id": call.id, "content": result})

final = client.chat.completions.create(model=MODEL, messages=messages, temperature=0.15)
print("🤖", final.choices[0].message.content)
