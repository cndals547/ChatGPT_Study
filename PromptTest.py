import openai
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content


# prompt = f"""
# Your task is to answer in a consistent style.
#
# <child>: Teach me about patience.
#
# <grandparent>: The river that carves the deepest \
# valley flows from a modest spring; the \
# grandest symphony originates from a single note; \
# the most intricate tapestry begins with a solitary thread.
#
# <child>: Teach me about resilience.
#
# """

data_json = { "employees" :[
    {"name":"Chungmin", "email":"cndald0725@gmail.com"},
    {"name":"Doosan", "email":"chungmin.lee@doosan.com"}
]}

prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""

response = get_completion(prompt, temperature=0)
print(response)
