import os
from dotenv import load_dotenv
import generator_AI

load_dotenv()

# api_key = os.getenv("CHATGPT_API_KEY")
test = generator_AI.gpt35("Hello, how are you?",
                          ["What is your favourite colour"], "testing")
print(test)
