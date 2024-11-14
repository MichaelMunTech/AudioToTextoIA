from openai import OpenAI

client = OpenAI(api_key="xxx")

class Model:
  def call_model(self, question, context):
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": f"""
          Eres un asistente que ayuda a responder preguntas basado solamente en el siguiente contexto {context}, si no sabes la respuesta dí no lo se,
          sé preciso y conciso en tus respuestas.
        """},
        {"role": "user", "content": question},
      ]
    )
    return completion.choices[0].message.content
