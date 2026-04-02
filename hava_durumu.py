import requests
import time

# --- 1. AYARLAR (GÜVENLİ HALE GETİRİLDİ) ---
# LÜTFEN SİZ KENDİ PROJENİZİ GITHUB'A YÜKLEMEK İSTERSENİZ BURAYA GERÇEK ŞİFRELERİNİZİ YAZMAYIN!
WEATHER_API_KEY = "API_ANAHTARINIZI_BURAYA_GIRIN"
SEHIR = "Antalya"

# Telegram Ayarları
TELEGRAM_TOKEN = "TELEGRAM_TOKEN_BURAYA_GIRIN"
CHAT_ID = "CHAT_ID_BURAYA_GIRIN"

# Eşik Değeri (Sıcaklık bu derecenin altındaysa mesaj atacak)
ESIK_SICAKLIK = 20  

# Botun mesajı atıp atmadığını aklında tutacağı değişken (State / Bayrak)
mesaj_zaten_atildi = False 

# --- 2. TELEGRAM MESAJ GÖNDERME FONKSİYONU ---
def telegram_mesaj_gonder(mesaj):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    parametreler = {
        "chat_id": CHAT_ID,
        "text": mesaj
    }
    requests.get(url, params=parametreler)

print("Bot çalışmaya başladı. Hava durumu takip ediliyor...")
print("-" * 40)

# --- 3. OTOMASYON (SONSUZ DÖNGÜ) ---
while True:
    try:
        # Hava durumunu çek
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={SEHIR}&appid={WEATHER_API_KEY}&units=metric&lang=tr"
        response = requests.get(weather_url)
        veri = response.json()

        if response.status_code == 200:
            sicaklik = veri["main"]["temp"]
            durum = veri["weather"][0]["description"]
            
            print(f"Güncel Sıcaklık: {sicaklik}°C. Aranan Eşik: {ESIK_SICAKLIK}°C'nin altı.")

            # ŞART 1: Sıcaklık eşiğin altındaysa VE henüz mesaj atmadıysak
            if sicaklik < ESIK_SICAKLIK and not mesaj_zaten_atildi:
                uyari_mesaji = f"🥶 Üşüme Uyarısı!\n{SEHIR} anlık sıcaklık {sicaklik}°C'ye düştü.\nHava şu an: {durum.capitalize()}."
                
                telegram_mesaj_gonder(uyari_mesaji)
                print(">>> Telegram'a uyarı mesajı başarıyla gönderildi!")
                
                # Mesajı attığımızı sisteme not ediyoruz ki tekrar atmasın!
                mesaj_zaten_atildi = True 

            # ŞART 2: Sıcaklık tekrar eşiğin üstüne (normale) çıkarsa sistemi sıfırla
            elif sicaklik >= ESIK_SICAKLIK:
                mesaj_zaten_atildi = False
                
        else:
            print(f"Hava durumu verisi çekilirken bir hata oluştu. Hata kodu: {response.status_code}")

    except Exception as e:
        print("Bir bağlantı hatası oluştu. Lütfen internetinizi kontrol edin:", e)

    # Bekleme Süresi (1 saat = 3600 saniye)
    print("Bir sonraki kontrol için bekleniyor...\n")
    time.sleep(3600)