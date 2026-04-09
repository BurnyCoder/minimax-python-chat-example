# MiniMax Python Chat Completions Example

Minimal Python script for calling the MiniMax OpenAI-compatible chat API at `https://api.minimax.io/v1/chat/completions`.

## Requirements

- Python 3
- A MiniMax API key in `MINIMAX_API_KEY`
- An optional model name in `MINIMAX_MODEL` (defaults to `MiniMax-M2.7`)

## Usage

```bash
export MINIMAX_API_KEY='your_key_here'
python3 test_minimax_api.py
python3 test_minimax_api.py "Write one short sentence about Python."
MINIMAX_MODEL='MiniMax-M2.7' python3 test_minimax_api.py "Write one short sentence about Python."
MINIMAX_MODEL='MiniMax-M2.7-highspeed' python3 test_minimax_api.py "Write one short sentence about Python."
```

The script reads the API key from the environment, accepts the prompt as command-line text, and prints the selected model followed by the response body. Secrets are not hardcoded.
