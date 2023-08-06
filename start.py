import tkinter as tk
from cmd_1 import start_command_os, start_command_sub

def cmd_start():
    rep = start_command_sub(entr1.get())
    text.insert("0.0", rep + "\n")
    

window = tk.Tk()

window.geometry("400x600")

label1 = tk.Label(window, text="Write command")
label1.pack(pady=10)
entr1 = tk.Entry(window)
entr1.pack(pady=10)

butt = tk.Button(window, text="enter command", command=cmd_start)
butt.pack(pady=10)

text = tk.Text(window, bg="gray", fg="white")
text.pack()

window.mainloop()
