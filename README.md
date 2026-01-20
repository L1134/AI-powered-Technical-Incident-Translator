# NetExplain AI  
AI-powered Technical Incident Translator for Telecom and IT Operations  

NetExplain AI is an intelligent platform that transforms raw network and infrastructure metrics into clear, executive-level incident reports using Generative AI.

Designed for telecom operators, cloud teams and IT operations, the system bridges the communication gap between highly technical environments and strategic decision makers.

---

## 🚀 Why NetExplain AI exists

In network and telecom operations:

- Engineers produce highly technical logs and metrics  
- Managers and executives struggle to interpret operational impact  
- Incident reports are often manual, slow and inconsistent  

NetExplain AI automates this process by converting technical signals into structured, business-oriented explanations that support faster and better decisions.

---

## 🧠 What it does

- Receives raw network metrics (latency, packet loss, affected users)  
- Analyzes instability patterns using Generative AI  
- Produces executive-ready incident summaries  
- Highlights business impact and technical risk  
- Suggests recommended operational actions  

---

## 🏗️ Architecture Overview

Metrics Input  
↓  
FastAPI Backend  
↓  
Google Gemini (AI Studio)  
↓  
Executive Incident Report  

---

## 🛠 Technology Stack

- Python  
- FastAPI  
- Google Gemini (AI Studio)  
- Prompt Engineering  
- HTML + JavaScript  

---

## 🔐 Security & Best Practices

- No credentials stored in the repository  
- Environment variables managed via `.env`  
- API keys never committed to GitHub  
- Clean and production-ready structure  

---

## 📌 Example Output

**Input**  
- Site: RJ-ZO-021  
- Latency: 280 ms  
- Packet loss: 6%  
- Users affected: 1200  

**Output**  

> “The site RJ-ZO-021 presents significant instability with elevated latency and packet loss.  
> Approximately 1,200 users may experience service degradation.  
> Recommended action: prioritize physical inspection and review primary link redundancy.”  

---

## 🎯 Use cases

- Telecom network operations centers (NOC)  
- Cloud infrastructure monitoring  
- IT service management  
- Executive incident reporting  
- Technical-to-business communication automation  

---

## ⚙️ Getting Started

1. Clone the repository  
2. Create a `.env` file with your Gemini API key  
3. Install dependencies  
4. Start the FastAPI server  
5. Send metrics and receive executive reports  

---

## 🌍 Vision

NetExplain AI aims to become a standard intelligent layer between technical monitoring systems and strategic decision processes, improving operational clarity, reducing incident response time and enhancing cross-functional communication in critical infrastructures.

---

## 👩‍💻 Author

Developed by Laurier Oliveira  
Telecom • Cloud • AI Applied to Infrastructure  

