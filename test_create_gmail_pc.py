"""
==============================================================================
TEST AUTO CREATE GMAIL DI LAPTOP / PC (SELENIUM MOBILE EMULATION)
==============================================================================
Script ini memungkinkan Anda melakukan tes otomasi alur bypass ganti umur
langsung di laptop menggunakan Google Chrome.
Chrome akan dibuka dalam mode simulasi layar HP Android sehingga alurnya
persis 100% sama dengan di HP.

Cara Menjalankan:
    python test_create_gmail_pc.py
==============================================================================
"""

import warnings
warnings.filterwarnings("ignore")

import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==============================================================================
# KONFIGURASI PENGUJIAN DI LAPTOP
# ==============================================================================
CONFIG = {
    # Akun Induk Orang Tua (Parent Sign-In)
    "PARENT_EMAIL": "by.u001user@gmail.com",
    "PARENT_PASSWORD": "martabakmesir13",

    # Password Akun Jadi (Gmail Market): "sgsg1122" atau "goldacok" atau custom
    "MARKET_PASSWORD": "sgsg1122",

    # Tahun Dewasa setelah Back (2001 s/d 2008)
    "ADULT_YEAR": "2001",

    # Telegram Notifikasi
    "TELEGRAM_BOT_TOKEN": "9196997158:AAF5OutT0JHy73no84X8mhzwbFrm0BeUIzU",
    "TELEGRAM_CHAT_ID": "5993311226",
}

# Daftar nama acak natural
FIRST_NAMES = ["nadia", "arib", "bintang", "dian", "fajar", "gilang", "haikal", "ihsan", "lutfi", "maulana", "rizki", "kurnia", "satria", "wahyu"]
LAST_NAMES = ["pratama", "utomo", "cahyo", "bagas", "dimas", "gunawan", "hubner", "kaila", "seika", "zahra", "anisa", "saputra"]

def send_telegram(token, chat_id, message):
    if not token or not chat_id:
        return
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, json={"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}, timeout=10)
        print("[TELEGRAM] Notifikasi berhasil dikirim!")
    except Exception as e:
        print(f"[TELEGRAM] Gagal kirim: {e}")

def create_driver():
    """Membuat browser Chrome dengan simulasi layar HP Android"""
    chrome_options = Options()
    
    # Emulasi Perangkat Mobile (Android)
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
        "//button[contains(., 'Next') or contains(., 'Berikutnya') or contains(., 'Lanjutkan')]",
        "//*[@id='collectNameNext' or @id='birthdaygenderNext' or contains(@id, 'Next')]",
        "//*[text()='Next' or text()='Berikutnya']"
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
    """Mengisi Tanggal Lahir dan memilih Gender dengan selector scoped Google"""
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

    # 3. Bulan (hanya jika belum terisi atau kosong)
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

    # 4. Gender (Scoped ke id='gender' agar tidak salah klik ke bahasa)
    try:
        gender_trigger = driver.find_elements(By.XPATH, "//*[@id='gender']")
        if gender_trigger and gender_trigger[0].is_displayed():
            driver.execute_script("arguments[0].click();", gender_trigger[0])
            time.sleep(0.6)
            # data-value='1' adalah Female, data-value='2' adalah Male
            gender_opt = driver.find_elements(By.XPATH, "//*[@id='gender']//li[@role='option' and (@data-value='1' or @data-value='2')] | //ul[@aria-label='Gender' or contains(@aria-label, 'kelamin')]//li[@data-value='1']")
            if gender_opt:
                driver.execute_script("arguments[0].click();", gender_opt[0])
                print("[INFO] Gender berhasil dipilih!")
            time.sleep(0.4)
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except Exception as e:
        print(f"[DROPDOWN GENDER]: {e}")

    time.sleep(1)
    # 5. Klik Tombol Next khusus halaman Birthday & Gender
    btn_next = driver.find_elements(By.XPATH, "//*[@id='birthdaygenderNext']")
    if btn_next and btn_next[0].is_displayed():
        safe_click(driver, btn_next[0])
    else:
        click_next_button(driver)
    
    # Tunggu sampai halaman beralih
    time.sleep(3.5)

def input_email_smartly(driver, target_uname, prefer_custom=False):
    """
    Mendeteksi dengan akurat apakah halaman adalah:
    1. INPUT TEKS BIASA (Username input)
    2. PILIHAN RADIO BUTTON (Saran email Google seperti di screenshot + Create your own)
    Menunggu secara adaptif hingga 15 detik sampai elemen benar-benar render.
    """
    print("[INFO] Menunggu halaman pilihan/input email muncul...")
    start_time = time.time()
    
    while time.time() - start_time < 15:
        # 1. Cek apakah ada input teks Username yang terlihat langsung
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
            time.sleep(2.5)
            return "input"

        # 2. Cek apakah ada pilihan Radio Button (saran email seperti kailaarib@gmail.com atau Create your own)
        # Selektor untuk opsi saran email berakhiran @gmail.com yang bisa diklik
        email_elements = driver.find_elements(By.XPATH, "//*[contains(text(), '@gmail.com')]")
        visible_emails = [e for e in email_elements if e.is_displayed() and e.tag_name != "input"]
        
        radio_elements = driver.find_elements(By.XPATH, "//div[@role='radiogroup']//div[@role='radio'] | //div[@role='radio'] | //input[@type='radio']")
        visible_radios = [r for r in radio_elements if r.is_displayed()]

        create_own_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Create your own') or contains(text(), 'Buat alamat Gmail Anda sendiri')]")
        visible_create_own = [c for c in create_own_elements if c.is_displayed()]

        if visible_emails or visible_radios or visible_create_own:
            print("[INFO] Halaman terdeteksi: PILIHAN RADIO BUTTON.")
            
            if prefer_custom and visible_create_own:
                print("[INFO] Memilih opsi 'Create your own Gmail address'...")
                safe_click(driver, visible_create_own[0])
                time.sleep(1)
                
                # Cari input username yang muncul
                custom_inps = driver.find_elements(By.XPATH, "//input[@name='Username' or contains(@aria-label, 'Username') or contains(@aria-label, 'Nama pengguna')]")
                vis_custom = [ci for ci in custom_inps if ci.is_displayed()]
                if vis_custom:
                    vis_custom[0].click()
                    vis_custom[0].send_keys(target_uname)
                    time.sleep(0.5)
            else:
                # Pilih saran pertama Google (sangat aman, resmi, dan anti-bentrok)
                target_choice = visible_radios[0] if visible_radios else visible_emails[0]
                choice_text = target_choice.text.strip() if target_choice.text else "Opsi Pertama"
                print(f"[INFO] Memilih opsi saran Google: {choice_text}")
                safe_click(driver, target_choice)
                time.sleep(1)

            click_next_button(driver)
            time.sleep(3)
            return "radio"

        time.sleep(1)

    print("[WARNING] Halaman email/radio tidak terdeteksi dalam 15 detik.")
    return "unknown"

def main():
    print("=" * 60)
    print(">> MEMULAI TESTING OTOMASI GMAIL DI LAPTOP...")
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
        print("\n[STEP 1] Membuka halaman pendaftaran Google...")
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
        print(f"[STEP 2] Memasukkan Nama: {first_name} {last_name}...")
        time.sleep(2)
        inputs = driver.find_elements(By.TAG_NAME, "input")
        if len(inputs) >= 1:
            inputs[0].send_keys(first_name)
            time.sleep(0.5)
        if len(inputs) >= 2:
            inputs[1].send_keys(last_name)
            time.sleep(0.5)

        click_next_button(driver)

        # STEP 3: Isi Tanggal Lahir Awal (Tahun Anak: 2015)
        print("[STEP 3] Mengisi tanggal lahir anak (Tahun: 2015)...")
        fill_birthday_and_gender(driver, day=day_birth, year="2015")

        # Verifikasi apakah sudah lolos dari halaman Birthday & Gender
        if "birthdaygender" in driver.current_url:
            print("[INFO] Mencoba klik Next sekali lagi pada Birthday...")
            btn_next = driver.find_elements(By.XPATH, "//*[@id='birthdaygenderNext']")
            if btn_next:
                safe_click(driver, btn_next[0])
                time.sleep(3)

        # STEP 4: Buat Alamat Gmail Sementara & Password Dummy
        print("[STEP 4] Mengisi Gmail sementara & sandi dummy...")
        res_email = input_email_smartly(driver, temp_uname, prefer_custom=False)
        if res_email == "unknown":
            raise Exception("Gagal memilih/mengisi email sementara di Step 4.")

        # Password Sementara (Dummy) - Tunggu sampai form password muncul
        print("[STEP 4.1] Menunggu dan mengisi sandi sementara...")
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

        # STEP 5: Parent Sign-In (Email Orang Tua)
        print(f"[STEP 5] Masuk halaman Parent Sign-In: {CONFIG['PARENT_EMAIL']}...")
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

        # STEP 5.1: Password Orang Tua (Wajib Tunggu Form Password Benar-benar Muncul!)
        print(f"[STEP 5.1] Menunggu dan mengisi Password Ortu: {CONFIG['PARENT_PASSWORD']}...")
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

        # STEP 5.2: Verifikasi 2FA HP Orang Tua (POCO F6)
        print("[STEP 5.2] Memeriksa verifikasi keamanan akun orang tua...")
        time.sleep(2)
        
        # Cek apakah Google meminta klik notifikasi di HP (POCO)
        if any(k in driver.page_source for k in ["POCO", "Check your", "Periksa ponsel", "ketuk Ya", "tap Yes", "2-Step", "Verifikasi 2", "Do you have your"]):
            print("\n" + "!" * 60)
            print("MOHON SEGERA KETUK NOTIFIKASI DI HP ANDA (POCO F6)!")
            print("Robot menunggu Anda mengetuk angka konfirmasi di HP (maks 60 detik)...")
            print("!" * 60 + "\n")

        # Tunggu sampai verifikasi di HP di-tap dan masuk ke halaman Persetujuan Ortu ("I agree...")
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

        # Centang Persetujuan Orang Tua
        print("[STEP 5.3] Menyetujui syarat parental consent...")
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

        # STEP 5.4: Verifikasi Perangkat Orang Tua (Do a device check - Menit 2:05 di Video)
        print("[STEP 5.4] Memeriksa verifikasi info perangkat orang tua (Do a device check)...")
        time.sleep(2)
        for _ in range(15):
            if any(k in driver.page_source for k in ["Do a device check", "Verify some info", "Periksa perangkat", "Verifikasi info", "device or phone number"]):
                print(">> [INFO] Halaman 'Do a device check' terdeteksi! Mengklik tombol Continue...")
                click_continue_smartly(driver)
                time.sleep(3)
                break
            time.sleep(1)

        # STEP 5.5: Konfirmasi Perangkat "Are you trying to verify your info?" -> Klik "Yes, continue"
        print("[STEP 5.5] Memeriksa konfirmasi 'Are you trying to verify your info?'...")
        for _ in range(15):
            if any(k in driver.page_source for k in ["Are you trying to verify", "Apakah Anda mencoba memverifikasi", "Yes, continue", "Ya, lanjutkan", "matches your device"]):
                print(">> [INFO] Halaman konfirmasi 'Are you trying to verify your info?' terdeteksi! Mengklik 'Yes, continue'...")
                click_continue_smartly(driver)
                time.sleep(3.5)
                break
            time.sleep(1)

        # STEP 5.6: Tunggu hingga halaman "How you'll help manage her account" benar-benar muncul
        print("[STEP 5.6] Menunggu konfirmasi sah orang tua ('How you'll help manage account')...")
        parent_confirmed = False
        for wait_p in range(25):
            if any(k in driver.page_source for k in ["manage her account", "manage his account", "kelola akun", "How you'll help", "Nadia's Google Account", "account will be similar"]):
                print(">> Verifikasi orang tua 100% tervalidasi sah oleh Google! Memulai aksi BACK bypass...")
                parent_confirmed = True
                break
            
            # Jika masih tertahan di layar 'Do a device check' atau 'Are you trying', terus klik Continue/Yes
            if any(k in driver.page_source for k in ["Do a device check", "Verify some info", "Are you trying to verify"]):
                print(f">> [INFO] Masih di layar verifikasi perangkat, mencoba klik Continue lagi ({wait_p + 1})...")
                click_continue_smartly(driver)
            time.sleep(1.5)

        if not parent_confirmed:
            print("\n" + "!" * 60)
            print("[PERINGATAN] Tombol 'Continue' / 'Yes, continue' belum berpindah.")
            print("Silakan klik tombol Continue/Yes di jendela Chrome laptop Anda jika masih terlihat.")
            print("Robot menunggu Anda mengkliknya (maks 15 detik)...")
            print("!" * 60 + "\n")
            for _ in range(15):
                if any(k in driver.page_source for k in ["manage her account", "manage his account", "kelola akun", "How you'll help"]):
                    parent_confirmed = True
                    break
                time.sleep(1)

        if not parent_confirmed:
            raise Exception("Gagal melewati verifikasi perangkat orang tua. Halaman 'How you'll help manage account' tidak tercapai.")

        # STEP 6: KUNCI BYPASS -> KLIK BACK HINGGA BENAR-BENAR MUNCUL INPUT TAHUN (#year)
        print("\n" + "=" * 50)
        print(">> [STEP 6] MELAKUKAN BACK BYPASS KE MENU GANTI UMUR...")
        print("=" * 50)
        time.sleep(2)

        back_success = False
        for b in range(1, 10):
            print(f">> Menekan tombol BACK ke-{b}...")
            driver.back()
            time.sleep(2)

            # Validasi apakah input #year benar-benar TAMPIL (bukan hanya ada di cache/DOM)
            year_inputs = driver.find_elements(By.XPATH, "//input[@id='year' or contains(@name, 'year')]")
            if year_inputs and year_inputs[0].is_displayed():
                print(f">> Berhasil kembali ke halaman ganti umur setelah {b} kali BACK!")
                back_success = True
                break

        if not back_success:
            raise Exception("Gagal kembali ke halaman ganti umur: input '#year' tidak terlihat setelah tombol BACK ditekan berulang.")

        # STEP 7: GANTI TAHUN KE TAHUN DEWASA (2001) DAN PILIH GENDER LAGI
        print(f"\n[STEP 7] Mengubah tahun dari 2015 ke {CONFIG['ADULT_YEAR']} & mengisi ulang Gender...")
        fill_birthday_and_gender(driver, day=day_birth, year=CONFIG["ADULT_YEAR"])

        # Tunggu sampai form birthday benar-benar berganti
        for _ in range(8):
            year_inputs = driver.find_elements(By.XPATH, "//input[@id='year' or contains(@name, 'year')]")
            if not year_inputs or not year_inputs[0].is_displayed():
                break
            time.sleep(1)

        # STEP 7.1: CEK HALAMAN TRANSISI DEWASA ("Next steps are for [Nama]")
        time.sleep(2)
        for _ in range(6):
            if any(k in driver.page_source for k in ["Next steps are for", "Langkah berikutnya untuk", "able to create a Google Account", "dapat membuat Akun Google sendiri"]):
                print(">> [INFO] Halaman transisi Google terdeteksi: 'Next steps are for [Nama]'. Mengklik Next...")
                click_next_button(driver)
                time.sleep(3.5)
                break
            time.sleep(0.5)

        # STEP 8: INPUT GMAIL MARKET & PASSWORD MARKET (AKUN RESMI JADI)
        print(f"\n[STEP 8] Mengisi Alamat Gmail Market: {final_email}...")
        time.sleep(2)
        
        # Loop pengisian username market (dengan auto-fallback jika username taken)
        for attempt in range(5):
            res_type = input_email_smartly(driver, market_uname)
            time.sleep(2.5)

            # Cek apakah username sudah dipakai orang lain
            if "That username is taken" in driver.page_source or "telah digunakan" in driver.page_source or "sudah digunakan" in driver.page_source:
                print(f"[INFO] Username '{market_uname}' sudah digunakan. Mengambil saran Google / nomor baru...")
                time.sleep(1)

                # 1. Coba klik chip saran username yang disediakan Google (Available / Tersedia)
                suggestion_chips = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Available') or contains(@aria-label, 'Tersedia')] | //*[contains(text(), 'Available') or contains(text(), 'Tersedia')]/following::button | //ul[contains(@class, 'Suggestions')]//button")
                if suggestion_chips:
                    try:
                        suggested_text = suggestion_chips[0].text.strip()
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
                        print(f"[INFO] Gagal klik saran: {ex}")

                # 2. Jika tidak ada chip, buat kombinasi angka 4 digit baru
                market_uname = (first_name + last_name + str(random.randint(1000, 9999)))[:20]
                final_email = f"{market_uname}@gmail.com"
                print(f"[INFO] Mencoba username baru: {market_uname}")
                time.sleep(1)
            else:
                # Berhasil lolos tanpa error taken
                print(f"[INFO] Username berhasil diterima: {final_email}")
                break

        # Password Market Final
        print(f"[STEP 8.1] Mengisi Password Market Final: {CONFIG['MARKET_PASSWORD']}...")
        time.sleep(2)
        
        # Tunggu form password muncul
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

        # Cek apakah setelah submit password malah kembali minta bantuan orang tua
        time.sleep(4)
        if any(k in driver.page_source for k in ["Get help from a parent", "Bantuan dari orang tua", "Parent email or phone"]):
            raise Exception("Google tetap meminta verifikasi orang tua ('Get help from a parent'). Bypass umur belum berhasil diproses Google.")

        # STEP 9: PRIVACY AND TERMS REGULER
        print("[STEP 9] Menyetujui Privacy and Terms Google Reguler...")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        
        agree_final = driver.find_elements(By.XPATH, "//*[text()='I agree' or text()='Saya setuju' or contains(@aria-label, 'agree')]")
        if agree_final:
            safe_click(driver, agree_final[0])
            time.sleep(5)

        # Cek apakah muncul pop-up atau halaman 'Add a selfie' / 'Not now'
        not_now_btns = driver.find_elements(By.XPATH, "//*[text()='Not now' or text()='Jangan sekarang' or text()='Skip' or text()='Lewati']")
        if not_now_btns and not_now_btns[0].is_displayed():
            print("[INFO] Melewati halaman tambahan ('Not now')...")
            safe_click(driver, not_now_btns[0])
            time.sleep(3)

        # STEP 10: SUKSES & LAPOR KE TELEGRAM
        print("\n" + "=" * 60)
        print(">> [SUKSES] AKUN GMAIL MARKET BERHASIL DIBUAT!")
        print(f"Email    : {final_email}")
        print(f"Password : {CONFIG['MARKET_PASSWORD']}")
        print(f"Tahun    : {CONFIG['ADULT_YEAR']}")
        print("=" * 60)

        report = (
            f"✅ *GMAIL MARKET BERHASIL DIBUAT (TEST LAPTOP)*\n\n"
            f"📧 *Email:* `{final_email}`\n"
            f"🔑 *Password:* `{CONFIG['MARKET_PASSWORD']}`\n"
            f"📅 *Tahun Lahir:* `{CONFIG['ADULT_YEAR']}`\n"
            f"👤 *Nama:* {first_name} {last_name}\n"
            f"💻 *Device:* Laptop Chrome Mobile Emulation"
        )
        send_telegram(CONFIG["TELEGRAM_BOT_TOKEN"], CONFIG["TELEGRAM_CHAT_ID"], report)

        print("\nPengujian selesai! Tekan Enter di terminal jika sudah selesai melihat browser...")
        input()

    except Exception as e:
        print(f"\n[!] Terjadi Kendala saat pengujian: {e}")
        print("Browser tetap terbuka agar Anda bisa mengecek layar...")
        input("Tekan Enter untuk menutup...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
