from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)