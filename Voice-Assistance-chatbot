import google.generativeai as genai
import streamlit as st
import speech_recognition as sr

# Streamlit title
st.title("Voice Assistant Chatbot")

# Gemini API
genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

# Speech recognizer
r = sr.Recognizer()

# Button
if st.button("Start Speaking"):

    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = r.listen(source)

    try:
        # Convert speech to text
        text = r.recognize_google(audio)

        st.write("You said:", text)

        # Gemini response
        response = model.generate_content(text)

        st.write("AI Response:")
        st.write(response.text)

    except:
        st.write("Sorry, could not recognize your voice")
