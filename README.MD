# 🤖 AI Task Assistant (Agent)

A simple agentic AI system that takes user goals and converts them into structured, actionable tasks.

## 🚀 Features

* Goal → Task breakdown using LLM
* Conversational memory (multi-turn interaction)
* Structured output (task, time, priority)
* Runs locally using Ollama (no API cost)

## 🛠️ Tech Stack

* Python
* Ollama (Llama3)
* Prompt Engineering

## 🧠 How it works

1. User enters a goal
2. Agent processes input using LLM
3. Maintains conversation history
4. Returns structured task plan

## ▶️ Run Locally

```bash
pip install ollama
ollama run llama3
python main.py
```

## 📌 Example

Input:

```
Plan AWS certification
```

Output:

```
1. Study fundamentals - 2 hrs - High
2. Practice labs - 1 hr - High
```

## 📈 Future Improvements

* Add tool usage (API calls)
* Convert to FastAPI backend
* Add persistent memory (DB)

## 👤 Author

Akshit Rathod
