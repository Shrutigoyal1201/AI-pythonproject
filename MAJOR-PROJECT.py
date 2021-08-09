import requests
import json
from tkinter import *
from PIL import ImageTk,Image
from tkinter.messagebox import showinfo, showerror
import smtplib as s 
import datetime
from datetime import date
import time
from functools import partial
from random import randint
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
from pyttsx3 import speak
import webbrowser
import os
import pywhatkit
from PyDictionary import PyDictionary as d

#smtplib is an inbuilt library in python, No need to install it.

root=Tk()
root.title("Personal Assistant")
root.geometry("400x800")
font = ("Helvetica", 20, "bold")

# Create a photoimage object of the image in the path
image1 = Image.open("img6.jpg")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)

# canvas = Canvas(root, width = 300, height = 300)
# canvas.pack()
# img = ImageTk.PhotoImage(Image.open("C:\Users\Asus\OneDrive\Desktop\py\project\4\img.jpg"))
# canvas.create_image(20, 20, anchor=NW, image=img)

def message():
    
    def send_sms(number,message):
        url = "https://www.fast2sms.com/dev/bulkV2"

        params= {
            "authorization":"ArkGJgtOYd62nX1qHy3548VwlUiuZmexpNojIzFcK0W7BDT9bQrA7GuKCEJnYpD4fNjVF0vbP9QezhyM",
            "sender_id":"TXTIND",
            "message":message,
            "language":"English",
            "route":"v3",
            "numbers":number
        }
    
        response=requests.get(url,params=params)
        a=response.json()
        # print(a)
        return a.get("return")

    

    def btnmsgclick():
        num=textNumber.get()
        msg=textMsg.get("1.0",END)
    
        r=send_sms(num,msg)

        if r:
            showinfo("Status","Message sent successfully")
        else:
            showerror("Error","Something went wrong ;(")


    root=Tk()
    root.title("Message Sender")
    root.geometry("400x800")
    font = ("Helvetica", 22, "bold")
    w = Label(root, text="Enter Number", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=20)
    textNumber=Entry(root,font=font)
    textNumber.pack(fill=X)
    w = Label(root, text="Type Your Message", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=20)
    textMsg=Text(root)
    textMsg.pack(fill=X,pady=20)

    sendBtn=Button(root,text="SEND MESSAGE",command=btnmsgclick, bg="green",
                fg='white')
    sendBtn.pack()

    root.mainloop()
    
def email():
      
    def send_email(sub,body,ra):
        ob=s.SMTP('smtp.gmail.com',587) 
        #ob is a variable= s is the SMTP library, mail address, port number
        ob.starttls()
        ob.login("shrutigoyal1201@gmail.com","mciscwxpftzoeork")
        subject=sub
        body=body
        message ="Subject:{}\n\n{}".format(subject,body)
        listofaddress=ra
        ob.sendmail("shrutigoyal1201@gmail.com",listofaddress,message)
        ob.quit()
        return True
       
    def btnemailclick():
        sub=subject.get()
        body=emailbody.get("1.0",END)
        ra=nra.get()
    
        r=send_email(sub,body,ra)

        if r:
            showinfo("Status","Email sent successfully")
        else:
            showerror("Error","Something went wrong ;(")
        
    root=Tk()
    root.title("Email Sender")
    root.geometry("400x800")
    font = ("Helvetica", 22, "bold")
    
    w = Label(root, text=" Sender's Address - shrutigoyal1201@gmail.com", bg="white", fg="black")
    w.pack(fill=X, padx=10,pady=20)
    
    w = Label(root, text="No. of Recipients", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=10)
    
    def recadd(s):
        try:
            s=int(Entry.get(s))
            root=Tk()
            root.title("Recipients Email")
            root.geometry("400x800")
        
            global l
        
            l=list()
            
            for i in range(1, s+1):
                
                receiveraddress = Label(root,text="Address " + str(i))
                receiveraddress.pack(fill=X,pady=10)
                
                r = Entry(root,font=font)
                r.pack(fill=X,pady=10)
            
            for i in range(1, s+1):
                    
                r=str(Entry.get(r))
            
                l.append(r)
                
            print(l)
        
        except:
            showerror("Error","Please add a valid input for no. of recipients")
            
        donebtn=Button(root,text="Done",command=root.destroy, bg="blue",fg='white') 
        donebtn.pack(pady=20)
        
        root.mainloop()
        
        return l
    
    nra = Entry(root,font=font)
    nra.pack(fill=X)
    
    # addbtn=Button(root,text="+",command=partial(recadd, nra), bg="blue",fg='white',activebackground="green") 
    # addbtn.pack()
    
    w = Label(root, text="Subject", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=10)
   
    subject=Entry(root,font=font)
    subject.pack(fill=X,pady=20)

    w = Label(root, text="write your email", bg="black", fg="white")
    w.pack(fill=X, padx=10,pady=20)
   
    emailbody=Text(root)
    emailbody.pack(fill=X,pady=10)
    
    sendBtn=Button(root,text="SEND EMAIL",command=btnemailclick, bg="green",fg='white')
    sendBtn.pack()

    root.mainloop()

def dateTime():
    
    canvas = Tk()
    canvas.title("Digital Clock")
    canvas.geometry("400x400")
    canvas.resizable(1,1)
    
    hour= int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        wish=Label(canvas,text="Good Morning Shruti Maam!", fg="black", borderwidth=2, relief="raise")
     
    elif hour>=12 and hour<18:
        wish=Label(canvas,text="Good Afternoon Shruti Maam!", fg="black", borderwidth=2, relief="raise")
     
    else:
        wish=Label(canvas,text="Good Evening Shruti Maam!", fg="black", borderwidth=2, relief="raise")
    
    wish.pack(pady=20)
        
    wish=Label(canvas,text=date.today() , fg="black", font=font)
    wish.pack(pady=20)
    
    label = Label(canvas, font=("Courier", 30, 'bold'), fg="white", bd =30 , bg="black")
    label.pack(pady=20)
    
    def digitalclock():
        text_input = time.strftime("%H:%M:%S")
        label.config(text=text_input)
        label.after(200, digitalclock)
    digitalclock()
    
    canvas.mainloop()


def Calculator():

    cal= Tk()
    cal.geometry("270x570")
    cal.title("Calculator")
    # cal.call('wm', 'iconphoto', cal._w, PhotoImage(file='cal.png'))  #icon

    scvalue= StringVar()
    scvalue.set("")
    screen= Entry(cal,textvar=scvalue, font="lucida 30 bold")
    screen.pack(fill=X,padx=10,pady=10,ipadx=10)

    def click(event):
        
        text= event.widget.cget("text")  #event.widget=> gives button that has been clicked::: .cget("text")=> gives the text on the button
        print(text)  #print on click (on terminal)  #optional

        if text== "=":
            if scvalue.get().isdigit():
                value= int(scvalue.get())   #typecasting to int if it is adigit
            else:    #if it is not adigit but an expression as 2x3
                try:
                    value= eval(screen.get())  #eval func evaluates a string
                except Exception as e:
                    value= "Error !"
                    
            scvalue.set(value)     #seting value in scvalue
           
        elif text== "C":
            scvalue.set("")
           
        else:   #if it is a number
            scvalue.set(scvalue.get() + text)#setting sc value again
        
        screen.update()  #will update entry at screen with the new value every time


    l=[['9','8','7'],['6','5','4'],['3','2','1'],[['0','grey'],['-','black'],['+','black']],[['*','black'],['/','black'],['%','black']],[['.','black'],['=','green'],['C','red']]]
        
    for i in range(len(l)):
        
        #making a frame
        f= Frame(cal, bg="black")  
          
        for j in range(len(l[i])):
            
            if i>=3:
                
                b= Button(f, text=l[i][j][0], padx=15, bg=l[i][j][1], fg="white", pady=10, font="lucida 20 bold",relief="raise") 
                b.bind("<Button-1>", click)
                b.pack(side=LEFT, padx=5, pady=4)
                    
            else:
                #button inside frame f =>Button(f,)
                b= Button(f, text=l[i][j], padx=15, pady=10, bg="grey", fg="white",  font="lucida 20 bold",relief="raise")   
                #binding button to a click event before packing
                b.bind("<Button-1>", click)  
                b.pack(side=LEFT, padx=5, pady=4)

            # packing frame
            f.pack()     
    
def mic():
    r=sr.Recognizer() # recognizes the sound

    def speakText(command): #through this function it will simply speak or read out text
        engine=pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
        
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


def rps():

    def Spin():
        pick_no= randint(0,2) #pick random no.
        #show image
        compchoice.config(image=comp_choice[pick_no])   #to set anew img

        #0=Rock, 1=Paper, 2=scissors
        #conert dropdown choice to numbers
        if choice.get()== "Rock":
            choice_value= 0   #list index =0 for rock
        elif choice.get()== "Paper":
            choice_value= 1
        elif choice.get()== "Scissors":
            choice_value= 2

        #determine result:
        if choice_value== 0: #rock
            if pick_no ==0:
                result.config(text="It's a Tie ! Spin Again!")
            elif pick_no ==1:
                result.config(text="Paper Covers Rock ! You Lose!")
            elif pick_no==2:
                result.config(text="Rock Smashes Scissors ! You win!")

        if choice_value== 1: #paper
            if pick_no ==0:
                result.config(text="Paper Covers Rock ! You Win!")
            elif pick_no ==1:
                result.config(text="It's a Tie ! Spin Again!")
            elif pick_no==2:
                result.config(text="Scissors Cuts Paper ! You Lose!")

        if choice_value== 2: #scissors
            if pick_no ==0:
                result.config(text="Rock Smashes Scissors ! You Lose!")
            elif pick_no ==1:
                result.config(text="Scissors Cuts Paper ! You Win!")
            elif pick_no==2:
                result.config(text="It's a Tie ! Spin Again!")

    root= Tk()
    root.title('GAME: Rock, Paper, Scissors')
    # root.iconbitmap('')
    root.geometry("500x600")

    root.config(bg="palegreen")

    # rock= PhotoImage(file='rock.png')
    # paper= PhotoImage(file='paper.png')
    # scis =PhotoImage(file='sci.png')
    
    rock=Label(root,text="rock")
    paper=Label(root,text="paper")
    scis=Label(root,text="scissors")
    
    #list of images
    comp_choice= [rock, paper, scis]

    #rand no b/w 0-2 =>0,1,2
    pick_no =randint(0,2)

    #image on prog start
    compchoice= Label(root,text=comp_choice[pick_no],font="garamond 20 bold",bg="navy", fg="palegreen")
    compchoice.pack(pady=20)

    #dropdown
    choice= ttk.Combobox(root, value=("Rock","Paper","Scissors"))
    choice.current(0)  #for initial display as rock  #default
    choice.pack(pady=20)

    #spin button
    spinbtn= Button(root, text="SPIN", command=Spin, bg="darkgreen", fg="white", font="garamond 25 bold")
    spinbtn.pack(pady=20)

    result= Label(root, text="", font="garamond 20 bold", bg="palegreen", fg="navy")
    result.pack(pady=20)
    

root.mainloop()
text=Label(root,text="Welcome!", fg="black",font=font)
text.pack(pady=50)
    
sms= Button(root, text="Send a Message",command=message, bg="black", fg="white")
sms.pack(fill=X, padx=10,pady=20)


emailf= Button(root, text="Write an E-mail",command=email, bg="grey", fg="black")
emailf.pack(fill=X, padx=10,pady=20)


dt= Button(root, text="Check Date and Time",command=dateTime, bg="black", fg="white")
dt.pack(fill=X, padx=10,pady=20)


cal= Button(root, text="Calculator",command=Calculator, bg="grey", fg="black")
cal.pack(fill=X, padx=10,pady=20)

rpsg= Button(root, text="Check Date and Time",command=rps, bg="black", fg="white")
rpsg.pack(fill=X, padx=10,pady=20)

search= Button(root, text="Google search", bg="black", fg="white")
search.pack(fill=X, padx=10,pady=20)


# Creating a photoimage object to use image
photo = PhotoImage(file = r"mic.png")
  
# Resizing image to fit on button
photoimage = photo.subsample(3, 3)
  
# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
Button(root, image = photoimage,command=mic,compound = LEFT).pack(side = TOP)

text=Label(root,text="~created by Shruti Goyal and Shiva Dantre", fg="black")
text.pack(pady=80,side = BOTTOM)

root.mainloop()

