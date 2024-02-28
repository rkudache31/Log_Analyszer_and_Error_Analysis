#!/usr/bin/env python

import openai
import os
import sys
from openai import OpenAI
#from dotenv import load_dotenv, find_dotenv
#_ = load_dotenv(find_dotenv()) # read local .env file
arg1 = sys.argv[1] if len(sys.argv) > 1 else None
#openai.api_key  = os.getenv('OPENAI_API_KEY')
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    client = OpenAI(
    # This is the default and can be omitted
   # api_key="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",
    #api_key="asst_YVUfpklQwrhacAapICHIVeoY"
    api_key="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"
    )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    raw_input= response.choices[0].message
    return raw_input.content
print(arg1)
lamp_review =arg1
prompt = f"""
provide resoltion in error review, 
which is delimited with triple backticks?

Review text: ```{lamp_review}```
"""
response = get_completion(prompt)
print(response)