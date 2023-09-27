import os

print("[*] Checking if assemblyai is installed.....")

try:
    import assemblyai as aai

    print("[*] Assemblyai is installed")
    print("[*] Running the program")

except ImportError:
    print("[*] Assemblyai is not installed")
    print("[*] Installing assemblyai")
    os.system("pip3 install assemblyai -q")
    print("[*] Assemblyai installed successfully")
    print("[*] Restarting the program")
    import assemblyai as aai

# replace with your API token
api_key = input("[*] Enter your API key: ")
aai.settings.api_key = f"{api_key}"

# URL of the file to transcribe
FILE_URL = input("[*] Enter the file path: ")

# Transcribe the file
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

# Formats the text
text = transcript.text
print("[*] Transcription complete")
file_name = input("[*] Enter the file name: ")
sentences = text.split(". ")
formatted_text = "\n".join(sentences)

# Saves the transcription to a file
with open(f"{file_name}.txt", "w") as f:
    f.write(formatted_text)

print(f"[*] Transcription saved to {file_name}.txt")
