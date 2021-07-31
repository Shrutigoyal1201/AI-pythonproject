from pyttsx3 import speak
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pywhatkit

r=sr.Recognizer()

def speakText(command): #through this function it will simply speak or read out text
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def Takecom(): #will listen to your commands
    try:
        with sr.Microphone() as b:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(b,duration=0.3)
           
            #listen to the input from user
            print("Hey! I am Jarvis. How can i help you?")
            audio2=r.listen(b)
            
            # using google to recognize audio
            mytext = r.recognize_google(audio2)
            
            mytext = mytext.lower()

            print(mytext)
            
    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except Exception: #for error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    
    return mytext

def Task():
    
    def music():
        speak('tell me the name of the song')
        musicname=Takecom()
        if 'rashi' in musicname:
            os.startfile('1.mp3')
        else:
            pywhatkit.playonyt(musicname)
        speak('Your song has been started,Enjoy Maam')
    
    while True:
        query=Takecom()
    
        if 'hello jarvis' in query:
            speak("Hello Shruti! I am Jarvis.")
            speak("I am your personal Assistant")
            speak("How may I help you?")
        
        elif 'table of 91' in query:
            i=1
            while(i<=10):
                speak(91*i)
                i+=1
        
        elif 'good night' in query:
            speak('Good night Sir')
            
        elif 'about python' in query:
            speak('Python is a general-purpose programming language, so it can be used for many things. Python is used for web development, AI, machine learning, operating systems, mobile application development, and video games.')

        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open('https://www.youtube.com/')
            speak('Done Maam')
        
        elif 'open facebook' in query:
            speak('Opening facebook')
            webbrowser.open('https://facebook.com/')
            speak('Done Maam')
            
        elif 'play music' in query:
            music()
            
        
Task()