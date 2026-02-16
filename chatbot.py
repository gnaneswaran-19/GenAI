import google.generativeai as genai
genai.configure(api_key='AIzaSyDbtoZaFMpnRys7mUHOKfZIo1GLE14Qdw8')
model=genai.GenerativeModel('gemini-2.5-flash')
role=("you are act as a mathematics genius. if user ask any question out of that. you answer them i am out of control")
prompt=input("Enter your prompt: ")
res=model.generate_content(prompt+role)
print(res.text)