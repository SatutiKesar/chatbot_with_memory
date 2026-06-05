# 🤖 Conversational Gemini AI Assistant

A clean, responsive, and state-aware conversational chatbot application built using **LangChain**, **Google Gemini**, and **Streamlit**. This project demonstrates how to transition a terminal-based Python CLI application into a modern web interface while maintaining complete session-based chat history.

---

## 🚀 Features

* **Persistent Chat History:** Leverages Streamlit's `st.session_state` combined with LangChain's core message schemas (`SystemMessage`, `HumanMessage`, `AIMessage`) to maintain full context awareness during conversations.
* **Gemini Flash Integration:** Powered by the ultra-fast `gemini-2.5-flash-lite` model for snappy, responsive interactions.
* **Performance Optimization:** Utilizes caching (`@st.cache_resource`) to instantiate the API client once, preventing unnecessary overhead during UI refreshes.
* **Polished UI:** A responsive, scrolling web interface built with native Streamlit chat components (`st.chat_message` and `st.chat_input`).

---

## 📂 Project Structure

```text
chatbot_project/
│
├── app.py                 # The Streamlit Frontend UI & Chat Logic
├── .env                   # Local environment file containing your Gemini API key
├── requirements.txt       # Python package dependencies
└── venv/                  # Isolated Python Virtual Environment

## 📷 Application Interface

<img width="1920" height="1080" alt="Screenshot 2026-06-05 110552" src="https://github.com/user-attachments/assets/9a6e8a78-7d6e-47ad-8c69-9defa02f5213" />


<img width="1920" height="1080" alt="Screenshot 2026-06-05 110653" src="https://github.com/user-attachments/assets/6bc57e3e-de96-4aca-a8aa-a66280cf0ba9" />
