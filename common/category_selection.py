import os
from huggingface_hub import InferenceClient

"""
Documentation: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
"""

PROMPT = "Определи категорию жалобы '{}' одним из вариантов. Варианты: [техническая, оплата, другое]. Ответ только одним словом."

def analyze():
    client = InferenceClient(
        provider="auto",
        api_key=os.environ["HF_TOKEN"],
    )

    completion = client.chat.completions.create(  # pyright: ignore
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=[
            {
                "role": "user",
                "content": PROMPT.format("Не приходит SMS-код.")
            }
        ],
    )

    print(completion.choices[0].message)
