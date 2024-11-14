import streamlit as st
import assemblyai as aai
import os
from moviepy.editor import VideoFileClip


os.environ["ASSEMBLYAI_API_KEY"] = "ec5d090ff0174f81892ef70facbee01d"

apykey= os.environ["ASSEMBLYAI_API_KEY"]

st.title("Procesador de archivos de Audio/Video")
aai.settings.api_key = apykey

#config = aai.TranscriptionConfig(language_detection=True)

file_url = st.text_input("Ingresa la URL del archivo de audio o video")

config = aai.TranscriptionConfig(speaker_labels=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  file_url,
  config=config
)



# Selección de tipo de entrada
input_type = st.selectbox("Selecciona el tipo de entrada", ["Local", "URL"])

for utterance in transcript.utterances:
  print(f"---Speaker {utterance.speaker}: {utterance.text}")



def processFile(url_file):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_url)

    if transcript.status == aai.TranscriptStatus.error:
        st.write(transcript.error)
    else:
        st.write(transcript.text)

if st.button("Process") and file_url:
    if input_type == "URL":
        try:
            processFile(file_url)
        except Exception as e:
            st.error(f"Error al procesar el archivo desde la URL: {e}")

    else:
        #video = VideoFileClip(file_url)
        try:
            print(file_url)
            processFile(file_url)
        except Exception as e:
            st.error(f"Error al procesar el archivo desde la Local: {e}")


