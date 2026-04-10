import os
import requests
from gtts import gTTS
from moviepy.editor import *

# 🔐 Secrets
API_KEY = os.environ["GROQ_API_KEY"]

# 🧠 AI Script (simple)
topic = "Motivation"

script = f"{topic} is the key to success. Never give up. Keep pushing forward."

# 🎙️ Voice generate
tts = gTTS(script)
tts.save("voice.mp3")

# 🖼️ Image download
img_url = "https://picsum.photos/720/1280"
img_data = requests.get(img_url).content

with open("image.jpg", "wb") as f:
    f.write(img_data)

# 🎬 Create video
audio = AudioFileClip("voice.mp3")
image = ImageClip("image.jpg").set_duration(audio.duration)

video = image.set_audio(audio)
video.write_videofile("video.mp4", fps=24)

print("✅ AI Video Created")
