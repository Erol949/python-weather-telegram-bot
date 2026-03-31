# 🌤️ Canlı Hava Durumu Telegram Uyarı Botu

Bu proje, RESTful API'ler üzerinden haberleşerek belirlediğiniz şehrin güncel hava durumu verilerini çeken ve sıcaklık belirli bir eşik değerinin altına düştüğünde Telegram üzerinden size otomatik uyarı mesajı gönderen bir Python otomasyon betiğidir (script).

## 🚀 Özellikler

* **Canlı Veri Çekme:** OpenWeatherMap API kullanılarak gerçek zamanlı sıcaklık ve hava durumu takibi yapılır.
* **Telegram Entegrasyonu:** BotFather ile oluşturulan Telegram botu üzerinden anlık bildirimler gönderilir.
* **Spam Koruması (State Management):** Durum kontrol mekanizması sayesinde, aynı hava durumu olayı için API'yi ve kullanıcıyı yoracak şekilde defalarca mesaj atılması engellenir.
* **Otomasyon:** Sürekli çalışan arka plan döngüsü ile belirlenen zaman aralıklarında otomatik kontroller sağlanır.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Kütüphaneler:** `requests`, `time`
* **API'ler:** OpenWeatherMap API, Telegram Bot API
