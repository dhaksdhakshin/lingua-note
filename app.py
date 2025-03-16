import streamlit as st
from audio_recorder import start_recognition, stop_recognition
from pdf_generator import generate_pdf 
from utils import process_audio_file

# Main Streamlit app 
def main():  
    st.title("Live Speech-to-Text with PDF Export")
     
    st.sidebar.title("Settings")  
    st.sidebar.write("Configure your transcription options.")  
       
    # Audio Input Options  
    audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "ogg"]) 
    if audio_file: 
        captions = process_audio_file(audio_file)
        st.write("Transcription in Progress...")

    # Real-time Recording Option
    if st.button("Start Recording"):      
        st.write("Recording started...")
        captions = start_recognition() 
 
    # Display live captions with timestamps
    if 'captions' in locals():
        st.text_area("Live Captions", value="\n".join(captions), height=300)

    # PDF Download Button
    if st.button("Download PDF"):
        if 'captions' in locals():
            pdf_buffer = generate_pdf(captions, "English", 120)  # Example language and duration
            st.download_button("Download Transcript", pdf_buffer, file_name="transcript.pdf")
        else:
            st.warning("No captions available. Please record or upload an audio file.")
    
if __name__ == "__main__":
    main()
