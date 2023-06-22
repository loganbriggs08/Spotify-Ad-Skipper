from colorama import *

init(convert=True)

class Logging:
    def error(message: str):
        print(f"{Fore.RED}[ERROR]{Fore.WHITE} {message}")
        
    def success(message: str):
        print(f"{Fore.GREEN}[SUCCESS]{Fore.WHITE} {message}")
