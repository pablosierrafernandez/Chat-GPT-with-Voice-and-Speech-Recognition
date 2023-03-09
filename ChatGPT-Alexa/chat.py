# importamos cosas
import datetime
import speech_recognition as sr
import pyaudio as ptg
from imports.auth import * # * --> all
import openai
import pyttsx3
import sqlite3
############################## CENTINELA DE INICIO
openai.api_key=api_key
r=sr.Recognizer()

conversation=""
engine=pyttsx3.init()
engine.setProperty('voice',0)
engine.setProperty('rate',150)

miConexion=sqlite3.connect("chat.bd")
miCursor=miConexion.cursor()
try:
    miCursor.execute("CREATE TABLE HISTORIAL(ID INTEGER PRIMARY KEY AUTOINCREMENT, PREGUNTA TEXT, RESPUESTA TEXT, FECHA DATETIME)")
except:
    pass
try:
    while(True):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=2)
            print("Escuchando...")
            audio=r.listen(source)
        try:
            text=str(r.recognize_google(audio,language=language_chat))
            

            conversation+="\Humano: "+text+"\nAI: "
            conversation=conversation.strip()
            response=openai.Completion.create(engine="text-davinci-003",prompt=conversation,temperature=0.9,max_tokens=150,top_p=1,frequency_penalty=0,presence_penalty=0.6, stop=["\n","Humano","AI"])
            
            answer=response.choices[0].text
            conversation+=answer
            fecha=datetime.datetime.fromtimestamp(response.created).strftime('%H:%M:%S')
            print(f"AI ({fecha}): {answer}\n")
            engine.say(answer)
            engine.runAndWait()
            
            miCursor.execute("INSERT INTO HISTORIAL (PREGUNTA, RESPUESTA, FECHA) VALUES(?, ?, ?)",(text,answer,datetime.datetime.fromtimestamp(response.created)))
           
        except:
            print("No reconozco tu voz")
        
except KeyboardInterrupt:
    miConexion.commit()
    miConexion.close()
    engine.say("Hasta pronto!")
    engine.runAndWait()
    
    print("\nHasta pronto!")
    
    