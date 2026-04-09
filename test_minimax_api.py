#!/usr/bin/env python3

import json
import os
import sys
import urllib.error
import urllib.request


api_key = os.environ.get("MINIMAX_API_KEY")
if not api_key:
    raise SystemExit("MINIMAX_API_KEY is not set")

model = os.environ.get("MINIMAX_MODEL", "MiniMax-M2.7")
prompt = " ".join(sys.argv[1:]) or "Reply with exactly: MINIMAX_CONNECTION_OK"

payload = {
    "model": model,
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

try:
    with urllib.request.urlopen(request, timeout=60) as response:
        data = json.loads(response.read().decode("utf-8"))
except urllib.error.HTTPError as exc:
    error_body = exc.read().decode("utf-8", errors="replace")
    raise SystemExit(f"HTTP {exc.code}: {error_body}")
except urllib.error.URLError as exc:
    raise SystemExit(f"Network error: {exc}")

text = data["choices"][0]["message"]["content"]
if text.startswith("<think>") and "</think>" in text:
    text = text.split("</think>", 1)[1].lstrip()

print(f"Model: {model}")
print(text)
