import streamlit as st
import ollama

st.title("AI CHATBOT")

question = st.text_input("Enter your question:")

if st.button("Submit"):
    if question:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response["message"]["content"]

        st.subheader("AI Response")
        st.write(answer)

    else:
        st.warning("Please enter a question.")