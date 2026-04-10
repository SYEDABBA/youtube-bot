import os
import json
import random
import requests
from moviepy import ImageClip, AudioFileClip
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

print("🚀 STARTING BOT...")

# ==============================
# TOKEN LOAD
# ==============================
token_json = os.environ.get("TOKEN_JSON")

if not token_json:
    raise Exception("❌ TOKEN_JSON missing in secrets")

with open("token.json", "w") as f:
    f.write(token_json)

# ==============================
# YOUTUBE AUTH
# ==============================
creds = Credentials.from_authorized_user_file("token.json")
youtube = build("youtube", "v3", credentials=creds)

print("✅ YouTube Auth Done")

# ==============================
# AUTO DOWNLOAD IMAGE
# ==============================
if not os.path.exists("image.jpg"):
    print("⬇️ Downloading image...")
    img_url = "https://picsum.photos/720/1280"
    img_data = requests.get(img_url).content
    with open("image.jpg", "wb") as f:
        f.write(img_data)

# ==============================
# SCRIPT GENERATOR
# ==============================
scripts = [
    "Zindagi badalne ka time aa gaya hai!",
    "Success chahiye? Aaj se start karo!",
    "Har din ek nayi opportunity hoti hai!"
]

script = random.choice(scripts)

# ==============================
# AUDIO (OPTIONAL)
# ==============================
audio = None
duration = 5

if os.path.exists("sample.mp3"):
    try:
        audio = AudioFileClip("sample.mp3")
        duration = audio.duration
    except:
        print("⚠️ Audio load failed, skipping")

# ==============================
# VIDEO CREATE
# ==============================
print("🎬 Creating video...")

image = ImageClip("image.jpg").with_duration(duration)

if audio:
    video = image.with_audio(audio)
else:
    video = image

video = video.resized(height=1280)

video.write_videofile(
    "output.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

print("✅ Video Created")

# ==============================
# UPLOAD TO YOUTUBE
# ==============================
print("📤 Uploading...")

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": script[:50],
            "description": script,
            "tags": ["AI", "shorts", "motivation"],
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
