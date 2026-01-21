# 📡 NOC-AI — Incident Triage System for Telecom Network Operations

![Tech](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FJS-blueviolet)
![AI](https://img.shields.io/badge/AI-Inference-yellow)
![Domain](https://img.shields.io/badge/Domain-Telecom%2FNOC-orange)
![Status](https://img.shields.io/badge/Status-Prototype-green)

> AI-powered incident triage system designed for NOC environments in telecom and ISP operations.

---

## 🎯 Overview

**NOC-AI** interprets technical incident descriptions and automatically provides:

✔ simplified interpretation  
✔ severity classification  
✔ operational category  
✔ remediation suggestions  

This prototype demonstrates how AI can **reduce triage time**, improve operational decision-making and standardize communication inside NOC environments.

---

## 🧠 Features

- Incident interpretation (English)
- Classification engine
- Severity assessment
- Category mapping (operational domain)
- Suggested remediation actions
- Lightweight UI for demonstration
- FastAPI backend + HTML/JS frontend

---

## 🖥 UI Preview

<p align="center">
<img width="600" alt="UI Preview" src="docs/ui.png"/>
</p>

---

## 🧪 Demonstration Case

> **Input Incident**

Router interface down after configuration change. Packet loss observed.


> **System Output**

<p align="center">
<img width="552" alt="NOC AI Output" src="https://github.com/user-attachments/assets/a8171bab-aa9b-4a54-9206-f695077f8f89" />
</p>

> **Mapped Operational Domain**:  
✔ Infrastructure & Transport Layer

---

## 📡 Context: Telecom & NOC Operations

This prototype fits naturally into:

✔ NOC (Network Operation Center)  
✔ Telecom / ISP Operations  
✔ Core & Aggregation Networks  
✔ Enterprise IT Operations  
✔ Infrastructure & Transport  

NOC workflows often require:

🔹 rapid triage  
🔹 classification  
🔹 ticket enrichment  
🔹 escalation rules  
🔹 standardized language  

NOC-AI explores how AI can accelerate these steps.

---

## 🏗 System Architecture

User → UI (HTML/JS) → API (FastAPI) → Inference Logic → Output


Backend:
- Python
- FastAPI
- Rule-based inference logic

Frontend:
- HTML
- CSS
- JavaScript (Fetch API)

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML + CSS + JS |
| Backend | Python + FastAPI |
| AI | Prototype inference (rule-based) |
| Domain | Telecom / NOC |
| Status | Prototype |

---

## 🚀 Roadmap (Next Iterations)

- [ ] LLM inference (Gemini, OpenAI or Claude)
- [ ] Multi-language support (PT/EN)
- [ ] Operational taxonomies (MEF, ITIL, MetroEthernet)
- [ ] Integration with NOC tooling (Zabbix, Grafana, PRTG, IPAM)
- [ ] API exposure for third-party systems
- [ ] Deployment (Cloud or On-prem)

---

## 📚 Licença

MIT License — this prototype is open for research & experimentation.

---

## 🎙 Positioning

This repository demonstrates **integrated technical capability** across:

✔ telecom domain knowledge  
✔ AI reasoning prototypes  
✔ backend development  
✔ UI integration  
✔ operations workflow understanding  


---

## 🧩 Future Integration — LLMs in NOC Operations

This prototype can be extended with real LLMs for reasoning-based triage, using models such as:

✔ Google Gemini  
✔ OpenAI GPT  
✔ Anthropic Claude  

When LLM inference is introduced, the system shifts toward:

> **LLM-assisted triage for telecom NOC environments.**

This enables a new class of capabilities including:

🧠 semantic interpretation  
📁 ticket enrichment  
📚 normalization of technical language  
📊 decision support for escalation  
🕑 MTTI reduction (Mean Time To Identify)  

---

## 🧪 Research Motivation — Why LLMs in NOC?

Network Operation Centers handle environment-specific incidents where variance in:

✔ vendor language (Cisco, Juniper, Huawei, Nokia)  
✔ transport stacks (MetroEthernet, MPLS, IP)  
✔ OSI layers  
✔ topology  
✔ service models (FTTx, Backbone, B2B, CDN)  

creates **high cognitive load** and **slow triage**.

LLMs can reduce this cognitive overhead by performing:

🔸 linguistic normalization  
🔸 domain mapping  
🔸 context inference  
🔸 protocol awareness  


---

## 📊 Operational KPIs for AI-assisted NOC

Potential KPIs impacted:

| KPI | Descrição |
|---|---|
| **MTTI** (Mean Time To Identify) | Tempo até identificar o tipo do incidente |
| **MTTE** (Mean Time To Enrich) | Tempo até enriquecer ticket com dados úteis |
| **MTTS** (Mean Time To Suggest) | Tempo para sugerir ações corretivas |
| **Escalation Quality** | Precisão na sugestão de equipe/nível para escalar |
| **Incident Categorization Accuracy** | Taxa de acerto na categorização |
| **Ticket Normalization Rate** | Quanto a IA reduz variação semântica |
| **Cognitive Load Reduction** | Redução de esforço mental dos analistas |
| **Operational Consistency** | Padronização inter-analista/nivel |


---

## 🧩 Where LLMs Integrate in NOC Workflow

Standard NOC workflow:

Incident → Triage → Classification → Enrichment → Escalation → Resolution

LLMs help mainly in:

Incident → [LLM Triage + Enrichment] → Classification → Escalation


---

## ⚠ Limitations & Considerations

LLMs in NOC environments must account for:

- network vendor vocabulary
- industry domain knowledge
- protocol stack awareness
- real-time constraints
- operational SLAs
- confidentiality & data residency


## 🎙 Closing Positioning

This project explores how AI can support network operations by enriching and accelerating incident triage workflows in telecom environments — without replacing human operational expertise.

---

## 🧭 Strategic Positioning

This project sits at the intersection of:

✔ **Product** — explores a viable tool for telecom NOC operations  
✔ **Applied Research** — evaluates LLM triage capabilities in real operational workflows  
✔ **Technical Thesis** — formalizes how AI can assist network incident analysis  
✔ **Platform Potential** — designed to integrate with NOC tooling and monitoring ecosystems  

This combination allows NOC-AI to evolve in multiple directions depending on context:

- as an internal enterprise tool
- as an ISP / telecom operational asset
- as a research artifact
- as a product prototype
- as a platform component in monitoring + ticketing stacks


---


---

## 🔌 Integration Ecosystem

Potential integration points include:

📡 **Monitoring & Telemetry**
- Zabbix
- Grafana
- PRTG
- LibreNMS
- Observium

📁 **Ticketing & ITSM**
- ServiceNow
- Jira Service Management
- Remedy
- GLPI

🌐 **Network Platforms**
- IPAM
- DNS
- BGP collectors
- Netflow / Sflow
- Syslog

🧠 **AI Layer**
- Gemini
- OpenAI
- Claude
- Local inference (LLM/LoRA)


---

## 📊 Operational KPIs Impacted

| KPI | Impact |
|---|---|
| **MTTI** (Mean Time To Identify) | Reduced by automating incident interpretation |
| **MTTE** (Mean Time To Enrich) | Automated ticket enrichment via AI |
| **Escalation Accuracy** | Improved routing to correct teams |
| **Categorization Accuracy** | Consistent mapping across analysts |
| **Cognitive Load** | Lowered for on-duty NOC analysts |
| **Operational Consistency** | Standardization of technical language |
| **SLA Preservation** | Faster triage can reduce SLA violations |


---

## 🚀 Evolution Map (Technology Maturity)

Prototype → LLM-assisted triage → Ticket enrichment → Escalation intelligence → NOC automation pipeline





