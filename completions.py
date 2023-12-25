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

    if len(sys.argv) > 2:
        instructions = sys.argv[2]
    else:
        instructions = " "

    send_request(prompt, instructions)

def send_request(prompt, instructions):

    console = Console()

    url = "https://api.neets.ai/v1/chat/completions"

    api_key = os.getenv('NEETS_API')
    headers = {
        'X-API-Key': api_key, 
        'Content-Type': 'application/json'
    }

    # models: mistralai/Mixtral-8X7B-Instruct-v0.1, Neets-7B

    data = {
        "messages": [
            {
                "content": f"{instructions}: {prompt}",
                "role": "user"
            }
        ],
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

    print(response.status_code)

    if response.text:  
        res = response.json()
    else:
        console.print("Empty response received")
        res = None

    console.print(Markdown(res['choices'][0]['message']['content']))

def prompt_res_logger(prompt, res):
    with open('prompt_res.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), prompt, res])


if __name__ == '__main__':
    main()
