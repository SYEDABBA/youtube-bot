from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

print("Uploading शुरू 🔥")

creds = Credentials.from_authorized_user_file("token.json")

youtube = build("youtube", "v3", credentials=creds)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "AI Fact 😱",
            "description": "Auto uploaded 🚀",
            "tags": ["ai", "shorts"],
            "categoryId": "28"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload("output.mp4")
)

response = request.execute()
print("Uploaded ✅", response)
