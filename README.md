# Restream 🚀

A Python script to restream RTMP streams to multiple outputs using FFmpeg. Perfect for broadcasting to YouTube, Twitch, etc. simultaneously.

## Requirements 📋
- Python 3.x (source: python.org)
- FFmpeg installed (source: ffmpeg.org)

## Installation 🛠️
1. Clone this repo
2. Make sure FFmpeg is in your PATH
3. Edit `config.json` with your RTMP URLs

## Usage 🔥
```bash
python restream.py
```
It starts RTMP servers on specified ports, listens for input, and pushes to all outputs. Ctrl+C to stop.

## Configuration ⚙️
Edit `config.json`:
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
Add more servers for multiple streams.

## How it works 🧠
Uses FFmpeg in listen mode to receive RTMP input and copy streams to multiple outputs. Threads handle multiple servers. Source: FFmpeg documentation (ffmpeg.org)" 
