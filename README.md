# MiniMax Python Chat Completions Example

Minimal Python script for calling the MiniMax OpenAI-compatible chat API at `https://api.minimax.io/v1/chat/completions`.

## Requirements

- Python 3
- A MiniMax API key in `MINIMAX_API_KEY`

## Usage

```bash
export MINIMAX_API_KEY='your_key_here'
python3 test_minimax_api.py
python3 test_minimax_api.py "Write one short sentence about Python."
```

The script reads the API key from the environment and does not hardcode secrets.
