import os
import sys
from Tools.Info.ip_Info import *
from Tools.Lockup.dnslock import *
from Tools.Lockup.dnsreverse import *
from Tools.Info.ph_Info import *
from Tools.Web.whois import *
from Tools.Finder.email import *
from Tools.Finder.user import *

class TextColors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    PURPLE = '\033[35m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BOLD = "\033[01;01m"
    LIGHT_MAGENTA = '\033[1;35m'
    DARK_RED = "\033[38;5;124m"
    CRIMSON = "\033[38;5;196m"
    TOMATO = "\033[38;5;202m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m" 

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.LIGHT_MAGENTA + """

                ██ ▄█▀ ██▓    ▓█████  █    ██ ▒███████▒
                ██▄█▒ ▓██▒    ▓█   ▀  ██  ▓██▒▒ ▒ ▒ ▄▀░
                ▓███▄░ ▒██░    ▒███   ▓██  ▒██░░ ▒ ▄▀▒░ 
                ▓██ █▄ ▒██░    ▒▓█  ▄ ▓▓█  ░██░  ▄▀▒   ░
                ▒██▒ █▄░██████▒░▒████▒▒▒█████▓ ▒███████▒ 
                ▒ ▒▒ ▓▒░ ▒░▓  ░░░ ▒░ ░░▒▓▒ ▒ ▒ ░▒▒ ▓░▒░▒
                ░ ░▒ ▒░░ ░ ▒  ░ ░ ░  ░░░▒░ ░ ░ ░░▒ ▒ ░ ▒
                ░ ░░ ░   ░ ░      ░    ░░░ ░ ░ ░ ░ ░ ░ ░
                ░  ░       ░  ░   ░  ░   ░       ░ ░    
                                            ░        건우Sec v1.0
╔════════════════════════════════════════════════════════════════════╗
║                   Link : https://doxwebd.serveo.net                ║
║════════════════════════════════════════════════════════════════════║
║                                                                    ║
║             [01] IP INFORMATION      [06] USER FINDER              ║
║             [02] NUMBER INFORMATION  [07] EMAIL FINDER             ║
║             [03] DNS Lockup          [08] EXIT                     ║
║             [04] DNS Reverse                                       ║
║             [05] WHOIS                                             ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝


    """ + TextColors.RESET)

def main():
    while True:
        logo()
        select = input(TextColors.MAGENTA + "> " + TextColors.RESET)

        if select == "1" or select.lower() == "1":
            ip_information()

        elif select == "2" or select.lower() == "2":
            number_information()
            
        elif select == "3" or select.lower() == "3":
            dnslockup()

        elif select == "4" or select.lower() == "4":
            dnsreverse()
            
        elif select == "5" or select.lower() == "5":
            whois_main()

        elif select == "6" or select.lower() == "6":
            userfinder_main()

        elif select == "7" or select.lower() == "6":
            emailfinder_main()

        
            

            
        elif select == "8" or select.lower() == "8":
            sys.exit()
    
             


if __name__ == "__main__":
    main()
