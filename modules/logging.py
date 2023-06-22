from colorama import *

init(convert=True)

class Logging:
    def error(message: str):
        print(f"{Fore.RED}[ERROR]{Fore.WHITE} {message}")