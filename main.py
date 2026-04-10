import os
import requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# 🔐 Secrets
with open("token.json", "w") as f:
    f.write(os.environ["TOKEN_JSON"])

with open("client_secret.json", "w") as f:
    f.write(os.environ["CLIENT_SECRET"])

# 🎥 Download sample video
video_url = "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"
video_file = "video.mp4"

r = requests.get(video_url)
with open(video_file, "wb") as f:
    f.write(r.content)

# 🔑 Auth
creds = Credentials.from_authorized_user_file("token.json")
youtube = build("youtube", "v3", credentials=creds)

# 📤 Upload
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "🔥 Auto Upload Test",
            "description": "Bot working 😈",
            "tags": ["shorts"],
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
