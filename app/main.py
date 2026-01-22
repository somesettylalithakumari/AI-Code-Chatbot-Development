import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

# ---------- IMPORTS ----------
import streamlit as st
from db.database import init_db
from admin_dashboard import admin_ui
from rag_pipeline import ingest_pdfs
from chat_logic import handle_chat
from models.llm import get_chatgroq_model

# ---------- INITIALIZE DATABASE ----------
init_db()

# ---------- STREAMLIT CONFIG ----------
st.set_page_config(
    page_title="AI Booking Assistant",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "booking_state" not in st.session_state:
    st.session_state.booking_state = {}

st.title("🤖 AI Booking Assistant (Groq)")

# ---------- PDF UPLOAD ----------
pdfs = st.file_uploader(
    "Upload PDFs for Knowledge Base",
    type="pdf",
    accept_multiple_files=True
)

if pdfs:
    ingest_pdfs(pdfs)
    st.success("✅ PDFs processed successfully")

# ---------- CHAT HISTORY ----------
for msg in st.session_state.messages[-25:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- MODEL ----------
chat_model = get_chatgroq_model()
user_input = st.chat_input("Ask a question or say 'I want to book'...")

# ---------- CHAT LOGIC ----------
if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------- PROCESS USER INPUT ----------
    response = handle_chat(user_input, st.session_state.booking_state)

    # ---------- SAVE ASSISTANT MESSAGE ----------
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# ---------- ADMIN PANEL ----------
st.divider()
admin_ui()
