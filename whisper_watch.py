import os
import time
import whisper
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

# ffmpeg yolunu sistem PATH'ine ekle
os.environ["PATH"] += os.pathsep + r"C:\Users\ckjiyat\Desktop\S2T\ffmpeg\bin"
print("[🧪] ffmpeg bulundu mu?:", shutil.which("ffmpeg"))

# input ve output klasörlerini oluştur (yoksa)
input_folder = "input"
output_folder = "output"
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Whisper modelini yükle
print("[📦] Whisper modeli yükleniyor...")
model = whisper.load_model("large")
print("[✅] Model yüklendi.")

# Watchdog sınıfı
class MP3Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".mp3"):
            return

        filename = os.path.basename(event.src_path)
        full_path = os.path.abspath(event.src_path)
        print(f"\n[🎧] Yeni dosya bulundu: {filename}")
        print(f"[🧩] Tam yol: {full_path}")

        # Dosya tamamen kopyalanmadan işleme başlamamak için bekle
        time.sleep(2)

        try:
            start_time = time.time()
            result = model.transcribe(full_path, language="turkish")
            elapsed = round(time.time() - start_time, 2)
            print(f"⏱ Transkripsiyon süresi: {elapsed} saniye")

            # Sonuçları yaz
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["text"])

            print(f"[✅] Çeviri tamamlandı → {output_path}")
        except Exception as e:
            print(f"[⛔] Hata oluştu: {e}")

# İzleme başlatılır
if __name__ == "__main__":
    print("[👀] 'input' klasörü izleniyor. MP3 dosyası bırakıldığında otomatik olarak yazıya dökülecek.")
    event_handler = MP3Handler()
    observer = Observer()
    observer.schedule(event_handler, path=input_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[🛑] İzleme durduruluyor...")
        observer.stop()

    observer.join()
    print("[✅] Program sonlandı.")
