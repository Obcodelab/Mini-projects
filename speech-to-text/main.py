import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Loads audio file (audio file can be in format wav, aiff and flac)
with sr.AudioFile("audio_file.wav") as source:
    audio = r.record(source)

# Convert speech to text
text = r.recognize_google(audio)
print(text)
