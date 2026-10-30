import urllib.request
import json
import random
import time
import os

print("=" * 50)
print(">> MENJALANKAN BOT AUTO CREATE GMAIL (TERMUX)...")
print("=" * 50)

TOKEN = "9196997158:AAF5OutT0JHy73no84X8mhzwbFrm0BeUIzU"
RECIPIENTS = ["5993311226", "392836663"]

def send_tele(text):
    for cid in RECIPIENTS:
        try:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            data = json.dumps({"chat_id": cid, "text": text, "parse_mode": "Markdown"}).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
            urllib.request.urlopen(req, timeout=10)
        except Exception as e:
            pass

send_tele("🚀 *Bot Termux Berhasil Dijalankan!*\nKoneksi repository dan telegram aktif.")
print("[OK] Notifikasi startup terkirim ke Telegram.")
