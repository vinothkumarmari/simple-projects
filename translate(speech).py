import googletrans
import speech_recognition as sr
import gtts
import playsound

# print(googletrans.LANGUAGES)

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = "en"
out_lang = "ta"

try:
    with sr.Microphone() as source:
        print('speak now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

t = translator.translate(text, dest=out_lang)
print(t.text)
converted_aud = gtts.gTTS(t.text, lang=out_lang)
converted_aud.save("s1.mp3")
playsound.playsound("s1.mp3")