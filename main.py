import os
import random
from moviepy import *
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import json

# ==============================
# LOAD TOKEN FROM GITHUB SECRET
# ==============================
token_json = os.environ.get("TOKEN_JSON")

if token_json:
    with open("token.json", "w") as f:
        f.write(token_json)

# ==============================
# YOUTUBE AUTH
# ==============================
with open("token.json") as f:
    creds_data = json.load(f)

youtube = build("youtube", "v3", credentials=None)

# ==============================
# SIMPLE AI SCRIPT (RANDOM TEXT)
# ==============================
scripts = [
    "Ek ladka tha jo kabhi haar nahi maanta tha...",
    "Zindagi ek safar hai, aur har din ek nayi kahani...",
    "Success ka raaz hai consistency aur hard work..."
]

script = random.choice(scripts)

# ==============================
# CREATE AUDIO (FAKE SHORT)
# ==============================
audio = AudioFileClip("sample.mp3") if os.path.exists("sample.mp3") else None

duration = audio.duration if audio else 5

# ==============================
# CREATE VIDEO
# ==============================
image = ImageClip("image.jpg").with_duration(duration)

if audio:
    video = image.with_audio(audio)
else:
    video = image

video = video.resized(height=1280)  # vertical
video.write_videofile("output.mp4", fps=24)

# ==============================
# UPLOAD TO YOUTUBE
# ==============================
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": script[:50],
            "description": script,
            "tags": ["AI", "shorts"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload("output.mp4")
)

response = request.execute()
print("✅ Uploaded:", response)
