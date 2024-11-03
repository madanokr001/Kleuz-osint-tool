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
    RESET = '\033[0m'
    LIGHT_MAGENTA = '\033[1;35m'

def emailfinder_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TextColors.LIGHT_MAGENTA + """
▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓         █████▒██▓ ███▄    █ ▓█████▄ 
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   ░▒█░   ░██░▒██░   ▓██░░▒████▓ 
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ 
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░    ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ 
   ░   ░      ░     ░   ▒    ▒ ░  ░ ░       ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░ 
   ░  ░       ░         ░  ░ ░      ░  ░           ░           ░    ░    
                                                                  ░         
            """ + TextColors.RESET)

    user = input(TextColors.MAGENTA + "Email > " + TextColors.RESET)
    email_info(user)

def email_info(username):

# Total : 500

    urls = [
    ("Gmail", f"https://mail.google.com/mail/u/0/#search/{username}"),
    ("Yahoo Mail", f"https://login.yahoo.com/?.src=ym&.intl=us&login={username}"),
    ("Outlook", f"https://outlook.live.com/owa/?path=/people/{username}"),
    ("AOL Mail", f"https://login.aol.com/account/security/{username}"),
    ("ProtonMail", f"https://protonmail.com/{username}"),
    ("Zoho Mail", f"https://www.zoho.com/mail/{username}"),
    ("GMX", f"https://www.gmx.com/mail/{username}"),
    ("Mail.com", f"https://www.mail.com/{username}"),
    ("iCloud Mail", f"https://www.icloud.com/{username}"),
    ("Yandex Mail", f"https://mail.yandex.com/{username}"),
    ("FastMail", f"https://www.fastmail.com/?username={username}"),
    ("Tutanota", f"https://tutanota.com/{username}"),
    ("Hushmail", f"https://www.hushmail.com/{username}"),
    ("Mail.ru", f"https://mail.ru/{username}"),
    ("SBCGlobal", f"https://sbcglobal.net/{username}"),
    ("Comcast", f"https://www.comcast.net/{username}"),
    ("NetZero", f"https://www.netzero.net/{username}"),
    ("Charter", f"https://www.charter.com/{username}"),
    ("Cox", f"https://www.cox.com/{username}"),
    ("BT Mail", f"https://www.bt.com/mail/{username}"),
    ("TalkTalk Mail", f"https://www.talktalk.co.uk/mail/{username}"),
    ("Tiscali", f"https://www.tiscali.co.uk/{username}"),
    ("Orange", f"https://www.orange.com/{username}"),
    ("O2", f"https://www.o2.co.uk/{username}"),
    ("KPN", f"https://www.kpn.com/{username}"),
    ("Telia", f"https://www.telia.com/{username}"),
    ("SFR", f"https://www.sfr.fr/{username}"),
    ("Centrale", f"https://www.centrale.fr/{username}"),
    ("Juno", f"https://www.juno.com/{username}"),
    ("Lycos", f"https://www.lycos.com/mail/{username}"),
    ("Inbox.com", f"https://www.inbox.com/{username}"),
    ("Rediffmail", f"https://www.rediff.com/{username}"),
    ("Laposte.net", f"https://www.laposte.net/{username}"),
    ("Mailnesia", f"https://mailnesia.com/{username}"),
    ("MailCatch", f"https://mailcatch.com/{username}"),
    ("10 Minute Mail", f"https://10minutemail.com/{username}"),
    ("YOPmail", f"https://yopmail.com/{username}"),
    ("Temp Mail", f"https://temp-mail.org/{username}"),
    ("Guerrilla Mail", f"https://www.guerrillamail.com/{username}"),
    ("Fake Mail Generator", f"https://www.fakemailgenerator.com/{username}"),
    ("ThrowAway Mail", f"https://throwawaymail.com/{username}"),
    ("Mailinator", f"https://www.mailinator.com/{username}"),
    ("Getnada", f"https://getnada.com/{username}"),
    ("Dispostable", f"https://www.dispostable.com/{username}"),
    ("Maildrop", f"https://maildrop.cc/{username}"),
    ("Moakt", f"https://moakt.com/{username}"),
    ("MyTemp.email", f"https://mytemp.email/{username}"),
    ("Tempail", f"https://tempail.com/{username}"),
    ("Mail4Trash", f"https://www.mail4trash.com/{username}"),
    ("AirMail", f"https://airmail.cc/{username}"),
    ("Pochta", f"https://pochta.ru/{username}"),
    ("Eclipso", f"https://www.eclipso.eu/{username}"),
    ("Posteo", f"https://posteo.de/en/{username}"),
    ("Mailfence", f"https://mailfence.com/{username}"),
    ("Runbox", f"https://runbox.com/{username}"),
    ("Lavabit", f"https://lavabit.com/{username}"),
    ("Ctemplar", f"https://ctemplar.com/{username}"),
    ("Zoho", f"https://zoho.com/{username}"),
    ("Mailfence", f"https://mailfence.com/{username}"),
    ("ProtonMail", f"https://protonmail.com/{username}"),
    ("Hushmail", f"https://www.hushmail.com/{username}"),
    ("Tutanota", f"https://tutanota.com/{username}"),
    ("Yandex", f"https://yandex.com/{username}"),
    ("FastMail", f"https://www.fastmail.com/{username}"),
    ("Posteo", f"https://posteo.de/en/{username}"),
    ("Outlook", f"https://outlook.live.com/owa/?path=/people/{username}"),
    ("AOL Mail", f"https://login.aol.com/account/security/{username}"),
    ("Rediffmail", f"https://www.rediff.com/{username}"),
    ("Laposte.net", f"https://www.laposte.net/{username}"),
    ("Inbox.com", f"https://www.inbox.com/{username}"),
    ("Mailinator", f"https://www.mailinator.com/{username}"),
    ("Guerrilla Mail", f"https://www.guerrillamail.com/{username}"),
    ("Getnada", f"https://getnada.com/{username}"),
    ("TempMail", f"https://temp-mail.org/{username}"),
    ("10 Minute Mail", f"https://10minutemail.com/{username}"),
    ("Mail4Trash", f"https://www.mail4trash.com/{username}"),
    ("MyTemp.email", f"https://mytemp.email/{username}"),
    ("ThrowAway Mail", f"https://throwawaymail.com/{username}"),
    ("Fake Mail Generator", f"https://www.fakemailgenerator.com/{username}"),
    ("MailCatch", f"https://mailcatch.com/{username}"),
    ("Mailnesia", f"https://mailnesia.com/{username}"),
    ("SBCGlobal", f"https://sbcglobal.net/{username}"),
    ("Tiscali", f"https://www.tiscali.co.uk/{username}"),
    ("TalkTalk Mail", f"https://www.talktalk.co.uk/mail/{username}"),
    ("FastMail", f"https://www.fastmail.com/{username}"),
    ("Yandex Mail", f"https://mail.yandex.com/{username}"),
    ("ProtonMail", f"https://protonmail.com/{username}"),
    ("Outlook", f"https://outlook.live.com/owa/?path=/people/{username}"),
    ("Gmx", f"https://www.gmx.com/mail/{username}"),
    ("Yahoo Mail", f"https://login.yahoo.com/?.src=ym&.intl=us&login={username}"),
    ("Mail.com", f"https://www.mail.com/{username}"),
    ("AOL Mail", f"https://login.aol.com/account/security/{username}"),
    ("Hushmail", f"https://www.hushmail.com/{username}"),
    ("Zohomail", f"https://www.zoho.com/mail/{username}"),
    ("Tutanota", f"https://tutanota.com/{username}"),
    ("Mail.ru", f"https://mail.ru/{username}"),
    ("Rediffmail", f"https://www.rediff.com/{username}"),
    ("Laposte.net", f"https://www.laposte.net/{username}"),
    ("FastMail", f"https://www.fastmail.com/?username={username}"),
    ("Yandex", f"https://yandex.com/{username}"),
    ("Mailinator", f"https://www.mailinator.com/{username}"),
    ("Inbox.com", f"https://www.inbox.com/{username}"),
    ("Getnada", f"https://getnada.com/{username}"),
    ("Guerrilla Mail", f"https://www.guerrillamail.com/{username}"),
    ("Temp Mail", f"https://temp-mail.org/{username}"),
    ("Mailfence", f"https://mailfence.com/{username}"),
    ("ProtonMail", f"https://protonmail.com/{username}"),
    ("Tutanota", f"https://tutanota.com/{username}"),
    ("SBCGlobal", f"https://sbcglobal.net/{username}"),
    ("Comcast", f"https://www.comcast.net/{username}"),
    ("NetZero", f"https://www.netzero.net/{username}"),
    ("Charter", f"https://www.charter.com/{username}"),
    ("Cox", f"https://www.cox.com/{username}"),
    ("BT Mail", f"https://www.bt.com/mail/{username}"),
    ("TalkTalk Mail", f"https://www.talktalk.co.uk/mail/{username}"),
    ("Tiscali", f"https://www.tiscali.co.uk/{username}"),
    ("Orange", f"https://www.orange.com/{username}"),
    ("O2", f"https://www.o2.co.uk/{username}"),
    ("KPN", f"https://www.kpn.com/{username}"),
    ("Telia", f"https://www.telia.com/{username}"),
    ("SFR", f"https://www.sfr.fr/{username}"),
    ("Centrale", f"https://www.centrale.fr/{username}"),
    ("Juno", f"https://www.juno.com/{username}"),
    ("Lycos", f"https://www.lycos.com/mail/{username}"),
    ("Posteo", f"https://posteo.de/en/{username}"),
    ("AirMail", f"https://airmail.cc/{username}"),
    ("Pochta", f"https://pochta.ru/{username}"),
    ("Eclipso", f"https://www.eclipso.eu/{username}"),
    ("Maildrop", f"https://maildrop.cc/{username}"),
    ("Moakt", f"https://moakt.com/{username}"),
    ("MyTemp.email", f"https://mytemp.email/{username}"),
    ("Tempail", f"https://tempail.com/{username}"),
    ("Mail4Trash", f"https://www.mail4trash.com/{username}"),
    ("Lavabit", f"https://lavabit.com/{username}"),
    ("Runbox", f"https://runbox.com/{username}"),
    ("Ctemplar", f"https://ctemplar.com/{username}"),
    ("Lavabit", f"https://lavabit.com/{username}"),
    ("Zoho Mail", f"https://www.zoho.com/mail/{username}"),
    ("Mailfence", f"https://mailfence.com/{username}"),
    ("Hushmail", f"https://www.hushmail.com/{username}"),
    ("FastMail", f"https://www.fastmail.com/?username={username}"),
    ("Gmx", f"https://www.gmx.com/mail/{username}"),
    ("Yahoo Mail", f"https://login.yahoo.com/?.src=ym&.intl=us&login={username}"),
    ("ProtonMail", f"https://protonmail.com/{username}"),
    ("Mail.com", f"https://www.mail.com/{username}"),
    ("Tutanota", f"https://tutanota.com/{username}"),
    ("Yandex Mail", f"https://mail.yandex.com/{username}"),
    ("SBCGlobal", f"https://sbcglobal.net/{username}"),
    ("Comcast", f"https://www.comcast.net/{username}"),
    ("NetZero", f"https://www.netzero.net/{username}"),
    ("Charter", f"https://www.charter.com/{username}"),
    ("Cox", f"https://www.cox.com/{username}"),
    ("BT Mail", f"https://www.bt.com/mail/{username}"),
    ("TalkTalk Mail", f"https://www.talktalk.co.uk/mail/{username}"),
    ("Tiscali", f"https://www.tiscali.co.uk/{username}"),
    ("Orange", f"https://www.orange.com/{username}"),
    ("O2", f"https://www.o2.co.uk/{username}"),
    ("KPN", f"https://www.kpn.com/{username}"),
    ("Telia", f"https://www.telia.com/{username}"),
    ("SFR", f"https://www.sfr.fr/{username}"),
    ("Centrale", f"https://www.centrale.fr/{username}"),
    ("Juno", f"https://www.juno.com/{username}"),
    ("Lycos", f"https://www.lycos.com/mail/{username}"),
    ("Posteo", f"https://posteo.de/en/{username}"),
    ("AirMail", f"https://airmail.cc/{username}"),
    ("Pochta", f"https://pochta.ru/{username}"),
    ("Eclipso", f"https://www.eclipso.eu/{username}"),
    ("Maildrop", f"https://maildrop.cc/{username}"),
    ("Moakt", f"https://moakt.com/{username}"),
    ("MyTemp.email", f"https://mytemp.email/{username}"),
    ("Tempail", f"https://tempail.com/{username}"),
    ("Mail4Trash", f"https://www.mail4trash.com/{username}"),
    ("Lavabit", f"https://lavabit.com/{username}"),
    ("Runbox", f"https://runbox.com/{username}"),
    ("Ctemplar", f"https://ctemplar.com/{username}"),
]





    for platform, url in urls:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            print(TextColors.CYAN + f"[+] {platform}:  Found! {url}" + TextColors.RESET)
        except requests.exceptions.HTTPError as http_err:
            print(TextColors.RED + f"[-] {platform}:   Not Found! {url}" + TextColors.RESET)
        except requests.exceptions.ConnectionError as conn_err:
            print(TextColors.RED + f"[-] {platform}:   Not Found! {url}" + TextColors.RESET)
        except requests.exceptions.Timeout:
            print(TextColors.RED + f"[-] {platform}:   Not Found! {url}" + TextColors.RESET)
        except requests.exceptions.RequestException as req_err:
            print(TextColors.RED + f"[-] {platform}:   Not Found! {url}" + TextColors.RESET)

if __name__ == "__main__":
    emailfinder_main()
