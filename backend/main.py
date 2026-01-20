from fastapi import FastAPI
from pydantic import BaseModel
import os
import google.generativeai as genai

app = FastAPI(title="AI Technical Incident Translator")

# Modelo de entrada
class IncidentRequest(BaseModel):
    text: str

# Inicializa Gemini (a chave virá depois via variável de ambiente)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.post("/translate")
def translate_incident(request: IncidentRequest):
    prompt = f"""
You are an expert telecom and IT engineer.
Translate the following technical incident into simple language for non-technical managers:

Incident:
{request.text}
"""

    response = model.generate_content(prompt)

    return {
        "original": request.text,
        "translated": response.text
    }
