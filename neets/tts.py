import requests
import sys
import os
import uuid
import subprocess
import datetime
import csv
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    voice = sys.argv[1]
    text = sys.argv[2]
    get_or_print_voices(voice)
    send_request(voice, text)



def send_request(voice, text): 

    url = "https://api.neets.ai/v1/tts"

    api_key = os.getenv('NEETS_API')
    headers = {
        "Authorization": "Bearer " + api_key, 
        'X-API-Key': api_key
    }
    params = {
        'voice_id': voice,
        'text': text,
        'fmt': 'wav'
    }

    response = requests.get(url, headers=headers, params=params)

    output_file = f'{voice}_{str(uuid.uuid1())}.wav'
    if response.status_code == 200:
        with open(f"audio/{output_file}", 'wb') as file:
            file.write(response.content)
        print(f"Saved audio to {output_file}")
    else:
        print(f"Error: {response.status_code}")
    log_request(output_file, voice, text)
    subprocess.run(['mpv', f"audio/{output_file}"])
    

def get_or_print_voices(voice):
    voices = [
        'angie', 'william', 'donald-trump', 'ben-shapiro', 'mark-zuckerberg', 'tucker-carlson', 'alex-jones', 'aoc', 
        'barack-obama', 'andrew-yang', 'kamala-harris', 'andrew-tate', 'lex-fridman', 'elon-musk', '50-cent', 
        'anderson-cooper', 'angela-merkel', 'anthony-fauci', 'antonio-banderas', 'ariana-grande', 'arnold-schwarzenegger', 
        'barry-white', 'ben-affleck', 'bernie-sanders', 'beyonce', 'bill-clinton', 'dj-khaled', 'tupac', 'will-smith', 
        'bill-oreilly', 'billie-eilish', 'cardi-b', 'casey-affleck', 'conor-mcgregor', 'darth-vader', 'dr-dre', 'dr-phil', 
        'drake', 'elizabeth-holmes', 'emma-watson', 'gilbert-gottfried', 'greta-thunberg', 'grimes', 'hillary-clinton', 
        'jason-alexander', 'jay-z', 'jeff-bezos', 'joe-rogan', 'john-cena', 'jordan-peterson', 'justin-trudeau', 'kanye-west', 
        'kermit', 'lil-wayne', 'matt-damon', 'mike-tyson', 'morgan-freeman', 'patrick-stewart', 'paul-mccartney', 'pokimane', 
        'rachel-maddow', 'ron-desantis', 'sam-altman', 'sbf', 'scarlett-johansson', 'sean-hannity', 'snoop-dogg', 'stephen-hawking', 
        'warren-buffett', 'taylor-swift'
    ]
    if voice in voices:
        return voice 
    else:
        for voice in voices:
            print(voice)
        exit()
    

def log_request(output_file, voice, text):
    text = text.replace('\n', ' ')

    if not os.path.exists('logs'):
        os.makedirs('logs')

    with open('logs/tts_log.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([output_file, datetime.datetime.now(), voice, text])

if __name__ == "__main__":
    main()