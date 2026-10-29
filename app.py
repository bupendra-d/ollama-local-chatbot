import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Page configuration
st.set_page_config(
    page_title="Ollama Local Chatbot",
)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer user questions clearly."),
    ("human", "{question}")
])


# Generate response
def generate_response(question, model_name, temperature, max_tokens):
    llm = ChatOllama(
        model=model_name,
        temperature=temperature,
        num_predict=max_tokens
    )

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"question": question})


# Streamlit interface
st.title("Local Q&A Chatbot")
st.caption("Powered by LangChain and Ollama")

# Sidebar settings
st.sidebar.header("Model Settings")

model_name = st.sidebar.selectbox(
    "Select Model",
    ["llama3.2:3b"]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

max_tokens = st.sidebar.slider(
    "Maximum Response Tokens",
    min_value=50,
    max_value=300,
    value=150,
    step=50
)

# User input
with st.form("chat_form"):
    question = st.text_input("Ask a question:")
    submitted = st.form_submit_button("Generate Response")

if submitted:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Generating response locally..."):
                answer = generate_response(
                    question=question,
                    model_name=model_name,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

            st.subheader("Response")
            st.write(answer)

        except Exception:
            st.error(
                "Unable to generate a response. "
                "Ensure Ollama is running and the selected model is installed."
            )

st.caption("Responses are generated using your local Ollama installation.")