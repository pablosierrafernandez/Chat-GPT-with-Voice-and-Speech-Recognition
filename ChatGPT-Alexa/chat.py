# importamos cosas
import datetime
import speech_recognition as sr
import pyaudio as ptg
from imports.auth import * # * --> all
import openai
import pyttsx3
############################## CENTINELA DE INICIO
openai.api_key=api_key
r=sr.Recognizer()

conversation=""
engine=pyttsx3.init()
engine.setProperty('voice',0)
engine.setProperty('rate',150)

try:
    while(True):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=2)
            print("Escuchando...")
            audio=r.listen(source)
        try:
            text=str(r.recognize_google(audio,language=language_chat, show_all=True))
            print(text)

            conversation+="\Humano: "+text+"\nAI: "
            conversation=conversation.strip()
            response=openai.Completion.create(engine="text-davinci-003",prompt=conversation,temperature=0.9,max_tokens=150,top_p=1,frequency_penalty=0,presence_penalty=0.6, stop=["\n","Humano","AI"])
            
            answer=response.choices[0].text
            conversation+=answer
            fecha=datetime.datetime.fromtimestamp(response.created).strftime('%H:%M:%S')
            print(f"AI ({fecha}): {answer}\n")
            engine.say(answer)
            engine.runAndWait()
        except:
            print("No reconozco tu voz")
        
except KeyboardInterrupt:
    engine.say("Hasta pronto!")
    engine.runAndWait()
    print("\nHasta pronto!")
    