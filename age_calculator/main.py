# Imports required module
from datetime import datetime
from tkinter import *

# Gets year
current_year = datetime.now().year


# Calculates age
def calculate():
    dob = dateInput.get()
    if dob.isdigit():
        dob = int(dob)
        age = current_year - dob
        result.configure(text=age)
    else:
        result.configure(text="Please enter a integer value")


# Calls dateBtn
def on_enter_key(event):
    dateBtn.invoke()


# Creates a window
root = Tk()
root.title("Age Calculator")
root.geometry("300x100")

# Enter Key bind
root.bind("<Return>", on_enter_key)

# Year Label
date = Label(root, text="Year of birth : ")
date.grid(row=0, column=0, padx=5, pady=5)

# Year Entry
dateInput = Entry(root, width=20)
dateInput.grid(row=0, column=1, padx=5, pady=5)

# Calculate Button
dateBtn = Button(root, text="Calculate", width=8, command=calculate)
dateBtn.grid(row=2, column=1)

# Age Label
resultLabel = Label(root, text="Age : ")
resultLabel.grid(row=1, column=0, padx=5, pady=5)

# Age
result = Label(root, text="")
result.grid(row=1, column=1, padx=5, pady=5)

# Initializes the program
root.mainloop()
