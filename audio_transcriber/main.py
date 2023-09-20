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
aai.settings.api_key = f"API_KEY_HERE"

# URL of the file to transcribe
FILE_URL = "FILE_PATH_HERE"

# Transcribe the file
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

# Formats the text
text = transcript.text
sentences = text.split(". ")
formatted_text = "\n".join(sentences)

# Saves the transcription to a file
with open("FILE_NAME.txt", "w") as f:
    f.write(formatted_text)
    print("[*] Transcription complete")

print("[*] Transcription saved to transcript.txt")
