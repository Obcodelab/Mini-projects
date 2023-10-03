# Audio Transcriber

This program transcribes an audio file and saves it in a txt file using assemblyai

## How to use terminal v1 `main.py`

- Replace API_KEY_HERE with your assembly api token which you can get at [AssemblyAI](https://www.assemblyai.com) after signing up for free.
- Change FILE_PATH_HERE to either be:
  - a local path to an audio file as regards to your os (`./my-audio.mp3`) or
  - a web url (`https://example.org/audio.mp3`)
- Change FILE_NAME to any name of your choice
- Run on terminal with `python main.py`
- Your transcript should be saved in a text file

## How to use terminal v2 `main2.py`

- Run on terminal with `python main2.py`
- Enter api_key
- Enter file path to either be:
  - a local path to an audio file as regards to your os (`C:\path_to_file`) or
  - a web url (`https://example.org/audio.mp3`)
- Wait till transcription is completed then enter file name (`transcript`)
- Your transcript should be saved in a text file (`transcript.txt`)

## How to use gui version `app.py`

- Run on terminal with `python app.py`
- Input your api key and file url
- You can either:
  - Paste a web url (`https://example.org/audio.mp3`) or
  - Click on the browse files button to select a local file
- Click on transcribe then wait for some time
- Your transcript should be saved in a text file (`transcript.txt`)

## Notes

- Time taken for the program to run depends on the duration of the audio file
- Check out [FAQ](https://www.assemblyai.com/docs/Concepts/faq) for audio file formats and api limits
- Check out [CONCEPTS](https://www.assemblyai.com/docs/models/speech-recognition#automatic-language-detection) for more info on automatic language detection supported languages
