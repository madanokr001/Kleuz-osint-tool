import os
import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim

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

    location = geocoder.description_for_number(number_info, "en")
    region_code = geocoder.region_code_for_number(number_info)

    latitude, longitude = phone_location(location)

    output = {
        
        "Valid": phonenumbers.is_valid_number(number_info),
        "Possible": phonenumbers.is_possible_number(number_info),
        "Number": phonenumbers.format_number(number_info, phonenumbers.PhoneNumberFormat.E164),
        "Location": location,
        "Carrier": carrier.name_for_number(number_info, "en") if carrier.name_for_number(number_info, "en") else 'Unknown',
        "Country Code": number_info.country_code,
        "Region Code": region_code if region_code else 'Unknown',
        "Country Name": geocoder.country_name_for_number(number_info, 'en') if geocoder.country_name_for_number(number_info, 'en') else 'Unknown',
        "Latitude": latitude,
        "Longitude": longitude,
        "Phone Type": phone_type(number_info),
        "Is Active": "Yes" if phonenumbers.is_valid_number(number_info) else "No",
        "Map": f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}",
    }

    print(TextColors.LIGHT_MAGENTA + "╔════════════════════════════════════════════════════════════════════╗")
    print("║                 https://discord.gg/Aahv5HTTba                      ║")
    print("║════════════════════════════════════════════════════════════════════║")
    for key, value in output.items():
        print(f"║ {key:<30} : {value:<33} ║")
    print("║                                                                    ║")
    print("╚════════════════════════════════════════════════════════════════════╝")

    input()

def phone_location(location):
    geolocator = Nominatim(user_agent="my_geocoder_app") 
    
    location_info = geolocator.geocode(location)
        
    if location_info:
        return location_info.latitude, location_info.longitude

    return "Unknown", "Unknown"


def phone_type(number_info):
    phone_type = phonenumbers.number_type(number_info)
    if phone_type == phonenumbers.PhoneNumberType.MOBILE:
        return "Mobile"
    elif phone_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        return "Landline"
    elif phone_type == phonenumbers.PhoneNumberType.FAX_PHONE:
        return "Fax"
    elif phone_type == phonenumbers.PhoneNumberType.PAGER:
        return "Pager"
    elif phone_type == phonenumbers.PhoneNumberType.TOLL_FREE:
        return "Toll-Free"
    else:
        return "Unknown"

if __name__ == "__main__":
    number_information()





