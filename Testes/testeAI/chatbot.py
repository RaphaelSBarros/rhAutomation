import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
