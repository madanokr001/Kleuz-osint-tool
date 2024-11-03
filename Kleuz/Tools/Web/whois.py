import os
import whois

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

def whois_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.LIGHT_MAGENTA + """
         █     █░ ██░ ██  ▒█████   ██▓  ██████ 
        ▓█░ █ ░█░▓██░ ██▒▒██▒  ██▒▓██▒▒██    ▒ 
        ▒█░ █ ░█ ▒██▀▀██░▒██░  ██▒▒██▒░ ▓██▄   
        ░█░ █ ░█ ░▓█ ░██ ▒██   ██░░██░  ▒   ██▒
        ░░██▒██▓ ░▓█▒░██▓░ ████▓▒░░██░▒██████▒▒
        ░ ▓░▒ ▒   ▒ ░░▒░▒░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░
        ▒ ░ ░   ▒ ░▒░ ░  ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░
        ░   ░   ░  ░░ ░░ ░ ░ ▒   ▒ ░░  ░  ░  
            ░     ░  ░  ░    ░ ░   ░        ░      
            """ + TextColors.RESET)
    
    url = input(TextColors.MAGENTA + "Url > " + TextColors.RESET)

    w = whois.whois(url)

    output = {
    "[+] Domain Name": f"{w.domain_name}" if w.domain_name else "[-] N/A",
    "[+] Registrar": f"{w.registrar}" if w.registrar else "[-] N/A",
    "[+] Creation Date": f"{w.creation_date}" if w.creation_date else "[-] N/A",
    "[+] Expiration Date": f"{w.expiration_date}" if w.expiration_date else "[-] N/A",
    "[+] Updated Date": f"{w.updated_date}" if w.updated_date else "[-] N/A",
    "[*] Name Servers": f"{', '.join(w.name_servers) if w.name_servers else 'N/A'}",
    "[*] Status": f"{', '.join(w.status) if w.status else 'N/A'}",
    "[*] DNSSEC": f"{w.dnssec}" if w.dnssec else "[-] N/A",
}

    print(TextColors.LIGHT_MAGENTA + "╔════════════════════════════════════════════════════════════════════╗")
    print("║                https://discord.gg/Aahv5HTTba                       ║")
    print("║════════════════════════════════════════════════════════════════════║")
    for key, value in output.items():                                          
        print(f"║ {key:<30} : {value:<33} ║")
    print("║                                                                    ║")
    print("╚════════════════════════════════════════════════════════════════════╝")

    input()

if __name__ == "__main__":
    whois_main()






