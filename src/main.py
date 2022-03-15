import speech_recognition as s_r
import gtts
# from translate import Translator
from langdetect import detect
from playsound import playsound
from googletrans import Translator
# from pytesseract import image_to_string
from PIL import Image
import pytesseract

img = Image.open('G:/PPT/2 - 2/AI DS/Project/Code-Mixing Translation DataSet/Image Dataset/text2.jpg')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text3 = pytesseract.image_to_string(img)
with open('abc.txt', mode='w') as file:
    file.write(text3)
    print(text3)
# write text in a text file and save it to source path
print(detect(text3))
if detect(text3) == 'te':
  translator = Translator()
  translation = translator.translate(text3, src='te', dest='en')
  print(translation.text)
  translator1 = Translator()
  translation1 = translator1.translate(translation.text, src='en', dest='hi')
  print(translation1.text)
  # make request to google to get synthesis
  tts = gtts.gTTS(translation1.text, lang="hi")
  # save the audio file
  tts.save("my-translation.mp3")
  # play the audio file
  playsound("my-translation.mp3")
elif detect(text3) != 'te':
  translator = Translator()
  translation = translator.translate(text3, src='en', dest='te')
  print(translation.text)
  translator1 = Translator()
  translation1 = translator1.translate(translation.text, src='te', dest='hi')
  print(translation1.text)
  # make request to google to get synthesis
  tts = gtts.gTTS(translation1.text, lang="hi")
  # save the audio file
  tts.save("my-translation.mp3")
  # play the audio file
  playsound("my-translation.mp3")
else:
  print("Try again")
  exit()
