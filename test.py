# check if cuda is available
import torch
import os

print(torch.cuda.is_available())
torch.cuda.empty_cache()
key = os.getenv("OPENAI_API_KEY")
print(type(key))