import time
import os
import whisper
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 1. Modeli bir kere yükle (yüklemesi birkaç saniye sürebilir)
model = whisper.load_model("large")

# 2. Giriş ve çıkış klasörleri
input_folder = "input"
output_folder = "output"

# 3. .mp3 dosyası klasöre eklendiğinde yapılacak işlemi tanımlarız
class MP3Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith(".mp3"):
            filename = os.path.basename(event.src_path)
            print(f"[🎧] Yeni dosya bulundu: {filename}")

            try:
                # Whisper modeliyle transkripsiyon yap
                result = model.transcribe(event.src_path, language="turkish")

                # .txt dosyasına kaydet
                output_path = os.path.join(
                    output_folder, os.path.splitext(filename)[0] + ".txt"
                )

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result["text"])

                print(f"[✅] Çeviri tamamlandı → {output_path}")
            except Exception as e:
                print(f"[⛔] Hata: {e}")

# 4. Klasör gözlemleyiciyi başlat
if __name__ == "__main__":
    event_handler = MP3Handler()
    observer = Observer()
    observer.schedule(event_handler, path=input_folder, recursive=False)
    observer.start()

    print("[👀] Klasör izleniyor. Dosya bırakıldığında otomatik işlenecek.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("İzleme durduruldu.")

    observer.join()
