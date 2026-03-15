import streamlit as st

st.title("Rule Based Chatbot")

user_input = st.text_input("You:")

if user_input:
    if "hello" in user_input.lower():
        st.write("Bot: Hello! How can I help you?")
    elif "bye" in user_input.lower():
        st.write("Bot: Goodbye!")
    else:
        st.write("Bot: I don't understand.")