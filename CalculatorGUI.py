import tkinter as tk
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    lblResult["text"] = num1 + num2

window = tk.Tk()
window.title("Calculator")
lbl1 = tk.Label(window, text="Enter the first number")
entry1 = tk.Entry(window)
lbl2 = tk.Label(window, text="Enter the second number")
entry2 = tk.Entry(window)
btnCalculate = tk.Button(window, text="Calculate", command=calculate)
lblResult = tk.Label(window)
lbl1.grid(column=0, row=0)
entry1.grid(column=1, row=0)
lbl2.grid(column=0, row=1)
entry2.grid(column=1, row=1)
btnCalculate.grid(column=0, row=2)
lblResult.grid(column=2, row=2)
window.mainloop()