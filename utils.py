import json
import random
import string
import requests
import os


def generate_name() -> str:
    # resp = requests.request('GET', 'https://www.reddit.com/api/v1/generate_username.json')
    resp = requests.get('https://www.reddit.com/api/v1/generate_username.json')
    print('status code: ' + str(resp.status_code) + ' raw json: ' + str(resp.json()))
    if resp.status_code == 200:
        json_format = json.loads(resp.text)
        return random.choice(json_format['usernames'])
    name_length = random.randint(10, 20)
    generated_name = str().join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=name_length))
    return generated_name


def generate_password() -> str:
    password_length = random.randint(8, 18)
    generated_password = str().join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=password_length))
    return generated_password


def generate_email() -> str:
    generated_email = str().join(random.choices(string.ascii_lowercase, k=10)) + '@gmail.com'
    return generated_email


def windscribe_connect(location: str):
    os.system(r'""C:\Program Files (x86)\Windscribe\windscribe-cli.exe" connect "' + location + r'"')



