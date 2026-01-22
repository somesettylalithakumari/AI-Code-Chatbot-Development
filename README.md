#  AI Booking Assistant 

An end-to-end **AI Booking Assistant** built with **Streamlit**, **Groq LLM**, and **Retrieval-Augmented Generation (RAG)**.  
The assistant answers user questions using uploaded PDFs and intelligently guides users through a complete **booking workflow**, storing data in a database and sending email confirmations.

---

## Features

- Conversational AI using Groq LLM  
- PDF-based Knowledge Base (RAG)  
- Smart, multi-step Booking Flow  
- Context-aware question answering  
- Persistent database storage  
- Email confirmation on booking  
- Built-in Admin Dashboard  
- Session state management  
- Streamlit-powered UI  

---

##  Project Structure
ai_code_chatbot/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # Streamlit entry point
│   ├── admin_dashboard.py      # Admin UI
│   ├── rag_pipeline.py         # PDF ingestion + RAG
│   ├── booking_flow.py         # Booking logic
│   ├── tools.py                # DB + email utilities
│   └── config.py               # App configuration
│
├── db/
│   ├── __init__.py
│   └── database.py             # Database initialization
│
├── models/
│   ├── __init__.py
│   └── llm.py                  # Groq LLM wrapper
│
├── requirements.txt
└── README.md

# Requirements
Python 3.9+
Streamlit
Groq API Key
Internet access (for LLM)
SMTP credentials (for email)

# Installation
Clone the Repository
```
git clone https://github.com/yourusername/ai_code_chatbot.git
cd ai_code_chatbot
```
Install Dependencies
```
pip install -r requirements.txt
```
# Environment Variables
Create a .env file (or export manually):
```
GROQ_API_KEY=your_groq_api_key
SMTP_EMAIL=your_email@example.com
SMTP_PASSWORD=your_email_password
```

# Running the Application
```
python -m streamlit run app/main.py
```


# How It Works
## Chat Flow
- User asks a question
- PDFs are searched via RAG
- Groq LLM generates a context-aware response

## Booking Flow
- User says “I want to book”
Assistant collects:
Name
Email
Date
Time
Booking is summarized
User confirms
Booking is saved to DB
Confirmation email is sent

## PDF Knowledge Base (RAG)
- Upload PDFs from the UI
- PDFs are embedded and indexed
- AI answers questions only using uploaded knowledge

## Admin Dashboard
- View all bookings
- Monitor system usage
- Accessible from the bottom of the app


<p align="center">
  <img 
    src="https://github.com/user-attachments/assets/3f3ad097-2d1b-4a2e-a9e5-339e3e4f5d6f"
    alt="Application Screenshot"
    width="900"
  />
</p>







