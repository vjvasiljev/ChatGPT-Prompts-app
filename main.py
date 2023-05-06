import os
from dotenv import load_dotenv
import generator_AI
VERSION = 3

load_dotenv()

# api_key = os.getenv("CHATGPT_API_KEY")
system_prompt = "You are a very stric but helpfull chatbot, you do not like to talk much"
comment = "Strict chatbot"
prompts = ["What is the best colour?"]
response = generator_AI.gpt(system_prompt,
                            prompts, comment, VERSION)
print(response)
