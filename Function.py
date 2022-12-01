from gtts import gTTS
import os
text = "Sometimes to search is good, there are times you must believe and not search, in both cases you need to function"
tts = gTTS(text)
tts.save("hi.mp3")
os.system("hi.mp3")
