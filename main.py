import os
from openai import OpenAI

def get_completion(client, prompt, model="gpt-3.5-turbo"):
    """Sends a chat completion request and returns the response."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def main():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("Please set the OPENAI_API_KEY environment variable.")
        print("You can get one from https://platform.openai.com/api-keys")
        return

    # --- Scenario 1: Using the official OpenAI API ---
    print("\n--- Using Official OpenAI API ---")
    # Initialize client with default OpenAI base URL (https://api.openai.com/v1)
    openai_client = OpenAI(api_key=openai_api_key)

    prompt_openai = "What is the capital of France?"
    print(f"Prompt: {prompt_openai}")
    response_openai = get_completion(openai_client, prompt_openai)
    print(f"Response: {response_openai}")

    # --- Scenario 2: Using an OpenAI-compatible alternative API ---
    print("\n--- Using OpenAI-Compatible Alternative API ---")
    alternative_base_url = os.getenv("ALTERNATIVE_BASE_URL")
    if not alternative_base_url:
        print("ALTERNATIVE_BASE_URL environment variable not set. Skipping alternative API demonstration.")
        print("To run this part, set ALTERNATIVE_BASE_URL to a compatible endpoint (e.g., a local LLM server like LiteLLM, vLLM, or another provider).")
        return

    # Initialize client, explicitly setting the base_url to the alternative provider.
    # This is the core concept: switching providers with minimal code change.
    # The API key might still be required by the alternative, or it could be a dummy value.
    alternative_client = OpenAI(
        api_key=openai_api_key, # Use the same key, or a specific one for the alternative
        base_url=alternative_base_url
    )

    prompt_alt = "Explain the concept of 'vendor lock-in' in software development in one sentence."
    print(f"Prompt: {prompt_alt}")
    # The model name might differ for the alternative provider.
    response_alt = get_completion(alternative_client, prompt_alt, model="local-model") 
    print(f"Response: {response_alt}")

if __name__ == "__main__":
    main()
