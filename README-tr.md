# Restream 🚀

FFmpeg kullanarak RTMP akışlarını birden fazla çıkışa restream eden Python scripti. YouTube, Twitch vs. aynı anda yayın için mükemmel. Boş laf yok, çalışıyor.

## Gereksinimler 📋
- Python 3.x (kaynak: python.org)
- FFmpeg yüklü (kaynak: ffmpeg.org)

## Kurulum 🛠️
1. Bu repo'yu klonla
2. FFmpeg'in PATH'te olduğundan emin ol
3. `config.json`'u RTMP URL'lerinle düzenle

## Kullanım 🔥
```bash
python restream.py
```
Belirtilen portlarda RTMP sunucuları başlatır, input'u dinler, tüm çıkışlara push eder. Durdurmak için Ctrl+C.

## Yapılandırma ⚙️
`config.json`'u düzenle:
```json
[
    {
        "port": 1233,
        "url": "rtmp://localhost:{port}/live/streamkey",
        "outputs": [
            "rtmp://a.rtmp.youtube.com/live2/YOUR_KEY"
        ]
    }
]
```
Birden fazla akış için daha fazla sunucu ekle.

## Nasıl çalışıyor 🧠
FFmpeg'i listen modunda kullanarak RTMP input'u alır ve birden fazla çıkışa kopyalar. Thread'ler birden fazla sunucuyu yönetir. Kaynak: FFmpeg dokümantasyonu (ffmpeg.org)
