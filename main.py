import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

from click import command

def search():
    print("button {}".format(search_text.get()))

def test_button(event: tk.Event):
    messagebox.showinfo("Перевод", event.widget.cget("text"))
    print(event.widget.cget("text"))

window = tk.Tk()
window.geometry("300x500")
window.title("Добро пожаловать в приложение PythonRu")

search_text = tk.StringVar()

#text = tk.Label(window, text="Поиск").grid(row=0)
input_text = tk.Entry(window, textvariable=search_text).grid(row=0, column=0)
button = tk.Button(window, text="Поиск", command=search).grid(row=0, column=1)

t = tk.Label(window, text="test")
t.grid(row=1, column=0)
t.bind("<Button-1>", test_button)
#b = tk.Button(window, text="GO")
#b.grid(row=2, column=1)
#b.bind("<Button-1>", test_button)

image = Image.open("./photos/test.png")
image.thumbnail((100, 100))
test_img = ImageTk.PhotoImage(image)
l_img = tk.Label(image=test_img)
l_img.grid(row=1, column=1)

window.mainloop()