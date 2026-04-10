import os
import json
import random
import requests
from gtts import gTTS
from moviepy import *
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

print("🚀 STARTING AI BOT...")

# ==============================
# LOAD TOKEN
# ==============================
token_json = os.environ.get("TOKEN_JSON")

if not token_json:
    raise Exception("❌ TOKEN_JSON missing")

with open("token.json", "w") as f:
    f.write(token_json)

# ==============================
# YOUTUBE AUTH
# ==============================
creds = Credentials.from_authorized_user_file("token.json")
youtube = build("youtube", "v3", credentials=creds)

print("✅ YouTube Connected")

# ==============================
# AI SCRIPT (HOOK BASED)
# ==============================
scripts = [
    "99% log ye galti karte hai jo unki life barbaad kar deti hai...",
    "Agar tum successful banna chahte ho to ye ek rule follow karo...",
    "Ye secret tumhe koi nahi batayega, par aaj main bataunga...",
    "Har din ye ek habit follow karo aur life change ho jayegi..."
]

script = random.choice(scripts)

# ==============================
# TEXT TO SPEECH (AI VOICE)
# ==============================
print("🎤 Generating voice...")
tts = gTTS(script)
tts.save("voice.mp3")

audio = AudioFileClip("voice.mp3")
duration = audio.duration

# ==============================
# AUTO IMAGE DOWNLOAD
# ==============================
if not os.path.exists("image.jpg"):
    img_url = "https://picsum.photos/720/1280"
    img = requests.get(img_url).content
    with open("image.jpg", "wb") as f:
        f.write(img)

# ==============================
# VIDEO CREATE
# ==============================
print("🎬 Creating video...")

image = ImageClip("image.jpg").with_duration(duration)

# TEXT SUBTITLE
txt = TextClip(
    script,
    font_size=60,
    color="white",
    size=(700, None),
    method="caption"
).with_position(("center", "bottom")).with_duration(duration)

video = CompositeVideoClip([image, txt]).with_audio(audio)

video = video.resized(height=1280)

video.write_videofile(
    "output.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

print("✅ Video Ready")

# ==============================
# UPLOAD
# ==============================
print("📤 Uploading...")

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": script[:60],
            "description": script,
            "tags": ["motivation", "shorts", "ai"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload("output.mp4")
)

response = request.execute()

print("🔥 SYSTEM ONLINE 😈")
print("✅ Uploaded:", response.get("id"))
