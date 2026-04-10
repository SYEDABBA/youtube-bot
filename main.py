import os
import datetime
from gtts import gTTS
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# ================= CONFIG =================
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

VIDEO_TITLE = "Amazing AI Fact 🤯"
VIDEO_DESC = "Subscribe for more 🔥 #shorts"
CATEGORY_ID = "28"  # Science & Tech

# ==========================================

def generate_script():
    return "AI can learn faster than humans in some cases 🤯"

def create_voice(script):
    tts = gTTS(script)
    tts.save("voice.mp3")

def create_video(script):
    txt_clip = TextClip(script, fontsize=60, color='white', size=(720,1280))
    txt_clip = txt_clip.set_duration(10)

    audio = AudioFileClip("voice.mp3")
    video = txt_clip.set_audio(audio)

    video.write_videofile("output.mp4", fps=24)

def upload_video():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION)

    request_body = {
        "snippet": {
            "title": VIDEO_TITLE,
            "description": VIDEO_DESC,
            "categoryId": CATEGORY_ID
        },
        "status": {
            "privacyStatus": "private",
            "publishAt": (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat("T") + "Z"
        }
    }

    media = MediaFileUpload("output.mp4")

    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = request.execute()
    print("Uploaded:", response)

# ================= RUN =================

if __name__ == "__main__":
    script = generate_script()
    create_voice(script)
    create_video(script)
    upload_video()
