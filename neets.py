import requests
import sys
import os 
import csv
import datetime
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv



def main():
    load_dotenv()
    prompt = sys.argv[1]
    send_request(prompt)

def send_request(prompt):
    print(prompt)
    url = "https://api.neets.ai/v1/chat/completions"

    api_key = os.getenv('NEETS_API')
    headers = {
        'X-API-Key': api_key, 
        'Content-Type': 'application/json'
    }

    data = {
        "messages": [
            # {
            #     "content": "You are to answer all questions in as if you were an expert programmer",
            #     "role": "assistant"
            # },
            {
                "content": f"{prompt}",
                "role": "user"
            }
        ],
        # "model": "mistralai/Mixtral-8X7B-Instruct-v0.1",
        "model": "Neets-7B",
        "frequency_penalty": 0,
        "max_tokens": 500,
        "n": 1,
        "presence_penalty": 0,
        "response_format": {
            "type": "json_object"
        },
        "seed": -9223372036854776000,
        "stop": "null",
        "stream": "false",
        "temperature": 1,
        "top_p": 1
        }

    response = requests.post(url, json=data, headers=headers)

    if response.text:  # Check if the response is not empty
        res = response.json()
    else:
        print("Empty response received")
        res = None

    console = Console()

    console.print(Markdown(res['choices'][0]['message']['content']))

def prompt_res_logger(prompt, res):
    with open('prompt_res.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), prompt, res])


if __name__ == '__main__':
    main()
