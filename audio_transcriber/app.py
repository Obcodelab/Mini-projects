import os

print("[*] Checking if assemblyai and customtkinter is installed.....")

try:
    import assemblyai as aai
    import customtkinter as Ctk
    from customtkinter import filedialog

    print("[*] Assemblyai and Customtkinter are installed")
    print("[*] Running the program")

except ImportError as e:
    missing_module = str(e).split()[-1].strip("'")

    if missing_module.lower() == "assemblyai":
        print("[*] Assemblyai is not installed")
        print("[*] Installing assemblyai")
        os.system("pip3 install assemblyai -q")
        print("[*] Assemblyai installed successfully")

    elif missing_module.lower() == "customtkinter":
        print("[*] Customtkinter is not installed")
        print("[*] Installing customtkinter")
        os.system("pip3 install customtkinter -q")
        print("[*] Customtkinter installed successfully")

    else:
        print("[*] Assemblyai and Customtkinter are not installed")
        print("[*] Installing Assemblyai and Customtkinter")
        os.system("pip3 install assemblyai -q")
        os.system("pip3 install customtkinter -q")
        print("[*] Assemblyai and Customtkinter installed successfully")

    print("[*] Restarting the program")

    import assemblyai as aai
    import customtkinter as Ctk
    from customtkinter import filedialog

root = Ctk.CTk()
root.title("Audio Transcriber")
Ctk.set_appearance_mode("dark")
counter = 0

for i in range(0, 4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


def browse(event=None):
    file_path = filedialog.askopenfilename()
    if file_path:
        url_entry.delete(0, "end")
        url_entry.insert(0, file_path)


def transcribe(event=None):
    global counter
    counter += 1
    transcription = Ctk.CTkLabel(root, text="")
    transcription.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
    api_key = api_key_entry.get()
    aai.settings.api_key = f"{api_key}"
    FILE_URL = url_entry.get()
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)
    text = transcript.text
    if text is not None:
        sentences = text.split(". ")
        formatted_text = "\n".join(sentences)
        with open("transcript.txt", "w") as f:
            f.write(formatted_text)
        if counter <= 1:
            transcription.configure(text="Transcription saved to txt file 1 time")
        elif counter > 1:
            transcription.configure(
                text=f"Transcription saved to txt file {counter} times"
            )


api_key_label = Ctk.CTkLabel(root, text="API Key : ")
api_key_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

api_key_entry = Ctk.CTkEntry(root, width=300)
api_key_entry.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

url_label = Ctk.CTkLabel(root, text="URL : ")
url_label.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

url_entry = Ctk.CTkEntry(root, width=300)
url_entry.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

browse_button = Ctk.CTkButton(root, text="Browse files", command=browse)
browse_button.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

transcribe_button = Ctk.CTkButton(root, text="Transcribe", command=transcribe)
transcribe_button.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

root.bind("<Return>", transcribe)
root.mainloop()
