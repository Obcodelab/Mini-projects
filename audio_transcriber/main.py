import logging
import os

# Set up logging
logging.basicConfig(filename="transcription.log", level=logging.INFO)

# Checks if assemblyai is installed
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

try:
    # Create a new TranscriptionConfig
    config = aai.TranscriptionConfig(language_detection=True)

    # Transcribe the file
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(FILE_URL)

    # Checks for errors
    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")

    # Formats the text
    text = transcript.text
    print("[*] Transcription complete")
    sentences = transcript.get_sentences()
    formatted_sentences = []
    for sentence in sentences:
        formatted_text = sentence.text
        formatted_sentences.append(formatted_text)

    # Saves the transcription to a file
    with open("FILE_NAME.txt", "w") as f:
        f.write(formatted_text + "\n")
        print("[*] Transcription complete")

    print("[*] Transcription saved to FILE_NAME.txt")

except Exception as e:
    print(f"Transcription failed: {e}")
    logging.error("Error during transcription", exc_info=True)
