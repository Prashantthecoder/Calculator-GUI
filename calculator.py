import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget to display results
        self.entry = tk.Entry(master, width=30, justify="right", font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

        # create buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # create and place the buttons on the grid
        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, font=("Arial", 12), width=5, height=2,
                               command=lambda text=button_text: self.handle_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # create the "C" button
        clear_button = tk.Button(master, text="C", font=("Arial", 12), width=5, height=2,
                                 command=self.clear_entry)
        clear_button.grid(row=5, column=0, padx=5, pady=5)

    def handle_click(self, text):
        if text == "=":
            # calculate the result and display it
            try:
                result = str(eval(self.entry.get()))
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        else:
            # append the clicked text to the entry widget
            self.entry.insert(tk.END, text)

    def clear_entry(self):
        # clear the entry widget
        self.entry.delete(0, tk.END)

root = tk.Tk()
app = Calculator(root)
root.resizable(False,False)
root.mainloop()
