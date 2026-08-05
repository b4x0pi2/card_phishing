<div align="center">

# 💳 Card Phishing  
### _Advanced Cybersecurity Awareness & Educational Tool_

<br>

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge&logo=mit)
![Termux](https://img.shields.io/badge/Termux-2026-black?style=for-the-badge&logo=android)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-blue?style=for-the-badge)

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-ACTIVE-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/EDUCATIONAL-ONLY-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Version-3.0-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Stars-%E2%AD%90%20Coming%20Soon-yellow?style=flat-square" />
</p>

<br>

</div>

---

## 📖 **Table of Contents**
- [🚀 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [🛠️ Usage](#️-usage)
- [🧠 How It Works](#-how-it-works)
- [📸 Screenshots](#-screenshots)
- [🎥 Video Tutorial](#-video-tutorial)
- [❓ FAQ](#-faq)
- [⚠️ Disclaimer](#️-disclaimer)
- [📌 Connect](#-connect)
- [📝 License](#-license)

---

## 🚀 **Overview**

**Card Phishing Simulator** is a high-quality, realistic simulation of a modern payment gateway — built using **Python** & **Flask**.

> 🎯 **Purpose:** Strictly educational. To show how phishing websites look, behave, and steal card details — so users can recognize and avoid them in real life.

🔒 **For:**  
✅ Cybersecurity Students  
✅ Ethical Hackers  
✅ Security Researchers  
✅ Penetration Testers  
✅ Teachers & Educators

---

## ✨ **Key Features**

| Feature | Description |
|---------|-------------|
| 🎨 **Premium Payment UI** | Apple-level glassmorphism design |
| 💳 **Live Card Capture** | Captures card number, CVV, expiry, name, phone, email |
| 📡 **Real-Time Monitor** | AndroRAT-style live terminal dashboard |
| 📁 **JSON Storage** | All data saved in `data/stolen_cards.json` |
| 🌐 **Ngrok Support** | Expose server globally with one command |
| 🎭 **Bank Redirect** | After submission, redirects to SBI (realism) |
| 🖥️ **Premium Banner** | Hollywood-style terminal header |
| 📱 **Responsive Design** | Mobile-friendly, works on all devices |
| ⚡ **Lightweight** | Minimal dependencies, runs on low-end devices |

---

## 📁 Project Structure
card_phishing/
├── data/
│   └── stolen_cards.json
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── server.py
├── monitor.py
├── requirements.txt
└── README.md


---

```mermaid
graph TD
    A[Server Starts] --> B[Hosts Payment UI]
    B --> C[User Visits Page]
    C --> D[User Enters Card Details]
    D --> E[Data Saved to JSON]
    E --> F[Monitor Alerts in Real-Time]
    F --> G[User Redirected to Real Bank Site]


