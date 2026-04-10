import os
import json
import random
from moviepy import ImageClip, AudioFileClip
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# ==============================
# LOAD TOKEN FROM GITHUB SECRET
# ==============================
token_json = os.environ.get("TOKEN_JSON")

if token_json:
    with open("token.json", "w") as f:
        f.write(token_json)

# ==============================
# YOUTUBE AUTH (FIXED)
# ==============================
creds = Credentials.from_authorized_user_file("token.json")
youtube = build("youtube", "v3", credentials=creds)

# ==============================
# SIMPLE SCRIPT GENERATOR
# ==============================
scripts = [
    "Ek ladka tha jo kabhi haar nahi maanta tha...",
    "Zindagi ek safar hai, har din ek nayi kahani...",
    "Success ka raaz hai consistency aur hard work..."
]

script = random.choice(scripts)

# ==============================
# AUDIO (OPTIONAL)
# ==============================
if os.path.exists("sample.mp3"):
    audio = AudioFileClip("sample.mp3")
    duration = audio.duration
else:
    audio = None
    duration = 5

# ==============================
# VIDEO CREATE (FIXED)
# ==============================
image = ImageClip("image.jpg").with_duration(duration)

if audio:
    video = image.with_audio(audio)
else:
    video = image

video = video.resized(height=1280)
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
