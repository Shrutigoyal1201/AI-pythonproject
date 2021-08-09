import speech_recognition as sr
import pyttsx3
from pyttsx3 import speak
import webbrowser
import os
import pywhatkit
import datetime
from PyDictionary import PyDictionary as d


r=sr.Recognizer() # recognizes the sound

def speakText(command): #through this function it will simply speak or read out text
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def dict():
    speak("Activated dictionary!")
    speak("Tell Me The Problem!")
    prob1 = Takecom()

    if 'meaning' in prob1:
            prob1 = prob1.replace("what is","")
            prob1 = prob1.replace("what is the meaning of","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("meaning of","")
            result =d.meaning(prob1)
            speak(f"The Meaning for {prob1} is {result}")

    elif 'synonym' in prob1:
            prob1 = prob1.replace("what is","")
            prob1 = prob1.replace("what is the meaning of","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("synonym of","")
            result =d.synonym(prob1)
            speak(f"The synonym for {prob1} is {result}")
    elif 'antonym' in prob1:
            prob1 = prob1.replace("what is","")
            prob1 = prob1.replace("what is the meaning of","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("antonym of","")
            result =d.antonym(prob1)
            speak(f"The antonym for {prob1} is {result}")
            speak("Exited Dictionary!")
    
def Takecom(): #will listen to your commands
    try:
        with sr.Microphone() as mic:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(mic)
            
            print("I am Jarvis. How can I help you?")
            #listen to the input from user
            audio1= r.listen(mic)
           
            # using google to recognize audio
            mytext = r.recognize_google(audio1)
            mytext = mytext.lower()   

            print(mytext)
            
    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))
    except Exception: #for error handling
        speak("error...")
        print("Network connection error") 
        return "none"
    
    return mytext

# speakText('Hello Maam')

def Task():
    
    def openapp():
        speak('OK mam wait a second')
        if 'open dev c plus plus' in query:
            os.startfile('"C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"')
        elif 'open cisco' in query:
            os.startfile('"C:\\Program Files (x86)\\Cisco Packet Tracer 6.2sv\\bin\\PacketTracer6.exe"')
        speak('Your command has been completed Maam')

    def closeapp():
        speak('OK mam wait a second')
        if 'close sublime' in query:
            os.closefile('TASKKILL /F /in sublime.exe')
    
    def wishme():
        hour= int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning Shruti Maam!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Shruti Maam!")
        else:
            speak("Good Evening Shruti Maam!")

    def music():
        speak('tell me the name of the song')
        musicname=Takecom()
        if 'first' in musicname:
            os.startfile('1.mp3')
        else:
            pywhatkit.playonyt(musicname)
        speak('Your song has been started,Enjoy Maam')
    
    wishme()
    
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
            
        elif 'open dev c++' in query:
                openapp()
        
        elif 'open cisco' in query:
                openapp()
        
        elif 'close dev c plus plus' in query:
            closeapp()
        
        elif 'close cisco' in query:
            closeapp()
            
        elif 'google search' in query:
            speak("This is what I found for you Ma'am!")
            query=query.replace("jarvis","")
            query=query.replace("google search","")
            pywhatkit.search(query)
            speak("Done Ma'am")
            
        elif 'open website' in query:
            speak("Tell me the name of the website")
            name=Takecom()
            web ='https://www.' + name + '.com' 
            webbrowser.open(web)
            speak("Done Maam")
            
        elif 'd' in query:
            dict()

        elif 'close all tabs' in query:
            os.system('taskkill /F /IM chrome.exe')
            
        elif 'shutdown' in query:  
            pywhatkit.shutdown(time=1)
Task()

'''
PYTHON LIBRARIES


Module is a file which contains various Python functions and global variables. It is simply just .py extension file which has python executable code.

Package is a collection of modules. It must contain an init.py file as a flag so that the python interpreter processes it as such. The init.py could be an empty file without causing issues.

Library is a collection of packages.

Framework is a collection of libraries. This is the architecture of the program.




1. PyAudio- is a set of Python bindings for PortAudio, a cross-platform C++ library interfacing with audio drivers.


2. pyttsx3- https://pyttsx3.readthedocs.io/en/latest/engine.html
pyttsx3 is a text-to-speech conversion library in Python. 
Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3. An application invokes the pyttsx3.
init() factory function to get a reference to a pyttsx3.


3. Speech recognition- is the process of converting spoken words to text.
Python supports many speech recognition engines and APIs, including Google Speech Engine, Google Cloud Speech API, Microsoft Bing Voice Recognition and IBM Speech to Text.


4. webbrowser- module provides a high-level interface to allow displaying Web-based documents to users. 
Under most circumstances, simply calling the open() function from this module will do the right thing.
The script webbrowser can be used as a command-line interface for the module. 
It accepts a URL as the argument. It accepts the following optional parameters: -n opens the URL in a new browser window, if possible; -t opens the URL in a new browser page (“tab”). 
The options are, naturally, mutually exclusive. Usage example:  python -m webbrowser -t "https://www.python.org"


5. OS-module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules.
This module provides a portable way of using operating system dependent functionality. The os and os. path modules include many functions to interact
with the file system.


6. Pywhatkit- Python offers numerous inbuilt libraries to ease our work. Among them pywhatkit is a Python library for sending WhatsApp messages at a certain time,
it has several other features too.
Following are some features of pywhatkit module:
Send WhatsApp messages.
Play a YouTube video.
Perform a Google Search.
Get information on particular topic.

Function pywhatkit.playonyt(), opens the YouTube in your default browser and plays the video you mentioned in the function. If you pass the topic
name as parameter, it plays the random video on that topic. On passing the URL of the video as the parameter, it open that exact video.

You can perform a Google search using the following simple command. It opens your browser and searches for the topic you have given in your code.
Syntax: pywhatkit.search(“Keyword”)

We can get brief information on a particular topic. We can also limit the number of lines to be printed. Also, make sure that you are searching for
 the topics that are available on Wikipedia.
Syntax: pywhatkit.info(“topic”,lines=x)


7. PyDictionary- is a dictionary (as in the English language dictionary) module for Python2 and Python3. PyDictionary provides the following services
for a word:
meanings
translations


8. adjust_for_ambient_noise- Noise is a fact of life. All audio recordings have some degree of noise in them, and un-handled noise can wreck the accuracy of speech
 recognition apps.
The adjust_for_ambient_noise() method reads the first second of the file stream and calibrates the recognizer to the noise level of the audio.
 Hence, that portion of the stream is consumed before you call record() to capture the data.
You can adjust the time-frame that adjust_for_ambient_noise() uses for analysis with the duration keyword argument.
 This argument takes a numerical value in seconds and is set to 1 by default. Try lowering this value to 0.5.




'''