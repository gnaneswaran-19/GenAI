import google.generativeai as genai
import streamlit as st
from PIL import Image
genai.configure(api_key='AIzaSyDbtoZaFMpnRys7mUHOKfZIo1GLE14Qdw8')
model=genai.GenerativeModel('gemini-2.5-flash')     
st.title("Image Analysis with Gemini-2.5")
img_file=st.file_uploader("Upload an image",type=["png","jpg","jpeg"])
prompt=st.text_input('Enter the question')
if st.button('submit') and prompt:
    img=Image.open(img_file)
    res=model.generate_content([prompt,img])
    st.write(res.text)
