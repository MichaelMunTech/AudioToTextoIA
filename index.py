import streamlit as st
import os
from openai import OpenAI
import streamlit as st

import Transcriber
import Model

# Configuración inicial de la interfaz de usuario
st.set_page_config(layout="wide")
transcriber_model = Transcriber.Transcriber()
chat_model = Model.Model()
with st.sidebar:
    st.title("Procesador de archivos de Audio/Video")
    file_url = st.text_input("Ingresa la URL del archivo de audio o video")


    if st.button("Process") and file_url:
        try:
            transcription = transcriber_model.transcript_audio(file_url)
            print("*** procesar")
            st.session_state.contexto=transcription.text
            st.write(st.session_state.contexto)
            #st.session_state.contextoTrancripcion=transcription.text
            st.session_state.chat_enabled = True
        except Exception as e:
            st.error(f"Error al procesar el archivo desde la URL: {e}")
            st.session_state.chat_enabled = False


# Verificar si el chat está habilitado
if st.session_state.get("chat_enabled", False):
    # Área de chat en la pantalla principal
    st.header("Chat")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


    # Crear el campo de entrada de texto sin modificar `st.session_state.user_input` después de su creación
    user_input = st.chat_input("Escribe tu mensaje:")
    if user_input:
        if user_input:
            # Añadimos el mensaje del usuario al historial del chat
            st.session_state.chat_history.append(f"Usuario: {user_input}")
            print(user_input)
            # Generamos una respuesta usando el modelo de chat
            print("*******"+st.session_state.contexto)
            response = chat_model.call_model(user_input,st.session_state.contexto)
            st.session_state.chat_history.append(f"IA: {response}")

    for message in st.session_state.chat_history:
        st.write(message)
else:
    st.info("Por favor, procesa un archivo para habilitar el chat.")