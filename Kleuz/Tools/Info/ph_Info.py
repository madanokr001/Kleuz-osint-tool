import os
import phonenumbers
from phonenumbers import geocoder, carrier

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

def number_information():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.LIGHT_MAGENTA + """
██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████     ██▓ ███▄    █   █████▒▒█████  
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░    ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░       ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
        ░  ░  ░    ░ ░           ░    ░  ░    ░           ░            ░ ░     
            """ + TextColors.RESET)

    number = input(TextColors.MAGENTA + "Number > " + TextColors.RESET)
    number_info = phonenumbers.parse(number)

    output = {
        "Valid": phonenumbers.is_valid_number(number_info),
        "Possible": phonenumbers.is_possible_number(number_info),
        "Number ": phonenumbers.format_number(number_info, phonenumbers.PhoneNumberFormat.E164),
        "Location": geocoder.description_for_number(number_info, "en"),
        "Carrier": carrier.name_for_number(number_info, "en") if carrier.name_for_number(number_info, "en") else 'Unknown',
        "Country Code": number_info.country_code,
        "Region Code": geocoder.region_code_for_number(number_info) if geocoder.region_code_for_number(number_info) else 'Unknown',
        "Country Name": geocoder.country_name_for_number(number_info, 'en') if geocoder.country_name_for_number(number_info, 'en') else 'Unknown'
    }

    print(TextColors.LIGHT_MAGENTA + "╔════════════════════════════════════════════════════════════════════╗")
    print("║                 https://discord.gg/Aahv5HTTba                      ║")
    print("║════════════════════════════════════════════════════════════════════║")
    for key, value in output.items():
        print(f"║ {key:<30} : {value:<33} ║")
    print("║                                                                    ║")
    print("╚════════════════════════════════════════════════════════════════════╝")

    input()

if __name__ == "__main__":
    number_information()





