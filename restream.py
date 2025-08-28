import subprocess
import sys
import json
import threading

def start_rtmp_server(input_url, output_urls):
    """
    RTMP sunucusu aç ve gelen akışı restream et.

    :param input_url: Dinlenecek RTMP URL (ör: rtmp://localhost:1935/live/input)
    :param output_urls: Çıkış RTMP URL'leri listesi
    """
    if not output_urls:
        print("Çıkış URL'leri yok!")
        return

    # FFmpeg komutu: listen modunda input al, multiple output ver
    cmd = [
        'ffmpeg',
        '-loglevel', 'quiet',
        '-listen', '1',
        '-i', input_url,
        '-avoid_negative_ts', 'make_zero',
        '-fflags', '+igndts+genpts+discardcorrupt',
        '-c', 'copy'
    ]
    for url in output_urls:
        cmd.extend(['-f', 'flv', url])

    print(f"Komut: {' '.join(cmd)}")
    print("RTMP sunucusu başlatıldı. Yayıncı bağlanınca restream başlayacak...")

    while True:
        try:
            # FFmpeg'i çalıştır (blocking)
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Hata: {e}")
            continue
        except KeyboardInterrupt:
            print("Sunucu durduruldu.")
            break

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    config = load_config()

    threads = []
    for server in config:
        port = server["port"]
        input_url = server["url"].format(port=port)
        outputs = server["outputs"]
        thread = threading.Thread(target=start_rtmp_server, args=(input_url, outputs))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Tüm sunucular durduruldu.")
