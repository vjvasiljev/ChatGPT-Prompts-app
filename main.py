import generator_AI
VERSION = 3

# Instructions for the role of the AI
system_prompt = "You are a very stric but helpfull chatbot, you do not like to talk much"
# Logging name of the iteration
comment = "Strict chatbot"
# Array of prompts and responses from the AI. [user, AI, user, AI...]
prompts = ["What is the best colour?"]
# Response from the AI
response = generator_AI.gpt(system_prompt,
                            prompts, comment, VERSION)
print(response)
