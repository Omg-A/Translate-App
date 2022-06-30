from tkinter import *
from tkinter import ttk
from googletrans import Translator

root = Tk()
root.title("Language Translater App")
root.geometry("1000x400")
root.configure(background="#59b7ff")

label_title = Label(root, text="Language Translater App", font=("Verdana", 20), fg="white", bg="#59b7ff")
label_title.place(relx=0.5, rely=0.1, anchor=CENTER)

label_input = Label(root, text="Enter Text", font=("Arial", 10, "bold"), bg="#59b7ff")
label_input.place(relx=0.06, rely=0.35, anchor=CENTER)

text_input = Text(root, height=10, width=50, wrap=WORD)
text_input.place(relx=0.23, rely=0.6, anchor=CENTER)

language = list(LANGUAGES.values())
print(language)

root.mainloop()