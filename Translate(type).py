import tkinter as tk
from tkinter.font import Font
import pygame
import pyttsx3
import googletrans
# import speech_recognition as sr
# import gtts

root = tk.Tk()
root.iconbitmap(r'microphone_black_shape_f0H_icon.ico')
root.geometry('1000x600')
root.title("icon")

# translator
# rec = sr.Recognizer()
translator = googletrans.Translator()
input_lang = "en"
out_lang = "ta"

# font
myfont = Font(family="Courier New", size=25, slant="italic", weight="bold")

# pygame init
pygame.mixer.init()

def playSong():
    pygame.mixer.music.load("s1.mp3")
    pygame.mixer.music.play(loops=0)

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    myLab = tk.Label(text=my_entry.get(), font=myfont, fg="red")
    myLab.pack()
    # translator
    t = translator.translate(my_entry.get(), dest=out_lang)
    # print(t.text)
    myLab1 = tk.Label(text=t.text, font=myfont, fg="green")
    myLab1.pack()
    engine.say(my_entry.get())
    engine.runAndWait()


my_entry = tk.Entry(font=("Helvetica", 28))
my_entry.pack(pady=20)
my_entry.insert(0, "type something")


img = tk.PhotoImage(file="E:/My downloads/mic1.png")


B = tk.Button(text="Translate", command=talk, bg="#e00e70", fg="green", padx=50, font=myfont)
B.pack()


B["compound"] = tk.LEFT,
B["image"] = img
B.place(x=940, y=0)
root.mainloop()