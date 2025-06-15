#!/bin/python
from colorama import Fore
import os, json, requests

LOGIN_FILE = os.path.expanduser("~/.faang_logdetails.json") #os.path.join(os.path.dirname(os.path.abspath(__file__)), '.log') 

def check_login_file():
    try:
        with open(LOGIN_FILE, "r") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return None
    
wrap = 60

def desc():
    help_desc = "The features within this menu offer a range of powerful and diverse DDoS methods, designed to test and identify vulnerabilities and resilience of networks and servers. This menu encompasses attacks on both layer 4 and layer 7, including various attack types such as UDP, TCP, HTTP, and more. These attack methods enable users to simulate real-world scenarios, providing deeper insights into the defense capabilities of their systems against such attacks. Ranging from request-based attacks to protocol-based ones, this menu covers a broad spectrum of options to identify and mitigate DDoS risks effectively."
    return help_desc

def menus():
    FIREBASE_URL = f"https://direct-login-firebase-default-rtdb.asia-southeast1.firebasedatabase.app/menu.json?auth={check_login_file().get('db_token')}"

    try:
        response = requests.get(FIREBASE_URL)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                return data
            else:
                print("Data menu bukan list:", data)
        else:
            print("Gagal ambil data:", response.status_code)
    except Exception as e:
        print("Error:", e)
    
    return []  # fallback kalau gagal

def word_wrapper(text, line_length):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if len(current_line) + 1 + len(word) <= line_length:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return "\n".join(lines)

def logos():
    logo = f"""
{Fore.MAGENTA} █████▒▄▄▄          ▄▄▄       ███▄    █   ▄████ 
▓██   ▒▒████▄       ▒████▄     ██ ▀█   █  ██▒ ▀█▒
▒████ ░▒██  ▀█▄     ▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░
{Fore.RESET}░▓█▒  ░░██▄▄▄▄██    ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓
░▒█░    ▓█   ▓██▒    ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒
 ▒ ░    ▒▒   ▓▒█░    ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ 
 ░       ▒   ▒▒ ░     ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░ ░     ░   ▒        ░   ▒      ░   ░ ░ ░ ░   ░ 
             ░  ░         ░  ░         ░       ░ 
                                                 
{word_wrapper(f"THE OWNER OF THESE TOOLS (Dx4) WILL NOT BE RESPONSIBLE FOR ANY DAMAGE CAUSED BY THE USER OWN THEREFORE, USE THESE TOOLS ONLY TO TEST YOUR OWN SITE FOR {Fore.GREEN}VULNERABILITIES {Fore.RESET}ATTACKING SITES OWNED BY OTHERS, {Fore.YELLOW}FAANG SHOULD NOT BE USED FOR ILLEGAL ACTIVITIES{Fore.RESET}, BY USING THIS SOFTWARE, {Fore.RED}YOU MUST AGREE TO BE FULLY RESPONSIBLE FOR DAMAGE CAUSED BY FAANG IN ANY WAY TO YOUR OWN{Fore.RESET}. THE CREATORS DO NOT WANT PEOPLE TO USE FAANG IF THEY HAVE NO EXPERIENCE WITH ATTACKS INCLUDING. ANY ATTACK WILL CAUSE TEMPORARY DAMAGE, BUT {Fore.YELLOW}LONG TERM DAMAGE{Fore.RESET} IS POSSIBLE. FAANG SHOULD NOT ADVISE PEOPLE TO DO {Fore.RED}ILLEGAL ACTIVITIES{Fore.RESET}.", wrap)}
"""
    return logo