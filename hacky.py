import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good  Evening!")


    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
 


    else:
       speak("Good Evening!")

    speak("I am Hacky sir. please tell me how may I help you")    
                
def takecommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='eng-in')
        print(f"User said: {query}\n")
        speak(f"User said: {query}\n")
    
    except Exception as e:
       print(e)
       print("say that again please...")
       return "None"
    return query
     

if __name__ == "__main__":
     wishMe()
     while True:
         query = takecommand().lower()

         #Logic for executing tasks based on query//
         if 'wikipedia' in query:
             speak('searching wikipedia...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query,sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")    

         elif 'open google' in query:
             webbrowser.open("google.com") 
         
         elif 'open flipkart' in query:
             webbrowser.open("flipkart.com")   

       
