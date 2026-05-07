from elevenlabs.client import ElevenLabs
import streamlit as st
from elevenlabs import save
st.title("Voice Generator")
model=ElevenLabs(api_key="d25bc7865471ca5c307b59716c4b7eb26ed08b096203a10e0d02c77e10d22c25")
prompt=st.text_input("Enter your text here:")
id="yrFqUM5ku2rYJCdiBKFU"
if st.button("Generate Voice"):
    audio=model.text_to_speech.convert(text=prompt,voice_id=id)
    save(audio,"output.mp3")
    print(st.audio("output.mp3"))