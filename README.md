# 📝 LinguaNote - Voice-to-Text Application

LinguaNote is a real-time voice-to-text application that converts spoken words into accurate, structured text captions. Designed for desktop users, it provides seamless transcription, customizable captions, and export options in multiple formats.

---

## 🚀 Features

✅ **Real-Time Speech-to-Text** – Uses OpenAI Whisper, Google Speech-to-Text, or Azure for multilingual voice recognition.  
✅ **Live Caption Display** – Shows real-time transcriptions with customizable fonts, colors, and timestamps.  
✅ **Audio Input Options** – Supports microphone input and pre-recorded audio files.   
✅ **Structured PDF Export** – Downloads transcripts with timestamps, metadata, and formatted text for readability.   
✅ **Enhanced UX** – Auto-stops on silence detection, highlights spoken words, and allows caption preview.  
✅ **Export Formats** – Save transcripts in `.pdf`, `.txt`, `.docx`, and `.srt` for flexible use.    
✅ **Timestamp Customization** – Users can modify timestamp intervals per word or per sentence.  
✅ **Error Handling** – Detects low-quality audio and provides grammar correction options..

---

## 🛠️ Installation

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/dhaksdhakshin/lingua-note.git

LinguaNote/
│── app.py                  # Main Streamlit application
│── audio_recorder.py        # Handles live audio input
│── transcription.py         # Speech-to-text processing logic
│── export.py                # PDF & file export functions
│── utils.py                 # Helper functions
│── requirements.txt         # Required dependencies
│── README.md                # Project documentation
│── assets/                  # Logo and design assets
│── venv/                    # Virtual environment (ignored in Git)
cd lingua-note
