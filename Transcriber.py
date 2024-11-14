from openai import OpenAI

client = OpenAI(api_key="xxx")

class Transcriber:
  def __init__(self):
    self.transcription = None

  def transcript_audio(self, audio_path):
    if self.transcription is None:
      audio_file= open(audio_path, "rb")
      self.transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
      )
    return self.transcription
