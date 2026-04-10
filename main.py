from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
import os

print("Bot started 🔥")

# Check files exist
if not os.path.exists("output.mp4"):
    raise Exception("❌ output.mp4 not found")

if not os.path.exists("token.json"):
    raise Exception("❌ token.json not found")

# Load credentials
creds = Credentials.from_authorized_user_file("token.json")

youtube = build("youtube", "v3", credentials=creds)

print("Uploading शुरू 🚀")

# Upload video
request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "AI Fact 😱",
            "description": "Auto uploaded by bot 🔥 #shorts",
            "tags": ["ai", "shorts", "facts"],
            "categoryId": "28"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload("output.mp4")
)

response = request.execute()

print("✅ Uploaded Successfully")
print(response)
