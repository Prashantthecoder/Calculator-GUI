import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text=result)
    except:
        output.config(text="Error")

root = tk.Tk()
root.title("Smart Calculator")

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Calculate", command=calculate)
button.pack()

output = tk.Label(root, text="")
output.pack()

root.mainloop()
