# Whisper Watcher 📁🎧

Bu Python projesi, bir klasöre `.mp3` dosyası bırakıldığında OpenAI'nin **Whisper** modelini kullanarak dosyayı otomatik olarak yazıya çevirir. `watchdog` kütüphanesi sayesinde klasör izlenir ve yeni gelen dosyalar anında işlenir.

---

## 🚀 Özellikler

- 🎧 Klasöre bırakılan `.mp3` dosyalarını otomatik algılar
- 🧠 Whisper modeli ile transkripsiyon yapar (Türkçe destekli)
- 📄 Çıktıyı `.txt` dosyası olarak `output/` klasörüne kaydeder
- 👀 `watchdog` ile gerçek zamanlı klasör izleme

---

## 🔧 Gereksinimler

Aşağıdaki Python kütüphaneleri gereklidir:

```bash
pip install -r requirements.txt
```

### `requirements.txt` içeriği

```
whisper
watchdog
```

> Not: `whisper`, `ffmpeg` gibi bağımlılıklara da ihtiyaç duyar. Bunları sisteminize ayrıca kurmanız gerekebilir.

## ffmpeg Kurulumu (Windows için)
1. https://www.gyan.dev/ffmpeg/builds/ adresinden Essentials Build zip dosyasını indir.

2. Dosyayı çıkart, ffmpeg\\bin klasörünü örneğin C:\\ffmpeg\\bin olarak konumlandır.

3. Path ortam değişkenlerine bu yolu ekle:

Denetim Masası → Sistem → Gelişmiş Sistem Ayarları → Ortam Değişkenleri → Path → Yeni → C:\\ffmpeg\\bin

4. Komut satırını kapatıp açtıktan sonra test et:
```bash
ffmpeg -version
```

---

## 📁 Klasör Yapısı

```
your-project/
│
├── input/          # MP3 dosyalarını buraya bırak
├── output/         # Transkriptler burada oluşur
├── whisper_watcher.py
├── requirements.txt
└── README.md
```

---

## ▶️ Kullanım

1. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

2. Klasörleri oluşturun:

```bash
mkdir input output
```

3. Scripti başlatın:

```bash
python whisper_watcher.py
```

4. `input/` klasörüne `.mp3` dosyası bırakın. Otomatik olarak yazıya çevrilip `output/` klasörüne `.txt` dosyası olarak kaydedilecektir.

---

## 📝 Notlar

- Whisper modeli internetten ilk indirildiğinde biraz zaman alabilir.
- Default olarak `"large"` modeli kullanılmıştır. Daha hızlı çalışması için `"base"` gibi modeller tercih edilebilir:

```python
model = whisper.load_model("base")
```

---

## 📜 Lisans

MIT License.

---

## ✨ İlham

Bu proje, Whisper ile otomatik transkripsiyonun basit ama etkili bir örneğini göstermek için hazırlandı.