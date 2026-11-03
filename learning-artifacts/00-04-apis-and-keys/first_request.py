# Practice for phases/00-setup-and-tooling/04-apis-and-keys/docs/en.md.
# Assemble the raw HTTP request explored during the lesson.
# Reference: https://platform.claude.com/docs/en/api/messages/create
# The key stays in memory; one run sends one generation request.
import getpass
import json
import os
import urllib.error
import urllib.request


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY") or getpass.getpass("API key (hidden): ")
    if not api_key.strip():
        print("API key is missing.")
        return

    payload = {
        "model": "claude-haiku-5-5",
        "max_tokens": 256,
        "messages": [{"role": "user", "content": "Explain neural networks in one sentence."}],
    }
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    request = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read())
    except urllib.error.HTTPError as error:
        print("HTTP status:", error.code)
        try:
            details = json.loads(error.read()).get("error", {})
            print("Error type:", details.get("type", "unknown"))
        except (ValueError, AttributeError):
            print("The server returned an error without a readable JSON error type.")
        return
    except (urllib.error.URLError, TimeoutError) as error:
        print("Connection failed:", type(error).__name__)
        return

    for block in result.get("content", []):
        if block.get("type") == "text":
            print(block["text"])
    print("Token usage:", result.get("usage", {}))
    print("Stop reason:", result.get("stop_reason"))


if __name__ == "__main__":
    main()
