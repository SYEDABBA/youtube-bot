from gtts import gTTS

print("Bot started 🔥")

text = "AI is growing faster than humans 😱"

tts = gTTS(text)
tts.save("voice.mp3")

print("Voice created ✅")
