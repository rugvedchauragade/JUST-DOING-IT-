from gtts import gTTS

text = input("What do you want me to say? ")

tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

print("Audio saved successfully")

 

