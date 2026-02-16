import streamlit as st
import requests
from PIL import Image   
st.title("Image Generation")
prompt=st.text_input('enter your prompt')
url="https://image.pollinations.ai/prompt/"+requests.utils.quote(prompt)
response=requests.get(url).content

if st.button('submit') and prompt:
    st.image(response)
