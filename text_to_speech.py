
from gtts import gTTS
import os


text = str(input("Please enter the text you want to convert to an audio file: "))

text_to_voice = gTTS(text=text, lang="en")
text_to_voice.save('voice.mp3')

os.system('voice.mp3')
