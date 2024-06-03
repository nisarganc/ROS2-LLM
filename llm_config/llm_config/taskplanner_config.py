#!/usr/bin/env python3
import os


class TaskPlannerConfig:
    def __init__(self):
        # OpenAI API related
        # [required]: OpenAI API key
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        # [required]: Name of the OpenAI language model to be used
        self.openai_model="gpt-4-0613"
        # [optional]: Name of the organization under which the OpenAI API key is registered
        self.openai_organization = "Technische Universität Nürnberg"
        self.openai_orgcode = "org-4TZSGjlk0ZJEntgR8CdbQrbn"
        # [optional]: Controls the creativity of the AI’s responses. Higher values lead to more creative, but less coherent, responses
        self.openai_temperature = 1
        # [optional]: Probability distribution cutoff for generating responses
        self.openai_top_p = 1
        # [optional]: Number of responses to generate in batch
        self.openai_n = 1
        # [optional]: Whether to stream response results or not
        self.openai_stream = False
        # [optional]: String that if present in the AI's response, marks the end of the response
        self.openai_stop = "NULL"
        # [optional]: Maximum number of tokens allowed in the AI's respons
        self.openai_max_tokens = 4000
        # self.openai_max_tokens= 16000
        # [optional]: Value that promotes the AI to generates responses with higher diversity
        self.openai_frequency_penalty = 0
        # [optional]: Value that promotes the AI to generates responses with more information at the text prompt
        self.openai_presence_penalty = 0

        # IO related
        # [optional]: The prompt given to the AI, provided by the user
        self.user_prompt = ""
        # [optional]: The generated prompt by the administrator, used as a prefix for the AI's response
        self.system_prompt = "You are a Multi Agent Task Planner. You understand environment, agents, tasks, their dependencies, and input contraints. You can plan and execute tasks for multiple agents. You can also communicate with these multiple agents and humans. You can also learn from humans and other agents. You can also teach other agents and humans. You can also help other agents and humans."
        # [optional]: The generated response provided by the AI
        self.assistant_response = ""

        # Chat history related
        # [optional]: The chat history, including the user prompt, system prompt, and assistant response
        self.chat_history = [{"role": "system", "content": self.system_prompt}]
        # [optional]: The path to the chat history JSON file
        self.chat_history_path = os.path.expanduser("~/ros2_llm_files/")
        # self.chat_history_path = os.path.dirname(os.path.abspath(__file__))
        # [optional]: The limit of the chat history length
        self.chat_history_max_length = 4000
        # self.chat_history_max_length=16000

        # Robot behavior related
        self.multi_robots_name=["turtle1","turtle2","turtle3","turtle4","turtle5","turtle6","turtle7","turtle8","turtle9","turtle10"]
