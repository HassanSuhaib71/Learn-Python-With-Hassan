from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="api-key",
)

command = '''
[4:48 PM, 12/18/2024] Háśšāñ Śûhąîß Ãßßáşï: hello
[4:49 PM, 12/18/2024] Own Telenor: How are
[4:49 PM, 12/18/2024] Háśšāñ Śûhąîß Ãßßáşï: fine and you
[4:49 PM, 12/18/2024] Own Telenor: Good
[4:49 PM, 12/18/2024] Own Telenor: How about your study
[4:49 PM, 12/18/2024] Háśšāñ Śûhąîß Ãßßáşï: its going well
[4:50 PM, 12/18/2024] Háśšāñ Śûhąîß Ãßßáşï: and what about your course
[4:50 PM, 12/18/2024] Own Telenor: Going well
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named harry who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Harry"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)