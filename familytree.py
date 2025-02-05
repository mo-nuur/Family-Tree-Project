#learning tkinter

import tkinter as tk

root = tk.Tk()

root.geometry("500x500")

root.title("My First GUI")

label = tk.Label(root, text="Hello World!", font = ('Arial', 18))
label.pack(padx = 20, pady = 20)

textbox = tk.Text(root, height = 3, font = ('Arial', 16))
textbox.pack()

myentry = tk.Entry(root, font = ('Arial', 16) )
myentry.pack()

button = tk.Button(root, text = 'click me!' ,font = ('Arial', 16))
button.pack(padx = 10, pady = 10)

root.mainloop()
