# publish topics at constant rate
# define wheel kinematics

import json
import os
import time
from openai import OpenAI
from llm_config.user_config import UserConfig

# Global Initialization
config = UserConfig()
client = OpenAI(
    api_key=config.openai_api_key
    
)

