# Copypasta Typer
import sys
import time
from tkinter import *
import pynput
from pynput.keyboard import Key, Controller
from pynput import keyboard



# Variables

ctrltrue = False
input = "base input"
charMax = 1000


# #tkinter part

mw=Tk()

mw.title('Copypasta Window')


# 3 subsections

tf = Frame(master=mw, height=400, width=600)
tf.grid(row=0, column=0, sticky="NESW", padx=20, pady=10)
tf.grid_columnconfigure(0, weight=1)
tf.grid_columnconfigure(2, weight=1)

mf = Frame(master=mw, height=100, width=600)
mf.grid(row=1, column=0, sticky="NESW", padx=20, pady=10)
mf.grid_columnconfigure(0, weight=1)
mf.grid_columnconfigure(3, weight=1)

bf = Frame(master=mw, height=100, width=600)
bf.grid(row=2, column=0, sticky="NESW", padx=20, pady=10)
bf.grid_columnconfigure(0, weight=1)
bf.grid_columnconfigure(4, weight=1)


# top frame

textBox = Text(master=tf)

textBox.grid(row=0, column=1)


# mid frame

label = Label(master=mf, text="Max Character Limit for Messaging: ")
label.grid(column=1, row=0)

resetLength = Entry(master=mf)
resetLength.insert(0, charMax)
resetLength.grid(column=2, row=0)

# bottom frame

b1 = Button(master=bf, text='Set',
 command=lambda: getInput()).grid(row=0, column=1, padx=5)


b2 = Button(master=bf, text='Quit',
 command=lambda:quit()).grid(row=0, column=2, padx=5)


b3 = Button(master=bf, text='Type',
 command=lambda:sendMessage(input)).grid(row=0, column=3, padx=5)





#keyboard functions


def getInput():
    global input
    global charMax

    input=textBox.get("1.0","end-1c")
    charMax = int(resetLength.get())

def on_press(key):
    global input
    keyboard = Controller()
    try:

        if key.char == ('['):   # Type Keybind
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
            print('[ works')
            sendMessage(input)


    except AttributeError:
        pass
        # print('special key {0} pressed'.format(key))

        

def on_release(key):

    # print('{0} released'.format(key))

    if key == keyboard.Key.esc:
        sys.quit()
        return False



def typeText(string):
    keyboard = Controller()
    keyboard.type(string)



def sendMessage(para):
    keyboard = Controller()
    i = para



    while True:


        typeText(i[:charMax]) # character reset
        
        i = i[charMax:]
        keyboard.press(Key.enter) # single enter rotation
        keyboard.release(Key.enter)

        if (len(i) == 0): # break condition
            break




with keyboard.Listener(
    
    on_press=on_press,
    on_release=on_release) as listener:

    mainloop() #runs interface

    listener.join()


listener = keyboard.Listener(
    on_press=on_press, 
    on_release=on_release)
listener.start
 