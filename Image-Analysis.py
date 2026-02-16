import google.generativeai as genai
import streamlit as st
from PIL import Image
from gtts import gTTS
genai.configure(api_key='AIzaSyBzLQbPMe-uOHBw-wlYDg43lwCKXDkPrP4')
model = genai.GenerativeModel('gemini-2.5-flash')
st.title("Image Analysis")
img_file=st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])   
prompt=st.text_input("Enter your prompt related to the image:")
if st.button('submit') and prompt:
    img=Image.open(img_file)
    response=model.generate_content([prompt,img])
    st.write(response.text)
    tts=gTTS(text=response.text)
    a=tts.save("tts1.mp3")
    st.audio("a",format="mp3")
