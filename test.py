import torch
import os
from openai import OpenAI
from llm_config.user_config import UserConfig

# check if cuda is available
print(torch.cuda.is_available())
torch.cuda.empty_cache()


config = UserConfig()
client = OpenAI(
    api_key=config.openai_api_key
)

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")