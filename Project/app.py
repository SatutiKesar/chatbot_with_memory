import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# 1. Load Environment Variables (.env)
load_dotenv()

# 2. Configure Streamlit Page Layout
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖", layout="centered")
st.title("🤖 Gemini AI Assistant")
st.caption("A decoupled, conversational interface powered by LangChain & Streamlit")

# 3. Initialize Model Cache
# Using st.cache_resource ensures the model doesn't re-instantiate on every single page rerun
@st.cache_resource
def get_model():
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

model = get_model()

# 4. Initialize Chat History in Streamlit Session State
# If the state doesn't exist yet, we initialize it with our SystemMessage
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content='You are a helpful AI assistant')
    ]

# 5. Render Existing Chat History to the UI
# We skip the very first message [1:] because it's the invisible SystemMessage
for message in st.session_state.chat_history[1:]:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# 6. Capture and Process New User Input
if user_input := st.chat_input("Type your message here..."):
    
    # Render user message instantly in the UI
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # Append the User message to the underlying LangChain tracking list
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    # Call the model with the entire history context
    with st.chat_message("assistant"):
        # Use st.spinner to show a loading animation while the API responds
        with st.spinner("Thinking..."):
            try:
                result = model.invoke(st.session_state.chat_history)
                response_text = result.content
                
                # Display the response
                st.markdown(response_text)
                
                # Append the AI's response to the track history
                st.session_state.chat_history.append(AIMessage(content=response_text))
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")