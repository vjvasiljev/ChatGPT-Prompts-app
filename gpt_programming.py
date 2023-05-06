import generator_AI
VERSION = 4

# Instructions for the role of the AI
system_prompt = "Act as a language designer for creating a linguistic programming language tailored to ChatGPT prompt programming."
# Logging name of the iteration
comment = "GPT Programming"
# Array of prompts and responses from the AI. [user, AI, user, AI...]
prompts_v1 = ["Suggest functional keywords and syntax that would be essential for this new language, keeping in mind the utility and ease of use for users interacting with ChatGPT. Please provide a list of keywords similar to Python's for, while, if, else, elif, def, class, etc. and briefly explain their purpose in the context of the ChatGPT prompt programming language."]
prompts = ['''Act as a software architect, and help design a linguistic programming framework in Python specifically for ChatGPT prompt programming. This framework should enable prompt engineers to interact with the GPT-model more efficiently by leveraging best practices discovered so far. Python has constructs like for, while, if, else, elif, def, class, etc. In the context of ChatGPT prompt programming, suggest functional keywords and syntax similar to "Brainstorm" for idea generation or "Act as [role]" for role-based interactions. Additionally, describe the implementation process, how the framework would look, and the ideal workflow for users interacting with it.''']
# Response from the AI
response = generator_AI.gpt(system_prompt,
                            prompts, comment, VERSION)
print(response)
