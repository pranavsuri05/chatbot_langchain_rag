<h1>AI Chatbot for Document & Web Search</h1>

<h2>Overview</h2>
<p>This chatbot is designed to efficiently handle both document-based and web-based queries using advanced AI techniques. It has evolved through multiple versions, improving retrieval accuracy, workflow automation, and deployment.</p>
<p>P.S.: Currently working to host it ^_^ </p>

<h2>Features</h2>
<ul>
  <li><strong>PDF Document Querying:</strong> Upload PDFs and extract answers from them.</li>
  <li><strong>Web Search Integration:</strong> Uses Serper API for real-time Google search when document content is insufficient.</li>
  <li><strong>AI-Powered Retrieval:</strong>
    <ul>
      <li><strong>LangChain</strong> for structured query processing.</li>
      <li><strong>FAISS</strong> for vector database storage and semantic search.</li>
      <li><strong>Hugging Face embeddings</strong> to enhance response relevance.</li>
    </ul>
  </li>
  <li><strong>FastAPI & Streamlit Deployment:</strong>
    <ul>
      <li>Accessible via <strong>Swagger UI</strong> (FastAPI).</li>
      <li>User-friendly interface with <strong>Streamlit</strong>.</li>
    </ul>
  </li>
</ul>

<h2>Files & Versions</h2>
<ul>
  <li><strong>chatbot_app.ipynb</strong> – Core chatbot logic using FastAPI.</li>
  <li><strong>streamlit_app.py</strong> – Streamlit web app for chatbot interaction.</li>
  <li><strong>Older Versions:</strong>
    <ul>
      <li><strong>Chatbot_RAG_langchain (1).ipynb</strong> – Initial version of the chatbot.</li>
      <li><strong>Chatbot_RAG_langchain (2).ipynb</strong> – Upgraded with FastAPI, PDF handling, and Q&A support.</li>
    </ul>
  </li>
</ul>

<h2>Next Steps</h2>
<ul>
  <li><strong>Serper API Integration</strong> for enhanced web search.</li>
  <li><strong>Optimizing the chatbot’s pipeline</strong> for improved accuracy and efficiency.</li>
</ul>
