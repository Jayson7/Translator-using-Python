from tkinter import *
# build language translator using tkinter and googletrans
from googletrans import Translator
import textblob  
from tkinter import ttk, messagebox 
root = Tk()
root.title("Google Translator - Jayson")
root.geometry("800x400")
root.maxsize('800','400')

def translate_it():

    pass

# Text boxes 
original_text = Text(root, width=30, height=20)
original_text.grid(row=0, column=0, padx=20, pady=10) 

translated_button = Button(root, text="Translate!", font=("cursive", 24 ), command=translate_it  )
translated_button.grid(row=0, column=1, padx=20)


translated_text = Text(root, width=30, height=20)
translated_text.grid(row=0, column=2, padx=20, pady=10) 

# combo boxes 
original_combo = ttk.Combobox(root, width=30, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translate_combo = ttk.Combobox(root, width=30, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)



root.mainloop()

