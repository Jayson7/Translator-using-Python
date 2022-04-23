from tkinter import *
# build language translator using tkinter and googletrans
from googletrans import Translator
import textblob  
from tkinter import ttk, messagebox 
root = Tk()
root.title("Google Translator - Jayson")
root.geometry("800x400")
root.maxsize('800','400')

# Text boxes 

def translate_it():

    pass

def language_list():
    
    pass

def  clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)
    

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

translated_combo = ttk.Combobox(root, width=30, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=2, column=2)


# clear button 
clear_button = Button(root, tetx='clear', command=clear)
clear_button.grid(row=2, column=1)



root.mainloop()

