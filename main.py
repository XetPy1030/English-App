import tkinter as tk
from tkinter import messagebox

import pandas as pd
from PIL import Image, ImageTk
import os

def convert(filename: str) -> list:
    excel = pd.read_excel(filename).to_dict()
    keys = [i for i in excel]
    nums_keys = len(keys)
    nums = len(excel[keys[0]])
    words = []
    for i in range(nums):
        word = {}
        for o in range(nums_keys):
            word[keys[o]] = str(excel[keys[o]][i])
        words.append(word)
    return words

words = convert("words.xlsx")

def click_word(event: tk.Event):
    pass

def set_words(words: list, window: tk.Tk, start_row: int = 2):
    for i in range(len(words)):
        text = tk.Label(window, text=words[i]["Word"])
        text.grid(row=start_row+i, column=0)
        text.bind("<Button-1>", click_word)

        if words[i]["Image"] != "nan":
            try:
                image = Image.open("./photos/{}".format(words[i]["Image"]))
                image.thumbnail((100, 100))
                test_img = ImageTk.PhotoImage(image)
                l_img = tk.Label(image=test_img)
                l_img.grid(row=start_row+i, column=1)
            except:
                pass

def search():
    print("button {}".format(search_text.get()))

def test_button(event: tk.Event):
    messagebox.showinfo("Перевод", event.widget.cget("text"))
    print(event.widget.cget("text"))

window = tk.Tk()
window.geometry("400x500")
window.title("Словарь")

search_text = tk.StringVar()

#text = tk.Label(window, text="Поиск").grid(row=0)
input_text = tk.Entry(window, textvariable=search_text).grid(row=0, column=0)
button = tk.Button(window, text="Поиск", command=search).grid(row=0, column=1)

set_words(words, window)

"""t = tk.Label(window, text="test")
t.grid(row=1, column=0)
t.bind("<Button-1>", test_button)
#b = tk.Button(window, text="GO")
#b.grid(row=2, column=1)
#b.bind("<Button-1>", test_button)

image = Image.open("./photos/test.png")
image.thumbnail((100, 100))
test_img = ImageTk.PhotoImage(image)
l_img = tk.Label(image=test_img)
l_img.grid(row=1, column=1)"""

window.mainloop()