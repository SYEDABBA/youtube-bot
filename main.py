from gtts import gTTS
import os

print("Bot started 🔥")

# Step 1: Text
text = "AI will replace many jobs in future 😱"

# Step 2: Voice
tts = gTTS(text)
tts.save("voice.mp3")

print("Voice created ✅")

# Step 3: Create video using ffmpeg
os.system(
    "ffmpeg -f lavfi -i color=c=black:s=720x1280:d=10 "
    "-i voice.mp3 -vf \"drawtext=text='AI FACT 😱':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=(h-text_h)/2\" "
    "-shortest -y output.mp4"
)

print("Video created 🎬")
