import socket
import os
import sys

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

def dnsreverse():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.LIGHT_MAGENTA + """
▓█████▄  ███▄    █   ██████  ██▓     ▒█████   ▄████▄   ██ ▄█▀ █    ██  ██▓███  
▒██▀ ██▌ ██ ▀█   █ ▒██    ▒ ▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒  ██  ▓██▒▓██░  ██▒
░██   █▌▓██  ▀█ ██▒░ ▓██▄   ▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ ▓██  ▒██░▓██░ ██▓▒
░▓█▄   ▌▓██▒  ▐▌██▒  ▒   ██▒▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░▒████▓ ▒██░   ▓██░▒██████▒▒░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
▒▒▓  ▒ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░ ▒  ▒ ░ ░░   ░ ▒░░ ░▒  ░ ░░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
░ ░  ░    ░   ░ ░ ░  ░  ░    ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░  ░░░ ░ ░ ░░       
░             ░       ░      ░  ░    ░ ░  ░ ░      ░  ░      ░              
░                                           ░             
                    
            """+ TextColors.RESET)
    
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    ip = input(TextColors.MAGENTA + "IP > "+ TextColors.RESET)

    addr = socket.gethostbyaddr(ip)

    print(TextColors.LIGHT_MAGENTA + f"""
    ══════════════════════════════════════════════════

          IP Address : {ip}

          Domain server : {addr}
                
    ══════════════════════════════════════════════════"""+ TextColors.RESET)

    input()


if __name__ == "__main__":
    dnsreverse()