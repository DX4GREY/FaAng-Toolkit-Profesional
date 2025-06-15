#!/bin/python

# Copyright (c) Dx4 2023-2025

# The FaAng Toolkit programmed and developed by Dx4
# The FaAng Toolkit was published by Dx4 under MIT Licence

# Legal atau tidaknya tergantung kalian yang menggunakan

from lib.app import main
import sys, platform, os
from colorama import Fore
import threading, time

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(f"\n {Fore.RED}[*]{Fore.RESET} Killing all processes...")
		time.sleep(1)
		print(f" {Fore.MAGENTA}[*]{Fore.RESET} Have a nice day Hackers!")
		time.sleep(3)
		os.system('cls' if os.name == 'nt' else 'clear')
		os._exit(1)