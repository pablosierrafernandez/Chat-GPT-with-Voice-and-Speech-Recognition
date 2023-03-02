# importamos cosas
import datetime
from imports.auth import * # * --> all
import openai
import pyttsx3
############################## CENTINELA DE INICIO
openai.api_key=api_key
conversation=""
engine=pyttsx3.init()
engine.setProperty('voice',0)
engine.setProperty('rate',150)

try:
    while(True):
        question=input("Humano:")
        conversation+="\Humano: "+question+"\nAI: "
        response=openai.Completion.create(engine="text-davinci-003",prompt=conversation,temperature=0.9,max_tokens=150,top_p=1,frequency_penalty=0,presence_penalty=0.6, stop=["\n","Humano","AI"])
        answer=response.choices[0].text.strip()
        conversation+=answer
        fecha=datetime.datetime.fromtimestamp(response.created).strftime('%H:%M:%S')
        print(f"AI ({fecha}): {answer}\n")
        engine.say(answer)
        engine.runAndWait()
except KeyboardInterrupt:
    engine.say("Hasta pronto!")
    engine.runAndWait()
    print("\nHasta pronto!")
    