"""
==============================================================================
BOT AUTO CREATE GMAIL (TERMUX NATIVE ENGINE - TANPA KABEL)
==============================================================================
Dirancang khusus untuk berjalan di dalam Termux Android.
- Membuka Chrome Android secara otomatis lewat Android Intent.
- Berinteraksi dengan elemen layar HP (tap, ketik teks, back).
- Mengirimkan hasil & log error ke Telegram Admin (5993311226) & Client (392836663).
==============================================================================
"""

import os
import sys
import time
import json
import random
import urllib.request
import subprocess
from datetime import datetime

# ==============================================================================
# KONFIGURASI BOT & TELEGRAM
# ==============================================================================
CONFIG = {
    # Akun Induk Orang Tua (Parent Sign-In)
    "PARENT_EMAIL": "by.u001user@gmail.com",
    "PARENT_PASSWORD": "martabakmesir13",

    # Password Akun Jadi (Gmail Market)
    "MARKET_PASSWORD": "sgsg1122",

    # Tahun Dewasa setelah Back (2001 s/d 2008)
    "ADULT_YEAR": "2001",

    # Telegram Bot Token
    "TELEGRAM_BOT_TOKEN": "9196997158:AAF5OutT0JHy73no84X8mhzwbFrm0BeUIzU",

    # Dua Penerima Notifikasi (Admin & Client)
    "ADMIN_CHAT_ID": "5993311226",
    "CLIENT_CHAT_ID": "392836663",
}

FIRST_NAMES = ["nadia", "arib", "bintang", "dian", "fajar", "gilang", "haikal", "ihsan", "lutfi", "maulana", "rizki", "kurnia", "satria", "wahyu"]
LAST_NAMES = ["pratama", "utomo", "cahyo", "bagas", "dimas", "gunawan", "hubner", "kaila", "seika", "zahra", "anisa", "saputra"]

CURRENT_STEP = "Inisialisasi"

def log_step(step_name, desc=""):
    global CURRENT_STEP
    CURRENT_STEP = step_name
    print(f"\n>> [{step_name}] {desc}")

def send_telegram(message):
    """Kirim pesan Markdown ke Admin & Client"""
    token = CONFIG["TELEGRAM_BOT_TOKEN"]
    recipients = [CONFIG["ADMIN_CHAT_ID"], CONFIG["CLIENT_CHAT_ID"]]
    for cid in recipients:
        if not cid:
            continue
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = json.dumps({"chat_id": cid, "text": message, "parse_mode": "Markdown"}).encode('utf-8')
            req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
            urllib.request.urlopen(req, timeout=10)
        except Exception:
            pass

def open_url_in_chrome(url):
    """Membuka tautan pendaftaran langsung di Google Chrome HP"""
    cmd = f"am start -a android.intent.action.VIEW -d '{url}' com.android.chrome"
    os.system(cmd)
    time.sleep(4)

def tap(x, y):
    """Klik koordinat layar HP"""
    os.system(f"input tap {x} {y}")
    time.sleep(1)

def type_text(text):
    """Ketik teks di layar HP"""
    escaped = text.replace(" ", "%s")
    os.system(f"input text \"{escaped}\"")
    time.sleep(1)

def press_key(key_code):
    """Kirim event tombol Android (66=Enter, 4=Back, 67=Backspace)"""
    os.system(f"input keyevent {key_code}")
    time.sleep(1)

def press_back():
    """Tekan tombol Back fisik di HP"""
    press_key(4)
    time.sleep(1.5)

def press_enter():
    """Tekan tombol Enter / Next di keyboard"""
    press_key(66)
    time.sleep(2)

def main():
    print("=" * 60)
    print(">> MEMULAI BOT GMAIL (TERMUX ANDROID)...")
    print(f"Parent Email    : {CONFIG['PARENT_EMAIL']}")
    print(f"Market Password : {CONFIG['MARKET_PASSWORD']}")
    print(f"Tahun Bypass    : {CONFIG['ADULT_YEAR']}")
    print("=" * 60)

    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    digits = str(random.randint(10, 999))
    child_year = "2015"
    adult_year = CONFIG["ADULT_YEAR"]
    day_birth = str(random.randint(1, 28))
    market_uname = (first_name + last_name + digits)[:20]
    final_email = f"{market_uname}@gmail.com"

    # Kirim sinyal bot mulai ke Telegram
    send_telegram(f"🚀 *Bot Termux Dimulai di HP!*\nTarget: `{final_email}`\nParent: `{CONFIG['PARENT_EMAIL']}`")

    try:
        # STEP 1: Buka Google Chrome di HP
        log_step("STEP 1", "Membuka halaman pendaftaran akun Google di Chrome...")
        open_url_in_chrome("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        time.sleep(5)

        # STEP 2: Input Nama Anak
        log_step("STEP 2", f"Memasukkan Nama Anak: {first_name} {last_name}...")
        # Fokus ke input pertama
        press_key(66) # Buka fokus / Enter
        time.sleep(1)
        type_text(first_name)
        time.sleep(1)
        press_key(66) # Tab / Enter ke nama belakang
        time.sleep(1)
        type_text(last_name)
        time.sleep(1)
        press_enter() # Klik Berikutnya
        time.sleep(4)

        # STEP 3: Isi Tanggal Lahir Anak (Tahun: 2015)
        log_step("STEP 3", f"Mengisi Tanggal Lahir (Hari: {day_birth}, Tahun: {child_year})...")
        type_text(day_birth)
        time.sleep(1)
        press_key(66)
        type_text(child_year)
        time.sleep(1)
        press_enter()
        time.sleep(4)

        # STEP 4: Parent Sign-In
        log_step("STEP 4", f"Mengisi Email Orang Tua: {CONFIG['PARENT_EMAIL']}...")
        type_text(CONFIG["PARENT_EMAIL"])
        time.sleep(1)
        press_enter()
        time.sleep(5)

        # STEP 4.1: Password Orang Tua
        log_step("STEP 4.1", "Mengisi Password Akun Orang Tua...")
        type_text(CONFIG["PARENT_PASSWORD"])
        time.sleep(1)
        press_enter()
        time.sleep(6)

        print("\n" + "!" * 55)
        print("MOHON KETUK NOTIFIKASI VERIFIKASI 2FA DI HP JIKA ADA")
        print("Robot menunggu persetujuan orang tua (30 detik)...")
        print("!" * 55 + "\n")
        time.sleep(20)

        # STEP 5: Trik Back Bypass Umur Dewasa
        log_step("STEP 5", "MELAKUKAN TRIK BACK BYPASS KE GANTI UMUR...")
        for b in range(1, 7):
            print(f">> Menekan tombol Back ke-{b}...")
            press_back()
            time.sleep(2)

        # STEP 6: Ganti Tahun ke Dewasa (2001)
        log_step("STEP 6", f"Mengubah Tahun Lahir Menjadi Umur Dewasa: {adult_year}...")
        type_text(adult_year)
        time.sleep(1)
        press_enter()
        time.sleep(4)

        # STEP 7: Password Market Final
        log_step("STEP 7", f"Mengisi Password Market: {CONFIG['MARKET_PASSWORD']}...")
        type_text(CONFIG["MARKET_PASSWORD"])
        time.sleep(1)
        press_enter()
        time.sleep(4)

        # STEP 8: Sukses & Kirim Laporan ke Telegram
        log_step("STEP 8", "SUKSES! Akun berhasil dibuat dan dilaporkan.")
        
        success_msg = (
            f"✅ *GMAIL MARKET BERHASIL DIBUAT (TERMUX)*\n\n"
            f"📧 *Email:* `{final_email}`\n"
            f"🔑 *Password:* `{CONFIG['MARKET_PASSWORD']}`\n"
            f"📅 *Tahun Lahir:* `{adult_year}`\n"
            f"👤 *Nama:* {first_name} {last_name}\n"
            f"🛡️ *Parent:* `{CONFIG['PARENT_EMAIL']}`\n"
            f"📱 *Engine:* Termux Python Native"
        )
        send_telegram(success_msg)
        print("\n[OK] Laporan sukses telah dikirimkan ke Telegram Admin & Client!")

    except Exception as e:
        err_msg = f"🚨 *ERROR TERMUX BOT!*\n\n📍 *Macet di:* `{CURRENT_STEP}`\n⚠️ *Detail:* `{str(e)}`"
        send_telegram(err_msg)
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    main()
