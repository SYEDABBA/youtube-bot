import os
import random
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# 🔐 Secrets se files bana
with open("token.json", "w") as f:
    f.write(os.environ["TOKEN_JSON"])

with open("client_secret.json", "w") as f:
    f.write(os.environ["CLIENT_SECRET"])

# 🎥 YouTube Auth
creds = Credentials.from_authorized_user_file("token.json")
youtube = build("youtube", "v3", credentials=creds)

# 🎬 Dummy video create (simple text video)
video_file = "video.mp4"

# Agar video nahi hai toh dummy file banayega
if not os.path.exists(video_file):
    with open(video_file, "wb") as f:
        f.write(os.urandom(1024 * 100))  # random 100kb file

# 📝 Random title
titles = [
    "🔥 Amazing Fact You Didn't Know!",
    "😱 Shocking Truth Revealed!",
    "🚀 वायरल होने वाला वीडियो!",
    "💡 Life Changing Hack!"
]

title = random.choice(titles)

# 📤 Upload
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": title,
            "description": "Auto uploaded by bot 😈",
            "tags": ["shorts", "viral"],
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload(video_file)
)

response = request.execute()

print("✅ Uploaded:", response["id"])
