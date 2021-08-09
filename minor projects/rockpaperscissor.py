from tkinter import *
from random import randint
from tkinter import ttk

from PIL import ImageTk,Image


def Spin():
    pick_no= randint(0,2) #pick random no.
    #show image
    image_label.config(image=image_list[pick_no])   #to set anew img

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

rock= ImageTk.PhotoImage(Image.open('rock.png'))
paper= ImageTk.PhotoImage(Image.open('paper.png'))
scis =ImageTk.PhotoImage(Image.open('scissors.png'))

#list of images
image_list= [rock, paper, scis]

#rand no b/w 0-2 =>0,1,2
pick_no =randint(0,2)

#image on prog start
image_label= Label(root,image=image_list[pick_no])
image_label.pack(pady=20)

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