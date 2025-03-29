import sounddevice as sd
import numpy as np
import whisper  # Corrected import for Whisper model
import tempfile  
import wave  

# Initialize the Whisper model for speech-to-text  
model = whisper.load_model("base")    
 
# Function to record audio 
def record_audio(duration=10, fs=16000):
    # Record audio for a specific duration
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished 
    return recording

# Function to save audio to a temporary file
def save_audio(recording, fs=16000):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    with wave.open(temp_file.name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes per sample 
        wf.setframerate(fs) 
        wf.writeframes(np.array(recording, dtype=np.int16).tobytes())
    return temp_file.name
 
# Function to start live speech recognition
def start_recognition():
    st.write("Recording...") 
    audio = record_audio(duration=10)  # Record for 10 seconds
    audio_file = save_audio(audio)
    captions = transcribe_audio(audio_file)
    return captions

# Function to stop recognition
def stop_recognition():
    pass  # Handle stopping logic if needed (not used in this case)

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    result = model.transcribe(audio_file)
    captions = []
    for segment in result['segments']:
        captions.append(f"{segment['start']} - {segment['end']}: {segment['text']}")
    return captions
