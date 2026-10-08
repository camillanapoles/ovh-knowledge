"""Uso 12 — Speech-to-Text: transcrição + diarização + legendas SRT.

Uso:
    export OVH_AI_ENDPOINTS_ACCESS_TOKEN="sua-key"
    pip install openai
    python 12_transcribe.py reuniao.mp3
"""
import os
import sys
from openai import OpenAI

client = OpenAI(
    base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
    api_key=os.environ["OVH_AI_ENDPOINTS_ACCESS_TOKEN"],
)

audio = sys.argv[1] if len(sys.argv) > 1 else "reuniao.mp3"

with open(audio, "rb") as f:
    t = client.audio.transcriptions.create(
        file=f,
        model="whisper-large-v3-turbo",
        language="pt",
        diarize=True,
        timestamp_granularities=["segment"],
        response_format="verbose_json",
        temperature=0,
    )
print("TEXTO:", t.text, "\n")
for seg in (getattr(t, "segments", None) or []):
    start = seg["start"] if isinstance(seg, dict) else seg.start
    text = seg["text"] if isinstance(seg, dict) else seg.text
    speaker = seg.get("speaker", "?") if isinstance(seg, dict) else getattr(seg, "speaker", "?")
    print(f"[{start:7.1f}s] {speaker}: {text}")

with open(audio, "rb") as f:
    srt = client.audio.transcriptions.create(
        file=f, model="whisper-large-v3-turbo", language="pt", response_format="srt"
    )
with open("transcricao.srt", "w", encoding="utf-8") as f:
    f.write(srt if isinstance(srt, str) else str(srt))
print("\n✅ Legendas salvas em transcricao.srt")
