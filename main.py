from gtts import gTTS
from moviepy.editor import AudioFileClip, ColorClip

print("🔥 Bot started")

# 1. Script
script = "Top 3 facts about space. Number 1, space is completely silent."

# 2. Voice generate
tts = gTTS(script)
tts.save("voice.mp3")

# 3. Audio load
audio = AudioFileClip("voice.mp3")

# 4. Simple background video (black screen)
video = ColorClip(size=(720,1280), color=(0,0,0), duration=audio.duration)
video = video.set_audio(audio)

# 5. Export
video.write_videofile("output.mp4", fps=24)

print("✅ Video created")
