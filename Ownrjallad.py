# Logo
logo = """
\033[1;32m▗▖ ▗▄▖ ▗▖   ▗▖    ▗▄▖ ▗▄▄▄      
  \033[1;32m ▐▌▐▌ ▐▌▐▌   ▐▌   ▐▌ ▐▌▐▌  █     
 \033[1;32m  ▐▌▐▛▀▜▌▐▌   ▐▌   ▐▛▀▜▌▐▌  █     
\033[1;32m▗▄▄▞▘▐▌ ▐▌▐▙▄▄▖▐▙▄▄▖▐▌ ▐▌▐▙▄▄▀     

\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;32m[*] 𝐎𝐖𝐍𝐄𝐑      : \033[1;32m𝐉𝐀𝐋𝐋𝐀𝐃 𝐊𝐈𝐍𝐆
\033[1;32m[*] 𝐆𝐈𝐓𝐇𝐔𝐁     : \033[1;32m𝐉𝐀𝐋𝐋𝐀𝐃 𝐈𝐍𝐒𝐈𝐃𝐄
\033[1;32m[*] 𝐒𝐓𝐀𝐓𝐔𝐒     : \033[1;32m𝐏𝐑𝐄𝐌𝐈𝐔𝐌
\033[1;32m[*] 𝐓𝐄𝐀𝐌       : \033[1;32m𝐎𝐍𝐄 𝐌𝐀𝐍 𝐀𝐑𝐌𝐘
\033[1;32m[*] 𝐓𝐎𝐎𝐋       : \033[1;32m𝐌𝐔𝐋𝐓𝐈 𝐓𝐎𝐊𝐄𝐍 𝐂𝐎𝐍𝐕𝐎 𝐓𝐎𝐎𝐋
\033[36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
print(logo)

import os
import random
import time
import requests

# Facebook Graph API endpoint
thread_id = input("\033[1;32m3NT3R TH3 GR0UP + 1NB0X U1D: ")

url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

# Token file paths
token_file_paths = input("\033[1;32mEnter token file paths : ").split(',')

# Message file path
message_file_path = input("\033[1;32mEnter message file path: ")

# Haters name
haters_name = input("\033[1;32mEnter haters name: ")

# Delay between messages
delay_between_messages = int(input("\033[1;32mEnter delay between messages: "))

# Read tokens from files
access_tokens = []
token_names = []
for token_file_path in token_file_paths:
    with open(token_file_path.strip(), "r") as token_file:
        for i, token in enumerate(token_file.readlines()):
            access_tokens.append(token.strip())
            token_names.append(f"Token {i+1}")

# Read messages from file
messages = []
with open(message_file_path, "r") as message_file:
    messages = message_file.readlines()

def get_account_name(token):
    try:
        response = requests.get(f'https://graph.facebook.com/v15.0/me?access_token={token}')
        data = response.json()
        return data['name']
    except Exception as e:
        return "Unknown"

def send_message(token, message, thread_id, haters_name):
    try:
        message_url = f"{url}"
        message_params = {
            "access_token": token,
            "message": f"{haters_name} {message}"
        }
        message_response = requests.post(message_url, params=message_params)
        if message_response.status_code == 200:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
\033[1;32m
✪✭═══════•『 𝐉𝟒𝐋𝐋𝟒𝐃 𝐊𝐈𝟗𝐆 𝟎𝐍𝐅𝟏𝐑𝟑 』•═══════✭✪
""")
            account_name = get_account_name(token)           
            print(f"\033[1;32m[+] M9SS9G3 S3ND T0 S9B9 JUTT => Thread ID: {thread_id} => Token: {token_names[access_tokens.index(token)]} => Account Name: {account_name} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
        else:
            current_time = time.strftime("%H:%M:%S")
            print(f"""
 \033[1;32m 
✪✭═══════•『 𝐉𝟒𝐋𝐋𝟒𝐃 𝐊𝐈𝟗𝐆 𝟎𝐍𝐅𝟏𝐑𝟑 』•═══════✭✪
""")
            print(f"\033[1;32mM3SS4G3 F9IL3D H0 GYA HAI => Thread ID: {thread_id} =>Token: {token_names[access_tokens.index(token)]} => Haters Name: {haters_name} => Message: {message} => Time: {current_time}\033[0m")
    except Exception as e:
        print(str(e))

def process_messages_thread():
    try:
        while True:
            random_token = random.choice(access_tokens)
            random_message = random.choice(messages).strip()
            send_message(random_token, random_message, thread_id, haters_name)
            time.sleep(delay_between_messages)
    except Exception as e:
        print(str(e))

process_messages_thread()
