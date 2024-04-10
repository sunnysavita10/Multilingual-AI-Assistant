import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech


def main():
    st.title("Multilingual AI Assistant 🤖")
    
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text=voice_input()
            response=llm_model_object(text)
            text_to_speech(response)
            
            
            audio_file=open("speech.mp3","rb")
            audio_bytes=audio_file.read()
            
            
            st.text_area()
            st.audio()
            st.download_button()
            
if __name__=='__main__':
    main()
