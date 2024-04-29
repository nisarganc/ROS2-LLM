# check if cuda is available
import torch
print(torch.cuda.is_available())
torch.cuda.empty_cache()
