from pypdf import PdfReader
import streamlit as st
import google.generativeai as genai
genai.configure(api_key='AIzaSyBzLQbPMe-uOHBw-wlYDg43lwCKXDkPrP4')
model=genai.GenerativeModel('gemini-2.5-flash')
st.title("Pdf Extractor")
file=st.file_uploader("Upload your PDF file", type=["pdf"])
prompt=st.text_input("Enter your prompt here")
if st.button('submit') and file:
    reader=PdfReader(file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    response=model.generate_content([text,prompt])
    print(st.write(response.text))