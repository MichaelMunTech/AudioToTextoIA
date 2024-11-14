# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "ec5d090ff0174f81892ef70facbee01d"
transcriber = aai.Transcriber()

#transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
transcript = transcriber.transcribe("/Users/michaelmunoz/Downloads/motivo1.mp4")

print(transcript.text)