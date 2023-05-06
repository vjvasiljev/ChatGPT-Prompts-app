import generator_AI
VERSION = 4

# Instructions for the role of the AI
system_prompt = "Act as a prompt generator for ChatGPT."
# Logging name of the iteration
comment = "Prompt Generator"
# Variables for the prompt
desired_prompt = "If we would be creating a linguistic programming framework in python for ChatGPT prompt programming, what would be the functional keywords and syntax? Python has for, while, if, else, elif, def, class, etc. The goal of this programming language/framework is to create a way for prompt engineers to interact with the existing gpt-model in a more eficient way, utilizes all of the best practise that have been discovored so far, in a controlled and effective way. Examples of effective interactions: Using the Brainstorm keyword for generating ideas, Act as...  - a great way to tell chatGPT what role is should play. What would be the correct keywords for ChatGPT prompt programming? Also how would you implement this? How would this framework look and what would be the workflow?"
# Array of prompts and responses from the AI. [user, AI, user, AI...]
prompts = [
    f'''I will state what I want and you will engineer a prompt that would yield the best and most desirable response from ChatGPT. Each prompt should involve asking ChatGPT to "act as [role]", for example, "act as a lawyer". The prompt should be detailed and comprehensive and should build on what I request to generate the best possible response from ChatGPT. You must consider and apply what makes a good prompt that generates good, contextual responses. Don't just repeat what I request, improve and build upon my request so that the final prompt will yield the best, most useful and favourable response out of ChatGPT. Place any variables in square brackets. Here is the prompt I want: {desired_prompt}?''']
# Response from the AI
response = generator_AI.gpt(system_prompt,
                            prompts, comment, VERSION)
print(response)
