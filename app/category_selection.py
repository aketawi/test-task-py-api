from huggingface_hub import InferenceClient
import os

"""
Documentation: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
"""

# PROMPT = "Определи категорию жалобы '{}' одним из вариантов. Варианты: техническая, оплата, другое. Ответ только одним словом."
PROMPT = "Select the category of this support request '{}'. Categories: technical, payment, other. Reply using only one word, this word should be the category."
"""Using a prompt in English, because they seem to provide more accurate answers."""

_client = InferenceClient(
    provider="auto",
    api_key=os.environ["HF_TOKEN"],
)

async def analyze(text: str) -> str:
    completion = _client.chat.completions.create(  # pyright: ignore
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=[
            {
                "role": "user",
                "content": PROMPT.format(text)
            }
        ],
    )
    response = completion.choices[0].message.content
    if response:
        return response.strip().lower()
    else:
        return "other"
