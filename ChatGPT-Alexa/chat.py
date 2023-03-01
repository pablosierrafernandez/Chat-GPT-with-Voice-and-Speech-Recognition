# importamos cosas
from imports.auth import * # * --> all
import openai
openai.api_key=api_key
conversation=""
i=1
while(i!=0):
    question=input("Humano:")
    conversation+="\Humano: "+question+"\nAI: "
    response=openai.Completion.create(engine="text-davinci-003",prompt=conversation,temperature=0.9,max_tokens=150,top_p=1,frequency_penalty=0,presence_penalty=0.6, stop=["\n","Humano","AI"])
    answer=response.choices[0].text.strip()
    conversation+=answer
    print("AI: "+answer+"\n")