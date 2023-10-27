#!/bin/python

# Copyright (c) Dx4 2023

# The FaAng Toolkit programmed and developed by Dx4
# The FaAng Toolkit was published by Dx4 under MIT Licence

# Legal atau tidaknya tergantung kalian yang menggunakan

from lib.app import main
import sys
from colorama import Fore

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(f"{Fore.BLUE}[0]{Fore.RESET} Exiting...") 
		sys.exit(1)