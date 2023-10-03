import os

print("[*] Checking for customtkinter module...")

try:
    from customtkinter import *

    print("[*] customtkinter module found")

except ModuleNotFoundError:
    print("[*] customtkinter module not found")
    os.system("pip install customtkinter -q")
    print("[*] customtkinter module installed")
    print("[*] Restarting the program")
    from customtkinter import *

root = CTk()
root.title("Decimal to Binary Converter")
set_appearance_mode("dark")
set_default_color_theme("blue")


def convert(event=None):
    value = decimalInput.get()
    if value.isdigit():
        value = int(value)
        binaryInput.delete(0, "end")
        binaryInput.insert(0, bin(value)[2:])

    else:
        binaryInput.delete(0, "end")
        binaryInput.insert(0, "Invalid Input")


for i in range(3):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

decimal = CTkLabel(root, text="Decimal : ")
decimal.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

decimalInput = CTkEntry(root, width=150)
decimalInput.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

binary = CTkLabel(root, text="Binary : ")
binary.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

binaryInput = CTkEntry(root, width=150)
binaryInput.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

calculate = CTkButton(root, text="Calculate", command=convert)
calculate.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

root.bind("<Return>", convert)
root.mainloop()
