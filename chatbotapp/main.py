import os
import openai

openai.api_key = "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"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":"Hi ChatGPT. Say hi back!"}
    ]
)
answer = response.choices[0].message.content
print(answer)