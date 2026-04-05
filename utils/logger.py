from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class Logger:

    @staticmethod
    def info(message):
        print(f"{Fore.CYAN}[{datetime.now()}] [INFO] {message}{Style.RESET_ALL}")

    @staticmethod
    def success(message):
        print(f"{Fore.GREEN}[{datetime.now()}] [SUCCESS] {message}{Style.RESET_ALL}")

    @staticmethod
    def warning(message):
        print(f"{Fore.YELLOW}[{datetime.now()}] [WARNING] {message}{Style.RESET_ALL}")

    @staticmethod
    def error(message):
        print(f"{Fore.RED}[{datetime.now()}] [ERROR] {message}{Style.RESET_ALL}")