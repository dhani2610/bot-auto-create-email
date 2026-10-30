"""
==============================================================================
BOT AUTO CREATE GMAIL (PYTHON ENGINE - MULTI DEVICE SUPPORT)
==============================================================================
Mendukung eksekusi di:
- Laptop / PC (Chrome Driver)
- HP Android (Termux / Environment)
- Emulator Android

Fitur:
- Telemetry & Error Debugger ke Telegram Admin
- Notifikasi Akun Jadi ke 2 Chat Telegram (Admin & Client)
==============================================================================
"""

import warnings
warnings.filterwarnings("ignore")

import time
import os
import random
import requests
import traceback
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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

    # 2 Chat ID Penerima Hasil: Admin/Dev (Andaka) & Client (Idc)
    "ADMIN_CHAT_ID": "5993311226",
    "CLIENT_CHAT_ID": "392836663",
}

# Daftar nama acak natural
FIRST_NAMES = ["nadia", "arib", "bintang", "dian", "fajar", "gilang", "haikal", "ihsan", "lutfi", "maulana", "rizki", "kurnia", "satria", "wahyu"]
LAST_NAMES = ["pratama", "utomo", "cahyo", "bagas", "dimas", "gunawan", "hubner", "kaila", "seika", "zahra", "anisa", "saputra"]

CURRENT_STEP_NAME = "Inisialisasi"
CURRENT_STEP_DESC = "Memulai bot"

def set_step(name, desc=""):
    global CURRENT_STEP_NAME, CURRENT_STEP_DESC
    CURRENT_STEP_NAME = name
    CURRENT_STEP_DESC = desc
    print(f"\n[{name}] {desc}")

def send_telegram(token, chat_ids, message):
    """Mengirim pesan notifikasi ke satu atau beberapa chat ID Telegram"""
    if not token or not chat_ids:
        return
    if isinstance(chat_ids, str):
        chat_ids = [chat_ids]

    for cid in chat_ids:
        if not cid:
            continue
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.post(url, json={"chat_id": cid, "text": message, "parse_mode": "Markdown"}, timeout=10)
        except Exception as e:
            print(f"[TELEGRAM] Gagal kirim ke {cid}: {e}")

def report_error_to_telegram(driver, error_msg):
    """Mengambil screenshot dan elemen teks saat ini lalu lapor ke Telegram Admin"""
    token = CONFIG["TELEGRAM_BOT_TOKEN"]
    admin_id = CONFIG["ADMIN_CHAT_ID"]
    
    # Ambil teks yang tampak di halaman
    screen_summary = []
    try:
        elements = driver.find_elements(By.XPATH, "//button | //h1 | //h2 | //input | //div[@role='button'] | //p")
        seen = set()
        for el in elements:
            txt = el.text.strip()
            if txt and txt not in seen:
                seen.add(txt)
                screen_summary.append(f"• [{el.tag_name}] \"{txt}\"")
                if len(screen_summary) >= 15:
                    break
    except Exception:
        pass

    tele_msg = (
        f"🚨 *LAPORAN ERROR DARI BOT PYTHON!*\n\n"
        f"📍 *Macet di:* `{CURRENT_STEP_NAME}`\n"
        f"📝 *Deskripsi:* {CURRENT_STEP_DESC}\n"
        f"⚠️ *Detail Error:* `{str(error_msg)}`\n"
        f"🕒 *Waktu:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        f"🔍 *Elemen yang Tampak di Layar:*\n"
        + ("\n".join(screen_summary) if screen_summary else "(Tidak ada elemen terdeteksi)")
    )
    send_telegram(token, admin_id, tele_msg)

    # Kirim juga screenshot ke Telegram Admin
    try:
        screenshot_path = "debug_screenshot.png"
        driver.save_screenshot(screenshot_path)
        with open(screenshot_path, "rb") as f:
            url = f"https://api.telegram.org/bot{token}/sendPhoto"
            requests.post(url, data={"chat_id": admin_id, "caption": f"📸 Screenshot saat macet di {CURRENT_STEP_NAME}"}, files={"photo": f}, timeout=15)
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
    except Exception as ex:
        print(f"[DEBUG] Gagal kirim foto: {ex}")

def create_driver():
    """Membuat browser Chrome dengan opsi anti-deteksi bot"""
    chrome_options = Options()
    
    mobile_emulation = {
        "deviceMetrics": {"width": 390, "height": 844, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(450, 950)
    return driver

def safe_click(driver, element):
    """Klik elemen secara aman (anti-intercept) menggunakan JavaScript"""
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.3)
        driver.execute_script("arguments[0].click();", element)
    except Exception:
        element.click()

def click_next_button(driver):
    """Klik tombol Next / Berikutnya umum"""
    time.sleep(0.8)
    try:
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.3)
    except:
        pass

    selectors = [
        "//button[contains(., 'Next') or contains(., 'Berikutnya') or contains(., 'Lanjutkan') or contains(., 'Ayo')]",
        "//*[@id='collectNameNext' or @id='birthdaygenderNext' or contains(@id, 'Next')]",
        "//*[text()='Next' or text()='Berikutnya' or text()='Ayo!']"
    ]
    target_btn = None
    for s in selectors:
        found = driver.find_elements(By.XPATH, s)
        for f in found:
            if f.is_displayed():
                target_btn = f
                break
        if target_btn:
            break

    if target_btn:
        safe_click(driver, target_btn)
    else:
        ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(3.5)

def click_continue_smartly(driver):
    """Mengeklik tombol Continue / Yes, continue pada verifikasi perangkat dengan berbagai metode"""
    time.sleep(1)
    selectors = [
        "//button[contains(., 'Continue') or contains(., 'Lanjutkan') or contains(., 'continue')]",
        "//*[contains(text(), 'Continue') or contains(text(), 'Lanjutkan')]/ancestor-or-self::button",
        "//*[contains(text(), 'Continue') or contains(text(), 'Lanjutkan')]/ancestor-or-self::div[@role='button']",
        "//*[contains(text(), 'Yes, continue') or contains(text(), 'Ya, lanjutkan')]",
        "//button[contains(@class, 'VfPpkd-LgbsSe') and not(@disabled)]"
    ]
    for s in selectors:
        btns = driver.find_elements(By.XPATH, s)
        for b in btns:
            if b.is_displayed():
                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", b)
                    time.sleep(0.3)
                    driver.execute_script("arguments[0].click();", b)
                    return True
                except:
                    try:
                        b.click()
                        return True
                    except:
                        pass
    try:
        ActionChains(driver).send_keys(Keys.ENTER).perform()
        return True
    except:
        return False

def fill_birthday_and_gender(driver, day, year):
    """Mengisi Tanggal Lahir dan memilih Gender secara akurat"""
    time.sleep(1.5)
    
    # Tunggu dan pastikan field tahun terlihat
    year_found = False
    for _ in range(10):
        year_in = driver.find_elements(By.XPATH, "//input[@id='year' or contains(@name, 'year')]")
        if year_in and year_in[0].is_displayed():
            year_found = True
            break
        time.sleep(1)
    
    if not year_found:
        raise Exception("Halaman Tanggal Lahir & Gender tidak aktif (input #year tidak ditemukan).")

    # 1. Hari
    day_in = driver.find_elements(By.XPATH, "//input[@id='day' or contains(@name, 'day')]")
    if day_in and day_in[0].is_displayed():
        day_in[0].click()
        day_in[0].send_keys(Keys.CONTROL + "a")
        day_in[0].send_keys(Keys.BACKSPACE)
        time.sleep(0.2)
        day_in[0].send_keys(str(day))
        time.sleep(0.3)

    # 2. Tahun
    year_in = driver.find_elements(By.XPATH, "//input[@id='year' or contains(@name, 'year')]")
    if year_in and year_in[0].is_displayed():
        year_in[0].click()
        year_in[0].send_keys(Keys.CONTROL + "a")
        year_in[0].send_keys(Keys.BACKSPACE)
        time.sleep(0.2)
        year_in[0].send_keys(str(year))
        time.sleep(0.3)
        print(f"[INFO] Tahun berhasil diisi: {year}")

    # 3. Bulan
    try:
        month_trigger = driver.find_elements(By.XPATH, "//*[@id='month']")
        if month_trigger and month_trigger[0].is_displayed():
            driver.execute_script("arguments[0].click();", month_trigger[0])
            time.sleep(0.6)
            month_opt = driver.find_elements(By.XPATH, "//*[@id='month']//li[@role='option' and @data-value='8'] | //ul[@aria-label='Month' or contains(@aria-label, 'Bulan')]//li[@data-value='8']")
            if month_opt:
                driver.execute_script("arguments[0].click();", month_opt[0])
            time.sleep(0.4)
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except Exception as e:
        print(f"[DROPDOWN BULAN]: {e}")

    # 4. Gender
    try:
        gender_trigger = driver.find_elements(By.XPATH, "//*[@id='gender']")
        if gender_trigger and gender_trigger[0].is_displayed():
            driver.execute_script("arguments[0].click();", gender_trigger[0])
            time.sleep(0.6)
            gender_opt = driver.find_elements(By.XPATH, "//*[@id='gender']//li[@role='option' and (@data-value='1' or @data-value='2')] | //ul[@aria-label='Gender' or contains(@aria-label, 'kelamin')]//li[@data-value='1']")
            if gender_opt:
                driver.execute_script("arguments[0].click();", gender_opt[0])
                print("[INFO] Gender berhasil dipilih!")
            time.sleep(0.4)
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except Exception as e:
        print(f"[DROPDOWN GENDER]: {e}")

    time.sleep(1)
    btn_next = driver.find_elements(By.XPATH, "//*[@id='birthdaygenderNext']")
    if btn_next and btn_next[0].is_displayed():
        safe_click(driver, btn_next[0])
    else:
        click_next_button(driver)
    time.sleep(3.5)

def input_email_smartly(driver, target_uname, prefer_custom=False):
    """Mendeteksi apakah input berupa form Username biasa atau pilihan Radio Button dari Google"""
    print("[INFO] Menunggu halaman pilihan/input email muncul...")
    start_time = time.time()
    
    while time.time() - start_time < 15:
        text_inputs = driver.find_elements(By.XPATH, "//input[@name='Username' or contains(@aria-label, 'Username') or contains(@aria-label, 'Nama pengguna')]")
        visible_texts = [inp for inp in text_inputs if inp.is_displayed()]
        if visible_texts:
            inp = visible_texts[0]
            print(f"[INFO] Halaman terdeteksi: INPUT TEKS BIASA. Mengisi: {target_uname}")
            inp.click()
            inp.send_keys(Keys.CONTROL + "a")
            inp.send_keys(Keys.BACKSPACE)
            time.sleep(0.3)
            inp.send_keys(target_uname)
            time.sleep(0.8)
            click_next_button(driver)
            return "text_input"

        radios = driver.find_elements(By.XPATH, "//div[@role='radio'] | //input[@type='radio']")
        visible_radios = [r for r in radios if r.is_displayed()]
        if visible_radios:
            print("[INFO] Halaman terdeteksi: PILIHAN RADIO BUTTON.")
            selected_email = ""
            try:
                labels = driver.find_elements(By.XPATH, "//div[@role='radio']//div[contains(text(), '@gmail.com')]")
                if labels:
                    selected_email = labels[0].text.strip()
            except:
                pass
            
            safe_click(driver, visible_radios[0])
            print(f"[INFO] Memilih opsi saran Google: {selected_email if selected_email else 'Pilihan 1'}")
            time.sleep(1)
            click_next_button(driver)
            return "radio_saran"

        time.sleep(1)
    return "unknown"

def main():
    print("=" * 60)
    print(">> MEMULAI BOT AUTO CREATE GMAIL (PYTHON ENGINE)...")
    print(f"Parent Email    : {CONFIG['PARENT_EMAIL']}")
    print(f"Market Password : {CONFIG['MARKET_PASSWORD']}")
    print(f"Tahun Bypass    : {CONFIG['ADULT_YEAR']}")
    print("=" * 60)

    driver = create_driver()

    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    digits = str(random.randint(10, 999))
    day_birth = random.randint(1, 28)
    temp_uname = (first_name + last_name + str(random.randint(100, 999)))[:20]
    temp_pw = f"dummy{random.randint(10000, 99999)}"
    market_uname = (first_name + last_name + digits)[:20]
    final_email = f"{market_uname}@gmail.com"

    try:
        # STEP 1: Buka Halaman Sign Up Google
        set_step("STEP 1", "Membuka halaman pendaftaran Google...")
        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
        time.sleep(3)

        # Klik "Create account" jika ada di halaman login biasa
        create_btns = driver.find_elements(By.XPATH, "//*[contains(text(), 'Create account') or contains(text(), 'Buat akun')]")
        if create_btns:
            safe_click(driver, create_btns[0])
            time.sleep(1.5)
            child_opts = driver.find_elements(By.XPATH, "//*[contains(text(), 'child') or contains(text(), 'anak')]")
            if child_opts:
                safe_click(driver, child_opts[0])
                time.sleep(2)
            
            cont_btns = driver.find_elements(By.XPATH, "//*[contains(text(), 'continue') or contains(text(), 'lanjutkan') or contains(text(), 'Yes')]")
            if cont_btns:
                safe_click(driver, cont_btns[0])
                time.sleep(3)

        # STEP 2: Input Nama Anak
        set_step("STEP 2", f"Memasukkan Nama: {first_name} {last_name}...")
        time.sleep(2)
        inputs = driver.find_elements(By.TAG_NAME, "input")
        if len(inputs) >= 1:
            inputs[0].send_keys(first_name)
            time.sleep(0.5)
        if len(inputs) >= 2:
            inputs[1].send_keys(last_name)
            time.sleep(0.5)

        click_next_button(driver)

        # Cek jika ada layar pengantar "Buat Akun Google untuk anak Anda" -> Ayo!
        for _ in range(3):
            ayo_btns = driver.find_elements(By.XPATH, "//*[text()='Ayo!' or text()='Ayo' or contains(text(), \"Let's go\")]")
            if ayo_btns and ayo_btns[0].is_displayed():
                print("[INFO] Layar 'Ayo!' terdeteksi. Mengklik...")
                safe_click(driver, ayo_btns[0])
                time.sleep(3)
                break
            time.sleep(1)

        # STEP 3: Isi Tanggal Lahir Awal (Tahun Anak: 2015)
        set_step("STEP 3", "Mengisi tanggal lahir awal anak (Tahun: 2015)...")
        fill_birthday_and_gender(driver, day=day_birth, year="2015")

        if "birthdaygender" in driver.current_url:
            print("[INFO] Mencoba klik Next sekali lagi pada Birthday...")
            btn_next = driver.find_elements(By.XPATH, "//*[@id='birthdaygenderNext']")
            if btn_next:
                safe_click(driver, btn_next[0])
                time.sleep(3)

        # STEP 4: Buat Alamat Gmail Sementara & Password Dummy
        set_step("STEP 4", "Mengisi Gmail sementara & sandi dummy...")
        res_email = input_email_smartly(driver, temp_uname, prefer_custom=False)
        if res_email == "unknown":
            raise Exception("Gagal memilih/mengisi email sementara di Step 4.")

        set_step("STEP 4.1", "Menunggu dan mengisi sandi sementara...")
        pw_filled = False
        for _ in range(12):
            pw_inputs = driver.find_elements(By.XPATH, "//input[@type='password']")
            visible_pws = [p for p in pw_inputs if p.is_displayed()]
            if visible_pws:
                for p in visible_pws:
                    p.clear()
                    p.send_keys(temp_pw)
                    time.sleep(0.4)
                click_next_button(driver)
                pw_filled = True
                time.sleep(3.5)
                break
            time.sleep(1)

        if not pw_filled:
            raise Exception("Form Password sementara tidak muncul di Step 4.")

        # STEP 5: Parent Sign-In
        set_step("STEP 5", f"Masuk halaman Parent Sign-In: {CONFIG['PARENT_EMAIL']}...")
        email_parent_filled = False
        for _ in range(12):
            parent_email_in = driver.find_elements(By.XPATH, "//input[@type='email' or contains(@name, 'identifier')]")
            visible_emails = [e for e in parent_email_in if e.is_displayed()]
            if visible_emails:
                visible_emails[0].click()
                visible_emails[0].clear()
                visible_emails[0].send_keys(CONFIG["PARENT_EMAIL"])
                time.sleep(0.8)
                click_next_button(driver)
                email_parent_filled = True
                time.sleep(3.5)
                break
            time.sleep(1)

        # STEP 5.1: Password Orang Tua
        set_step("STEP 5.1", f"Menunggu dan mengisi Password Ortu...")
        pw_parent_filled = False
        for _ in range(15):
            parent_pw_in = driver.find_elements(By.XPATH, "//input[@type='password' or @name='Passwd']")
            visible_pws = [p for p in parent_pw_in if p.is_displayed()]
            if visible_pws:
                visible_pws[0].click()
                visible_pws[0].clear()
                visible_pws[0].send_keys(CONFIG["PARENT_PASSWORD"])
                time.sleep(0.8)
                click_next_button(driver)
                pw_parent_filled = True
                time.sleep(3.5)
                break
            time.sleep(1)

        if not pw_parent_filled:
            raise Exception("Form Password Akun Orang Tua tidak muncul di layar.")

        # STEP 5.2: Verifikasi 2FA HP Orang Tua
        set_step("STEP 5.2", "Memeriksa verifikasi keamanan akun orang tua (2FA)...")
        time.sleep(2)
        
        if any(k in driver.page_source for k in ["POCO", "Check your", "Periksa ponsel", "ketuk Ya", "tap Yes", "2-Step", "Verifikasi 2", "Do you have your"]):
            print("\n" + "!" * 60)
            print("MOHON SEGERA KETUK NOTIFIKASI DI HP ORANG TUA!")
            print("Robot menunggu Anda mengetuk angka konfirmasi di HP (maks 60 detik)...")
            print("!" * 60 + "\n")

        consent_reached = False
        start_wait = time.time()
        while time.time() - start_wait < 60:
            if "I agree" in driver.page_source or "Saya setuju" in driver.page_source or len(driver.find_elements(By.XPATH, "//input[@type='checkbox']")) > 0:
                consent_reached = True
                print(">> Verifikasi HP selesai! Masuk ke persetujuan orang tua.")
                break
            elif "manage her account" in driver.page_source or "manage his account" in driver.page_source or "kelola akun" in driver.page_source:
                consent_reached = True
                break
            time.sleep(2)

        # STEP 5.3: Centang Persetujuan Orang Tua
        set_step("STEP 5.3", "Menyetujui syarat parental consent...")
        time.sleep(1.5)
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        for cb in checkboxes:
            try:
                if not cb.is_selected():
                    driver.execute_script("arguments[0].click();", cb)
                    time.sleep(0.5)
            except:
                pass

        agree_btn = driver.find_elements(By.XPATH, "//*[text()='I agree' or text()='Saya setuju' or text()='Next' or text()='Berikutnya']")
        if agree_btn:
            safe_click(driver, agree_btn[-1])
            time.sleep(4)

        # STEP 5.4: Do a device check
        set_step("STEP 5.4", "Memeriksa verifikasi info perangkat orang tua (Do a device check)...")
        time.sleep(2)
        for _ in range(15):
            if any(k in driver.page_source for k in ["Do a device check", "Verify some info", "Periksa perangkat", "Verifikasi info", "device or phone number"]):
                print(">> [INFO] Halaman 'Do a device check' terdeteksi! Mengklik tombol Continue...")
                click_continue_smartly(driver)
                time.sleep(3)
                break
            time.sleep(1)

        # STEP 5.5: Konfirmasi Perangkat "Are you trying to verify your info?"
        set_step("STEP 5.5", "Memeriksa konfirmasi 'Are you trying to verify your info?'...")
        for _ in range(15):
            if any(k in driver.page_source for k in ["Are you trying to verify", "Apakah Anda mencoba memverifikasi", "Yes, continue", "Ya, lanjutkan", "matches your device"]):
                print(">> [INFO] Halaman konfirmasi 'Are you trying to verify your info?' terdeteksi! Mengklik 'Yes, continue'...")
                click_continue_smartly(driver)
                time.sleep(3.5)
                break
            time.sleep(1)

        # STEP 5.6: Tunggu hingga halaman "How you'll help manage her account"
        set_step("STEP 5.6", "Menunggu konfirmasi sah orang tua ('How you'll help manage account')...")
        parent_confirmed = False
        for wait_p in range(25):
            if any(k in driver.page_source for k in ["manage her account", "manage his account", "kelola akun", "How you'll help", "Google Account", "account will be similar"]):
                print(">> Verifikasi orang tua 100% tervalidasi sah oleh Google! Memulai aksi BACK bypass...")
                parent_confirmed = True
                break
            
            if any(k in driver.page_source for k in ["Do a device check", "Verify some info", "Are you trying to verify"]):
                print(f">> [INFO] Masih di layar verifikasi perangkat, mencoba klik Continue lagi ({wait_p + 1})...")
                click_continue_smartly(driver)
            time.sleep(1.5)

        if not parent_confirmed:
            for _ in range(10):
                if any(k in driver.page_source for k in ["manage her account", "manage his account", "kelola akun", "How you'll help"]):
                    parent_confirmed = True
                    break
                time.sleep(1)

        # STEP 6: KUNCI BYPASS -> KLIK BACK HINGGA MUNCUL INPUT TAHUN
        set_step("STEP 6", "MELAKUKAN BACK BYPASS KE MENU GANTI UMUR...")
        time.sleep(2)

        back_success = False
        for b in range(1, 10):
            print(f">> Menekan tombol BACK ke-{b}...")
            driver.back()
            time.sleep(2)

            year_inputs = driver.find_elements(By.XPATH, "//input[@id='year' or contains(@name, 'year')]")
            visible_years = [y for y in year_inputs if y.is_displayed()]
            
            if visible_years and any(k in driver.page_source for k in ["Basic info", "Informasi dasar", "birthday", "tanggal lahir", "Gender"]):
                print(f">> [BERHASIL] Halaman Tanggal Lahir & Gender berhasil dicapai pada Back ke-{b}!")
                back_success = True
                time.sleep(1.5)
                break

        if not back_success:
            raise Exception("Gagal kembali ke halaman Tanggal Lahir setelah menekan tombol Back 9 kali.")

        # STEP 7: UBAH TAHUN LAHIR MENJADI UMUR DEWASA (2001)
        set_step("STEP 7", f"MENGUBAH TAHUN MENJADI UMUR DEWASA: {CONFIG['ADULT_YEAR']}...")
        time.sleep(1.5)
        
        year_in = driver.find_elements(By.XPATH, "//input[@id='year' or contains(@name, 'year')]")
        if year_in:
            year_in[0].click()
            year_in[0].send_keys(Keys.CONTROL + "a")
            year_in[0].send_keys(Keys.BACKSPACE)
            time.sleep(0.3)
            year_in[0].send_keys(CONFIG["ADULT_YEAR"])
            print(f">> [INFO] Tahun berhasil diubah menjadi: {CONFIG['ADULT_YEAR']}")
            time.sleep(0.5)

        # Pilih ulang Gender (karena Google selalu mereset gender saat di-Back)
        try:
            gender_trigger = driver.find_elements(By.XPATH, "//*[@id='gender']")
            if gender_trigger and gender_trigger[0].is_displayed():
                driver.execute_script("arguments[0].click();", gender_trigger[0])
                time.sleep(0.6)
                gender_opt = driver.find_elements(By.XPATH, "//*[@id='gender']//li[@role='option' and (@data-value='1' or @data-value='2')] | //ul[@aria-label='Gender' or contains(@aria-label, 'kelamin')]//li[@data-value='1']")
                if gender_opt:
                    driver.execute_script("arguments[0].click();", gender_opt[0])
                    print("[INFO] Gender berhasil dipilih ulang setelah Back!")
                time.sleep(0.4)
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        except Exception as e:
            print(f"[DROPDOWN GENDER BACK]: {e}")

        # Klik Next mengunci akun dewasa
        btn_next = driver.find_elements(By.XPATH, "//*[@id='birthdaygenderNext']")
        if btn_next and btn_next[0].is_displayed():
            safe_click(driver, btn_next[0])
        else:
            click_next_button(driver)
        time.sleep(4)

        # STEP 7.1: Transisi "Next steps are for [Nama]"
        if any(k in driver.page_source for k in ["Next steps", "Langkah berikutnya", "able to create", "dapat membuat"]):
            print("[INFO] Halaman transisi mandiri terdeteksi! Mengklik Next...")
            click_next_button(driver)
            time.sleep(3.5)

        # STEP 8: INPUT GMAIL MARKET & PASSWORD MARKET
        set_step("STEP 8", f"Membuat Alamat Gmail Market: {final_email}...")
        time.sleep(2)

        for attempt_u in range(5):
            username_inputs = driver.find_elements(By.XPATH, "//input[@name='Username' or contains(@aria-label, 'Username') or contains(@aria-label, 'Nama pengguna')]")
            visible_unames = [u for u in username_inputs if u.is_displayed()]
            
            if visible_unames:
                visible_unames[0].click()
                visible_unames[0].send_keys(Keys.CONTROL + "a")
                visible_unames[0].send_keys(Keys.BACKSPACE)
                time.sleep(0.3)
                visible_unames[0].send_keys(market_uname)
                time.sleep(0.8)
                click_next_button(driver)
                time.sleep(2.5)

            if any(k in driver.page_source for k in ["taken", "digunakan", "That username is taken"]):
                print(f"[INFO] Username '{market_uname}' sudah dipakai. Mencoba saran Google...")
                suggestion_chips = driver.find_elements(By.XPATH, "//button[contains(@class, 'VfPpkd-LgbsSe') and contains(., '@gmail.com')] | //span[contains(text(), '@gmail.com')]")
                if suggestion_chips:
                    try:
                        suggested_text = suggestion_chips[0].text.replace("@gmail.com", "").strip()
                        safe_click(driver, suggestion_chips[0])
                        time.sleep(1)
                        if suggested_text:
                            market_uname = suggested_text
                            final_email = f"{market_uname}@gmail.com"
                            print(f"[INFO] Memilih saran Google: {final_email}")
                        click_next_button(driver)
                        time.sleep(2.5)
                        break
                    except Exception as ex:
                        pass

                market_uname = (first_name + last_name + str(random.randint(1000, 9999)))[:20]
                final_email = f"{market_uname}@gmail.com"
                print(f"[INFO] Mencoba username baru: {market_uname}")
                time.sleep(1)
            else:
                print(f"[INFO] Username berhasil diterima: {final_email}")
                break

        # STEP 8.1: Password Market Final
        set_step("STEP 8.1", f"Mengisi Password Market: {CONFIG['MARKET_PASSWORD']}...")
        time.sleep(2)
        
        for _ in range(10):
            final_pw_inputs = driver.find_elements(By.XPATH, "//input[@type='password']")
            visible_pws = [p for p in final_pw_inputs if p.is_displayed()]
            if visible_pws:
                for fpw in visible_pws:
                    fpw.clear()
                    fpw.send_keys(CONFIG["MARKET_PASSWORD"])
                    time.sleep(0.4)
                click_next_button(driver)
                break
            time.sleep(1)
        else:
            raise Exception("Form Password Market tidak ditemukan di halaman.")

        time.sleep(4)
        if any(k in driver.page_source for k in ["Get help from a parent", "Bantuan dari orang tua", "Parent email or phone"]):
            raise Exception("Google tetap meminta verifikasi orang tua. Bypass umur belum berhasil.")

        # STEP 9: PRIVACY AND TERMS REGULER
        set_step("STEP 9", "Menyetujui Privacy and Terms Google Reguler...")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        
        agree_final = driver.find_elements(By.XPATH, "//*[text()='I agree' or text()='Saya setuju' or contains(@aria-label, 'agree')]")
        if agree_final:
            safe_click(driver, agree_final[0])
            time.sleep(5)

        not_now_btns = driver.find_elements(By.XPATH, "//*[text()='Not now' or text()='Jangan sekarang' or text()='Skip' or text()='Lewati']")
        if not_now_btns and not_now_btns[0].is_displayed():
            print("[INFO] Melewati halaman tambahan ('Not now')...")
            safe_click(driver, not_now_btns[0])
            time.sleep(3)

        # STEP 10: SUKSES & LAPOR KE DUA TELEGRAM (ADMIN & CLIENT)
        set_step("STEP 10", "Sukses! Mengirimkan kredensial ke Telegram...")
        print("\n" + "=" * 60)
        print(">> [SUKSES] AKUN GMAIL MARKET BERHASIL DIBUAT!")
        print(f"Email    : {final_email}")
        print(f"Password : {CONFIG['MARKET_PASSWORD']}")
        print(f"Tahun    : {CONFIG['ADULT_YEAR']}")
        print("=" * 60)

        report = (
            f"✅ *GMAIL MARKET BERHASIL DIBUAT!*\n\n"
            f"📧 *Email:* `{final_email}`\n"
            f"🔑 *Password:* `{CONFIG['MARKET_PASSWORD']}`\n"
            f"📅 *Tahun Lahir:* `{CONFIG['ADULT_YEAR']}`\n"
            f"👤 *Nama:* {first_name} {last_name}\n"
            f"📱 *Metode:* Bypass Ganti Umur (Parent -> Dewasa)"
        )
        
        # Kirim ke 2 Chat Telegram: Admin (Andaka) & Client (Idc)
        recipients = [CONFIG["ADMIN_CHAT_ID"], CONFIG["CLIENT_CHAT_ID"]]
        send_telegram(CONFIG["TELEGRAM_BOT_TOKEN"], recipients, report)
        print(f"[TELEGRAM] Hasil terkirim ke Admin ({CONFIG['ADMIN_CHAT_ID']}) & Client ({CONFIG['CLIENT_CHAT_ID']})!")

    except Exception as e:
        print(f"\n[!] Terjadi Kendala: {e}")
        report_error_to_telegram(driver, e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
