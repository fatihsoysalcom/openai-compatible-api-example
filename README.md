# OpenAI Compatible API Example

This example demonstrates how to use the `openai` Python library to interact with both the official OpenAI API and a hypothetical OpenAI-compatible alternative API. It highlights how to switch between providers by simply changing the `base_url` parameter, illustrating the article's concept of reducing vendor lock-in and increasing flexibility. This approach allows developers to optimize costs and adapt to future technological advancements with minimal code changes.

## Language

`python`

## How to Run

1. Install the OpenAI library: `pip install openai`
2. Set your OpenAI API key: `export OPENAI_API_KEY="your_openai_api_key_here"`
3. To demonstrate the alternative, set `export ALTERNATIVE_BASE_URL="http://localhost:8000/v1"` (replace with a real compatible endpoint like from LiteLLM, vLLM, or another provider).
4. Run the script: `python main.py`

## Original Article

This example accompanies the Turkish article: [Yapay Zeka Çıkarım API'ları Neden Kritik ve 2026'da Neler Değişecek?](https://fatihsoysal.com/blog/yapay-zeka-cikarim-apilari-neden-kritik-ve-2026da-neler-degisecek/).

## License

MIT — see [LICENSE](LICENSE).
