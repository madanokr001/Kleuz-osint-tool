import requests
import os

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

def ip_information():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.LIGHT_MAGENTA + """
            ██▓ ██▓███      ██▓ ███▄    █   █████▒▒█████  
            ▓██▒▓██░  ██▒   ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
            ▒██▒▓██░ ██▓▒   ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
            ░██░▒██▄█▓▒ ▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
            ░██░▒██▒ ░  ░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
            ░▓  ▒▓▒░ ░  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
            ▒ ░░▒ ░         ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
            ▒ ░░░           ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
            ░               ░           ░            ░ ░      
            """+ TextColors.RESET)
    
    ip = input(TextColors.MAGENTA + "IP > "+ TextColors.RESET)
    api(ip)

def api(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    
    if response.status_code == 200:
        data = response.json()
        
        latitude = data.get('lat', 'N/A')
        longitude = data.get('lon', 'N/A')

        output = {
            "[+] IP": data.get('query', 'N/A'), 
            "[+] continent_code": data.get('continent', 'N/A'),
            "[+] continent_name": data.get('continent', 'N/A'),
            "[+] country_code": data.get('countryCode', 'N/A'),
            "[+] country_name": data.get('country', 'N/A'),
            "[*] region_code": data.get('region', 'N/A'),
            "[*] region_name": data.get('regionName', 'N/A'),
            "[*] city": data.get('city', 'N/A'),
            "[*] zip": data.get('zip', 'N/A'),
            "[*] latitude": latitude,
            "[*] longitude": longitude,
            "[*] ISP": data.get('isp', 'N/A'),
            "[*] timezone": data.get('timezone', 'N/A'),
            "[*] country capital": data.get('capital', 'N/A'),  
            "[*] currency": data.get('currency', 'N/A'),  
            "[*] language": data.get('language', 'N/A'),  
            "[*] status": data.get('status', 'N/A'),
            "[*] Map": f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"  
        }

        print(TextColors.LIGHT_MAGENTA +"╔════════════════════════════════════════════════════════════════════╗")
        print("║                 https://discord.gg/Aahv5HTTba                      ║")
        print("║════════════════════════════════════════════════════════════════════║")
        for key, value in output.items():                                          
            print(f"║ {key:<30} : {value:<33} ║")
        print("║                                                                    ║")
        print("╚════════════════════════════════════════════════════════════════════╝")

        input()

if __name__ == "__main__":
    ip_information()




    


