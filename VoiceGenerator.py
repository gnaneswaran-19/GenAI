from elevenlabs.client import ElevenLabs
import streamlit as st
from elevenlabs import save
st.title("Voice Generator")
model=ElevenLabs(api_key="Your API key")
prompt=st.text_input("Enter your text here:")
id="yrFqUM5ku2rYJCdiBKFU"
if st.button("Generate Voice"):
    audio=model.text_to_speech.convert(text=prompt,voice_id=id)
    save(audio,"output.mp3")
    print(st.audio("output.mp3"))
