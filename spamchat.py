#!/usr/bin/env python3
"""
WhatsApp Spam Tool - Python Wrapper
Memanggil script Node.js untuk spam pairing code
Requirement: Node.js terinstal
"""

import subprocess
import sys
import os
import platform

# Warna untuk terminal (opsional)
try:
    from colorama import init, Fore, Style
    init()
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    CYAN = Fore.CYAN
    RESET = Style.RESET_ALL
except ImportError:
    # Fallback jika colorama tidak terinstal
    RED = GREEN = YELLOW = CYAN = RESET = ''

def check_node():
    """Periksa apakah Node.js terinstal"""
    try:
        result = subprocess.run(
            ["node", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"{GREEN}✓ Node.js terdeteksi: {result.stdout.strip()}{RESET}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"{RED}✗ Node.js tidak ditemukan!{RESET}")
        return False

def main():
    print(f"""{CYAN}
╔═══════════════════════════════════════╗
║    WhatsApp Spammer - Python Launcher ║
║        (Memanggil Node.js)            ║
║         Created by ZinXploit          ║
║         Lulzec Indonesia 🇮🇩           ║
╚═══════════════════════════════════════╝{RESET}
    """)
    
    # 1. Cek Node.js
    if not check_node():
        print(f"\n{YELLOW}📥 Silakan install Node.js dari: https://nodejs.org/{RESET}")
        input("Tekan Enter untuk keluar...")
        return
    
    # 2. Cek keberadaan script Node.js
    node_script = "wa-spam-free.js"
    if not os.path.exists(node_script):
        print(f"{RED}✗ File '{node_script}' tidak ditemukan!{RESET}")
        print(f"{YELLOW}Pastikan file tersebut ada di folder yang sama dengan script ini.{RESET}")
        input("Tekan Enter untuk keluar...")
        return
    
    # 3. Informasi
    print(f"{GREEN}✓ Script Node.js ditemukan: {node_script}{RESET}")
    print(f"{YELLOW}⚠️  PERINGATAN: Penggunaan tools ini dapat melanggar ketentuan WhatsApp.{RESET}")
    print(f"{YELLOW}   Risiko: nomor target bisa crash, IP Anda diblokir.{RESET}\n")
    
    # 4. Jalankan script Node.js
    try:
        print(f"{CYAN}🚀 Menjalankan script Node.js...{RESET}\n")
        # Gunakan shell=False untuk keamanan
        subprocess.run(["node", node_script])
    except KeyboardInterrupt:
        print(f"\n{RED}⛔ Dihentikan oleh user.{RESET}")
    except Exception as e:
        print(f"{RED}❗ Error: {e}{RESET}")
    
    input("\nTekan Enter untuk keluar...")

if __name__ == "__main__":
    main()
