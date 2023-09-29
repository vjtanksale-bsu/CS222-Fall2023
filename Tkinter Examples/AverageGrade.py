import tkinter as tk


def calculate():
    assignment = float(entry1.get())
    project = float(entry2.get())
    achievement = float(entry3.get())
    final = float(entry4.get())
    weightedAssignment =  assignment/100 * 0.2
    weightedProject =  project/100 * 0.7
    weightedAchievement = achievement/100 * 0.05
    weightedFinal = final/100 * 0.05

    lblResult["text"] = (weightedAssignment + weightedProject + weightedAchievement + weightedFinal) * 100


window = tk.Tk()
window.title("Average Grade Calculator")
lbl1 = tk.Label(window, text="Enter Assignment %")
entry1 = tk.Entry(window)
lbl2 = tk.Label(window, text="Enter Project %")
entry2 = tk.Entry(window)
lbl3 = tk.Label(window, text="Enter Achievement %")
entry3 = tk.Entry(window)
lbl4 = tk.Label(window, text="Enter Final Exam %")
entry4 = tk.Entry(window)
btnCalculate = tk.Button(window, text="Calculate Grade", command=calculate)
lbl5 = tk.Label(window, text="Answer %")
lblResult = tk.Label(window)
lbl1.grid(column=0, row=0)
entry1.grid(column=1, row=0)
lbl2.grid(column=0, row=1)
entry2.grid(column=1, row=1)
lbl3.grid(column=0, row=2)
entry3.grid(column=1, row=2)
lbl4.grid(column=0, row=3)
entry4.grid(column=1, row=3)
lbl5.grid(column=0, row=4)
lblResult.grid(column=1, row=4)
btnCalculate.grid(column=0, row=5)

window.mainloop()
