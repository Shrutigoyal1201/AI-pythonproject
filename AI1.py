import speech_recognition as s
sr=s.Recognizer() #constructor
print("I am you Script and Listening to you...")
with s.Microphone() as m:
    audio=sr.listen(m)
    query = sr.recognize_google(audio,language='eng-in')
    print(query) 