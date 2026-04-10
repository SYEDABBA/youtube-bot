import os
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
from gtts import gTTS

print("🔥 Bot started")

# 1. Script generate (simple demo)
script = "Top 3 facts about space. Number 1, space is completely silent."

# 2. Voice generate
tts = gTTS(script)
tts.save("voice.mp3")

# 3. Create text video
clip = TextClip(script, fontsize=50, color='white', size=(720,1280))
clip = clip.set_duration(10)

# 4. Add audio
audio = AudioFileClip("voice.mp3")
video = clip.set_audio(audio)

# 5. Export video
video.write_videofile("output.mp4", fps=24)

print("✅ Video created")

# 6. Upload (basic print for now)
print("🚀 Ready to upload:", os.path.exists("output.mp4"))
