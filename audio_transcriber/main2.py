import os
import logging

# Set up logging
logging.basicConfig(filename='transcription.log', level=logging.INFO)

def install_assemblyai():
    print("[*] Assemblyai is not installed")
    print("[*] Installing assemblyai")
    os.system("pip3 install assemblyai -q")
    print("[*] Assemblyai installed successfully")
    print("[*] Restarting the program")
    import assemblyai as aai

    return aai

try:
    import assemblyai as aai
except ImportError:
    aai = install_assemblyai()

# Replace with your API token
api_key = input("[*] Enter your API key: ")

# Validate API key format
if not api_key or len(api_key) != 64:
    print("[*] Invalid API key format")
    exit(1)

aai.settings.api_key = api_key

# URL of the file to transcribe
FILE_URL = input("[*] Enter the file path: ")

# Validate file URL format (you can add more validation logic here)
if not FILE_URL.startswith("http"):
    print("[*] Invalid file URL format")
    exit(1)

try:
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
    logging.info(f"Transcription saved to {file_name}.txt")
except Exception as e:
    print("[*] An error occurred during transcription:")
    print(str(e))
    logging.error("Error during transcription:", exc_info=True)
