import speech_recognition as sr
import pyaudio as ptg
r = sr.Recognizer()

while(True):
    with sr.Microphone() as micro:
        print("Di algo...")
        
        audio=r.listen(micro)
        print("no llwgo")
    try:
        text=str(r.recognize_google(audio,language='es-Es'))
        print("llego aquuio")
        print(text)
    except:
        print("No reconozco tu voz")
        