from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = genai.GenerativeModel("gemini-pro")

class IncidentRequest(BaseModel):
    text: str

@app.post("/translate")
def translate_incident(request: IncidentRequest):
    prompt = f"""
    You are an AI assistant specialized in Telecom NOC operations (ISP + Telco + Core).
    
    Analyze the following incident and respond ONLY in valid JSON with these fields:

    - translated_text: simplified execution-level English
    - severity: High | Medium | Low
    - category: e.g. BGP, Access, RF, Fiber, Routing, Transport, Core, OSS, Power,...
    - layer: OSI layer (L1-L7)
    - suggested_action: short technical action
    - noc_domain: Access | Aggregation | Core | Edge | Datacenter
    
    INCIDENT:
    "{request.text}"
    """

    response = model.generate_content(prompt)

    try:
        data = json.loads(response.text)
    except:
        # fallback if model returns fenced code block etc
        cleaned = response.text.replace("```json", "").replace("```", "")
        data = json.loads(cleaned)

    return data




