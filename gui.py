import tkinter as tk
window = tk.Tk()
hello = tk.Label(text="Hello World")
welcome = tk.Label(text="Welcome to CS 222", foreground="white", background="black")
clickMe = tk.Button(text="Ok",width=10,height=3)
hello.pack()
welcome.pack()
clickMe.pack()
window.mainloop()