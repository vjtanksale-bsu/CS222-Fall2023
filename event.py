import tkinter as tk
window = tk.Tk()
window.title("Second Python GUI")
window.geometry('500x300')
lbl = tk.Label(window, text="Ok")
lbl.grid(column=0, row=0)
txt = tk.Entry(window, width=10)
txt.grid(column=1, row=0)
def clicked():
    result = "Welcome " + txt.get()
    lbl.configure(text=result)
btn = tk.Button(window, text="Welcome", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()