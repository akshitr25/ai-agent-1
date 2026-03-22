# 🤖 AI Task Planner Agent (Multi-Agent System)

A production-style AI system that converts user goals into structured task plans and computes total execution time using a hybrid architecture (LLM + deterministic logic).

---

## 🚀 Overview

This project implements a **multi-agent AI system** with clear separation of responsibilities:

* 🧠 **Planner Agent (LLM)** → Breaks user goals into structured tasks
* ⚙️ **Executor Agent (Code)** → Computes total time deterministically
* 🌐 **API Layer (FastAPI)** → Exposes the system as a backend service

---

## 🧠 Architecture

```
User Input
   ↓
FastAPI Endpoint (/ask)
   ↓
Planner Agent (LLM)
   ↓
Structured Task Plan
   ↓
Executor Agent (Regex-based logic)
   ↓
Final Response (Tasks + Total Time)
```

---

## ✨ Features

* Goal → structured task breakdown
* Task-level time estimation using LLM
* Deterministic total time calculation (no hallucination)
* Multi-agent design (planner + executor)
* REST API using FastAPI
* Modular and scalable backend architecture

---

## 🛠️ Tech Stack

* Python
* FastAPI
* OpenAI API (LLM)
* python-dotenv
* Regex (for deterministic computation)

---

## 📂 Project Structure

```
ai-agent-1/
├── app.py          # FastAPI API layer
├── agent.py        # Planner + Executor logic
├── config.py       # System prompts
├── main.py         # CLI testing (optional)
├── .env            # API keys (not committed)
├── requirements.txt
```

---

## ▶️ Running the Project

### 1. Clone the repo

```
git clone https://github.com/<your-username>/ai-agent-1.git
cd ai-agent-1
```

---

### 2. Install dependencies

```
python -m pip install -r requirements.txt
```

---

### 3. Setup environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

### 4. Run the API

```
uvicorn app:app --reload
```

---

### 5. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example

### Input:

```
Plan AWS certification and include total time
```

### Output:

```
1. Task name: Research AWS Certification Options  
   Time required: 2 hours  
   Priority: Medium  

...

🔹 Estimated total time: 31 hours
```

---

## 🧠 Key Design Decisions

* ❌ Avoided relying on LLM for total time (reduces hallucination)
* ✅ Used regex-based deterministic computation
* ✅ Separated planning and execution into different agents
* ✅ Designed API-first architecture for scalability

---

## 📈 Future Improvements

* Add persistent memory (database)
* Integrate tool-calling frameworks (e.g., LangGraph)
* Add frontend UI (React)
* Deploy as a cloud service

---

## 💼 Resume Highlight

> Built a multi-agent AI system using Python and FastAPI, combining LLM-based planning with deterministic execution logic to ensure reliable and scalable task automation.

---

## 👤 Author

**Akshit Rathod**
Backend Engineer | Distributed Systems | AI Systems
