import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "api-key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key="api-key"
    )
    completion = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages= [
        { "role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud" },
        {"role": "user","content": command},
    ],
    )
    return completion.choices[0].message.content


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https//google.com")
    elif "open github" in c.lower():
        webbrowser.open("https//github.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https//youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https//linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        output = aiProcess(c)
        speak(output)
        

if __name__ == "__main__":
    speak("Initializinig Jarvis....")

while True:
    r = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2 , phrase_time_limit=1)
        print("Recognizing...")
        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
            speak("Ya")
            with sr.Microphone() as source:
                print("Jarvis active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                
                processcommand(command)

    
    except Exception as e:
        print("Error {0}".format(e))

