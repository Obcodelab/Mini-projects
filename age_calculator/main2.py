#Imports required module
from customtkinter import *
from datetime import datetime

#Gets year
current_year = datetime.now().year

#Calculates age
def calculate():
    dob = dateInput.get()
    if dob.isdigit():
        dob = int(dob)
        age = current_year - dob
        result.configure(text = age)
    else:
        result.configure(text = 'Please enter a integer value')

#Creates a window
root = CTk()
root.title('Age Calculator')
root.geometry('300x100')

#Year Label
date = CTkLabel(root, text="Year of birth : ")
date.grid(row=0, column=0, padx=5)

#Year Entry
dateInput = CTkEntry(root, width=150)
dateInput.grid(row=0, column=1, padx=5)

#Calculate Button
dateBtn = CTkButton(root, text="Calculate", width=50,command=calculate)
dateBtn.grid(row=2, column=1)

#Age Label
resultLabel = CTkLabel(root, text="Age : ")
resultLabel.grid(row=1,column=0, padx=5)

#Age
result = CTkLabel(root, text="")
result.grid(row=1, column=1, padx=5)

#Initializes the program
root.mainloop()