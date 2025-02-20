import streamlit as st
import requests

# Backend API URLs (Change "127.0.0.1" to your EC2 IP when deploying)
UPLOAD_API_URL = "http://127.0.0.1:8000/upload-pdf/"
ASK_API_URL = "http://127.0.0.1:8000/ask-question/"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False  # Track PDF upload status

# Streamlit UI
st.title("📄 AI Chatbot with RAG")
st.subheader("🤖 Ask me anything!But make sure you have uploaded the pdf")

# Sidebar for PDF Upload
st.sidebar.header("📂 Upload A PDF")

uploaded_file = st.sidebar.file_uploader("Choose a PDF", type="pdf")

if uploaded_file is not None and not st.session_state.pdf_uploaded:
    st.sidebar.info("📤 Uploading...")
    
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(UPLOAD_API_URL, files=files)
    
    if response.status_code == 200:
        st.sidebar.success("✅ PDF uploaded successfully!")
        st.session_state.pdf_uploaded = True
    else:
        st.sidebar.error("❌ PDF upload failed. Try again.")

# Chat Interface
st.subheader("💬 Chat with AI")
user_input = st.text_input("Ask a question:")

if st.button("Send"):
    if not st.session_state.pdf_uploaded:
        st.warning("⚠️ Please upload a PDF first!")
    elif user_input:
        response = requests.post(ASK_API_URL, params={"query": user_input})

        if response.status_code == 200:
            response_data = response.json()
            st.session_state.messages.append({"role": "user", "content": user_input})

            if "google_search_results" in response_data:
                search_results = response_data["google_search_results"]
                
                # **🛠 Fix: Ensure `search_results` is a list**
                if isinstance(search_results, list) and all(isinstance(result, dict) for result in search_results):
                    formatted_results = "\n".join(
                        [f"- [{result.get('title', 'No Title')}]({result.get('link', '#' )})" for result in search_results[:5]]
                    )
                    bot_response = "🤖 I couldn't find an exact answer in the PDF, but here are some Google search results:\n\n" + formatted_results
                else:
                    bot_response = "🤖 No relevant answers in the PDF, but Google search failed to return valid results."

            else:
                bot_response = response_data.get("answer", "🤖 Sorry, I couldn't generate a response.")

            st.session_state.messages.append({"role": "bot", "content": bot_response})
        else:
            st.error("❌ Error: Unable to fetch response.")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])