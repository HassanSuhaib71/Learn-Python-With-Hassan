from openai import OpenAI

client = OpenAI(
    api_key="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"
)
completion = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages= [
        { "role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud" },
        {"role": "user","content": "What is programming.",},
    ],
)

print(completion.choices[0].message.content)

