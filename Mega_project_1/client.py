from openai import OpenAI

client = OpenAI(
    api_key=""
)
completion = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages= [
        { "role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud" },
        {"role": "user","content": "What is programming.",},
    ],
)

print(completion.choices[0].message.content)


