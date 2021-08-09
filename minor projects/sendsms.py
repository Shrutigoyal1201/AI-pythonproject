import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror

def send_sms(number,message):
    url = "https://www.fast2sms.com/dev/bulkV2"

    params= {
        "authorization":"NMVWgP7US6l5zIewbxCv3yYO0FuinfsZ4QHAdkBGc19marqh8jmh8L0rk1IPxEolCyeY2nvTFQzUWd9K",
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


def btnclick():
    num=textNumber.get()
    msg=textMsg.get("1.0",END)

    '''The first part, "1.0" means that the input should be read from line one, character zero (ie: the very first character). 
    END is an imported constant which is set to the string "end". The END part means to read until the end of the text box is reached. 
    The only issue with this is that it actually adds a newline to our input.
     So, in order to fix it we should change END to end-1c'''

    r=send_sms(num,msg)

    if r:
        showinfo("Status","Message sent successfully")
    else:
        showerror("Error","Something went wrong ;(")


root=Tk()
root.title("Message Sender")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
textNumber=Entry(root,font=font)
textNumber.pack(fill=X,pady=20)
textMsg=Text(root)
textMsg.pack(fill=X,pady=10)
sendBtn=Button(root,text="SEND MESSAGE",command=btnclick)
sendBtn.pack()

root.mainloop()



# Definition and Usage

#Requests module

# The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).


#json module

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# response.json() returns a JSON object of the result (if the result was written in JSON format, 
# if not it raises an error). Python requests are generally used to fetch the content from a particular resource URI. 
# Whenever we make a request to a specified URI through Python, it returns a response object.
# Now, this response object would be used to access certain features such as content, headers, etc. 


# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

