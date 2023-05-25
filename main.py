# Much of this is from Angela Wu from a Python Udemy Course, notably the images.

# You can edit the csv file as you want.
# You can edit the names for the labels in Label1 and Lavel2 a few lines under here
# You can also flip them around by changing the switch_around value from 1 to 0 or visa versa

# This requires PANDAS to handle the CSV data
# You can get it using the command prompt. If you have python, type in cmd:  pip install pandas
# If it doesnt download, look up how to get "pip" first.
# Finally you need python version 3+ to use this

import pandas
from tkinter import *
from tkinter.ttk import *
import random
import time
# Type \/ \/ \/
label1 = "Port"
label2 = "Name"
switch_around = 1
#  Type /\ /\ /\




score = 0




BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/ports.csv")
# TODO 1. Create a dictionary in this format:
newlist = {row.Ports: row.Names for (index, row) in data.iterrows()}
list = newlist
lista = []
listb = []

suba = []
subb = []

x = 0


for x in newlist:
    lista.append(x)
    listb.append(newlist[x])
size = len(lista)
print(lista)
print(listb)

if switch_around == 1:
    copya = lista
    copyb = listb
    lista = copyb
    listb = copya


def LoadEntry():
    pickword()


def LoadEntry2():

    global lista
    global listb
    global valuer

    del lista[valuer]
    del listb[valuer]
    pickword()






def pickword():
    global enword
    global frword
    global lista
    global listb
    global valuer
    global score
    canvas.itemconfig(image, image=logo_img)
    score += 1
    try:
        valuer = random.randint(0, len(lista) - 1)
        frword = lista[valuer]
        enword = listb[valuer]
        print(len(lista))
        print(len(listb))
    except:
        lista = []
        listb = []
        for x in newlist:
            lista.append(x)
            listb.append(newlist[x])
        valuer = random.randint(0, len(lista) - 1)
        frword = lista[valuer]
        enword = listb[valuer]
        print(f"{score} tries for {size} cards. Average {round((score/size), 3)}")
        score = 0

    finally:
        canvas.itemconfig(language, text=label1, font=("Arial", 36, "italic"))
        canvas.itemconfig(wiq, text=frword, font=("Arial", 48, "bold"))
        window.after(3000, lambda: changelanguage())

    # value = random.randint(0, len(lista) - 2)
    # frword = lista[value]
    # enword = listb[value]
    # print(len(lista))
    # print(len(listb))
    # canvas.itemconfig(language, text="French", font=("Arial", 36, "italic"))
    # canvas.itemconfig(wiq, text=frword, font=("Arial", 48, "bold"))
    # window.after(5, lambda: changelanguage())


def changelanguage():

    canvas.itemconfig(language, text=label2, font=("Arial", 36, "italic"))
    canvas.itemconfig(wiq, text=enword, font=("Arial", 48, "bold"))
    canvas.itemconfig(image, image=backimg)




window = Tk()
window.title("Flashcard")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR, height=1200, width=1200)


canvas = Canvas(width=1200, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
logo_img = PhotoImage(file="images/card_front.png")
backimg = PhotoImage(file="images/card_back.png")
image = canvas.create_image(600, 300, image=logo_img)
canvas.grid(column=1, row=1)
language = canvas.create_text(600, 180, text="FLASHCARDS", font=("Arial", 36, "italic"))
wiq = canvas.create_text(600, 330, text="Press The Red X to Start", font=("Arial", 48, "bold"))




newcanvas = Canvas(width=1200, height=200, highlightthickness=0, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
newcanvas.grid(column=1, row=2)

rightimage = PhotoImage(file="images/right.png")
buttonright = Button(newcanvas,  text="Search", command=LoadEntry2, width=100, image=rightimage)
buttonright.grid(column=0, row=0)

wrongimage = PhotoImage(file="images/wrong.png")
buttonwrong = Button(newcanvas, text="Search", command=LoadEntry, width=100, image=wrongimage)
buttonwrong.grid(column=2, row=0)

centercanvas = Canvas(newcanvas, width=500, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
centercanvas.grid(column=1, row=0)
window.mainloop()

pickword()
