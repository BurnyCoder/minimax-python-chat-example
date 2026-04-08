#!/usr/bin/env python3

import json
import os
import sys
import urllib.request


api_key = os.environ.get("MINIMAX_API_KEY")
if not api_key:
    raise SystemExit("MINIMAX_API_KEY is not set")

prompt = " ".join(sys.argv[1:]) or "Reply with exactly: MINIMAX_CONNECTION_OK"

payload = {
    "model": "MiniMax-M2.7",
    "messages": [{"role": "user", "content": prompt}],
}

request = urllib.request.Request(
    "https://api.minimax.io/v1/chat/completions",
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    method="POST",
)

with urllib.request.urlopen(request, timeout=60) as response:
    data = json.loads(response.read().decode("utf-8"))

text = data["choices"][0]["message"]["content"]
if text.startswith("<think>") and "</think>" in text:
    text = text.split("</think>", 1)[1].lstrip()

print(text)
