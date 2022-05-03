import tkinter as tk
from tkinter import Listbox, messagebox

import pandas as pd
from PIL import Image, ImageTk
import config

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

all_words = convert("words.xlsx")
words = all_words

def click_word(event: tk.Event):
    newWindow = tk.Toplevel(window)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

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

def search_click():
    global search_text, all_words, set_words_list, window

    text = search_text.get()

    if not text:
        return

    new_words = search(text, all_words)

    set_words_list(new_words, window)

def search(search_text: str, words: list):
    searched_word = []
    search_text = search_text.lower()

    for i in words:
        for o in config.search_in:
            if search_text in i[o].lower():
                searched_word.append(i)
    
    return searched_word

def test_button(event: tk.Event):
    messagebox.showinfo("Перевод", event.widget.cget("text"))
    print(event.widget.cget("text"))

def select_word(event: tk.Event):
    global newWindow, newWindowText

    newWindow.deiconify()

    word = my_list.get(tk.ANCHOR)
    info = get_info_from_word(word, words)

    newWindowText.set(config.info.format(word=info["Word"], translate=info["Translate"], other=info["Other"].replace("nan", config.not_found)))

def get_info_from_word(word: str, words: list):
    for i in words:
        if i["Word"] == word:
            return i
    return None

window = tk.Tk()
window.geometry(config.app_size)
window.title(config.app_name)

search_text = tk.StringVar()

input_text = tk.Entry(window, textvariable=search_text).grid(row=0, column=0)
button = tk.Button(window, text=config.button_search, command=search_click).grid(row=0, column=1)

my_list = Listbox(window, width=40)
my_list.grid(row=1, column=0)
my_list.bind('<<ListboxSelect>>', select_word)

def set_words_list(words: list, window: tk.Tk):
    global my_list

    my_list.delete(0, tk.END)

    for i in range(len(words)):
        my_list.insert(i+1, words[i]["Word"])

set_words_list(words, window)

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

def closeNewWindow():
    global newWindow
    newWindow.withdraw()

newWindow = tk.Toplevel(window)
newWindow.protocol("WM_DELETE_WINDOW", closeNewWindow)
newWindowText = tk.StringVar()
newWindowLabel = tk.Label(newWindow, textvariable=newWindowText)
newWindowLabel.pack()

window.mainloop()