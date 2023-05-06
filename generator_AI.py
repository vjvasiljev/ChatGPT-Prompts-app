# Open AI API request. Takes 3 parameteres. Query, Temperature, Max_Tokens(Optional)

import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    before_log
)  # for exponential backoff
# for logging
import logging
# for printing logs to console
import sys
from pprint import pprint
from typing import List, Dict, Tuple

# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
# logger = logging.getLogger(__name__)
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("CHATGPT_API_KEY")

# open AI request with backoff, retry on rate limit exponential wait time.

# @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(10), before=before_log(logger, logging.DEBUG))


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(30))
def accessOpenAI(innerPrompt, temperature, max_tokens=3900):
    print("Generating", innerPrompt)
    language_prompt = ''
    # if language:
    #     language_prompt = ' Write it in ' + language + '.'

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=innerPrompt + language_prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=0,
        presence_penalty=1)
    response = response.choices[0].text


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(30))
def gpt(system_prompt: str, prompts: List[str], comment: str = 'Not Specified.', version: int = 3):
    gpt_model = ''
    if version == 3:
        gpt_model = 'gpt-3.5-turbo'
    elif version == 4:
        gpt_model = 'gpt-4'
    print(f"[{gpt_model}] Generating: {comment}")
    messages_object = [{"role": "system",
                        "content": system_prompt}]

    # If there are even number of prompts, the last prompt is assistants and probably will be ignored
    if len(prompts) % 2 == 0:
        print("WARNING: Last prompt was from assistant and probably will be ignored")

    # Autogenerate user and assistant prompts for chat history. Iterate an array. First item is always a user prompt, then assistant, then user and so on.
    for count, prompt in enumerate(prompts):
        # print(count, prompt)
        role = ''
        if count == 0 or count % 2 == 0:
            role = "user"
        elif count % 2 == 1:
            role = "assistant"
        messages_object.append({"role": role, "content": prompt})

    # print(messages_object)
    # {"role": "assistant",
    #     "content": "The Los Angeles Dodgers won the World Series in 2020."},
    # {"role": "user", "content": "Where was it played?"}

    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=messages_object)
    # pprint(response)
    text = response["choices"][0]["message"]["content"]
    # print(text)
    text = text.strip()
    return text


# gpt35("You are sarcastic", ["Generate a a joke",
#       "Meters", "Brainstorm a science fact", "help", "fun", "joke"])
