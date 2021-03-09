# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:22:31 2021

@author: Ethan

The main idea of this project is to make use of my cryptography knowledge
to make a GUI in tkinter that performs various functions- caesar, one-time
pad, freq analysis.
"""

import tkinter as tk					 
from tkinter import ttk 
import Utilities

# Global variables: key and length of the alphabet
key = 3
alphaLen = 26

########################################

def printFreqs():    
# handle output to the GUI:
    charDict = Utilities.count()
    rowNum = 4
    colNum = 1
    
    for char in charDict:
        ttk.Label(tab2, text=""+char+": "+str(charDict[char])).grid(
                column = colNum,
                row = rowNum,
                padx = 20)
        rowNum += 1
        if rowNum > 10:
            rowNum -= 7
            colNum += 1

def reset():
    # just reset all values to default
    inputVar.set("")
    outputVar.set("")
    keyVar.set("3") 
    global key
    key = 3

def setKey():
    global key
    key = int(keyVar.get())
    
def setOutput():
    plaintext = inputField.get()
    ciphertext = Utilities.encipher(plaintext, key, alphaLen)
    outputVar.set(ciphertext)
    
def setInput():
    ciphertext = outputField.get()
    plaintext = Utilities.decipher(ciphertext, key, alphaLen)
    inputVar.set(plaintext)

# code to create all the stuff for GUI
root = tk.Tk() 
root.title("CryptoGUI")
root.geometry("450x350") 
tabControl = ttk.Notebook(root) 

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 

tabControl.add(tab1, text ='Caesar Cipher') 
tabControl.add(tab2, text ='Frequency Analysis')

keyVar = tk.StringVar()
outputVar = tk.StringVar()
inputVar = tk.StringVar()

    # Caesar Cipher tab
        # Input      
ttk.Label(tab1, text ="Plaintext").grid(
        column = 0,
        row = 0,
        padx = 30,
        pady = 30) 
inputField = ttk.Entry(tab1, textvariable = inputVar)
inputField.grid(
        column = 1,
        row = 0,
        padx = 30,
        pady = 30)

    # Output    
ttk.Label(tab1, text = "Ciphertext").grid(
        column = 0,
        row = 1)
outputField = ttk.Entry(tab1, textvariable = outputVar)
outputField.grid(
        column = 1,
        row = 1,
        padx = 30,
        pady = 30)

    # Key
keyVar.set("3")

ttk.Label(tab1, text = "Key").grid(
        column = 0,
        row = 2)

ttk.Entry(tab1, textvariable = keyVar).grid(
        column = 1,
        row = 2,
        pady = 30)

ttk.Button(tab1, text= "Change Key",command=setKey).grid(
        column = 2,
        row = 2) 
        # Buttons
ttk.Button(tab1, text= "Encipher",command=setOutput).grid(
        column = 1,
        row = 3,
        pady = 30) 

ttk.Button(tab1, text= "Decipher",command=setInput).grid(
        column = 0,
        row = 3,
        pady = 30) 

ttk.Button(tab1, text= "Reset All", command=reset).grid(
        column = 2,
        row = 3,
        pady = 30)

# Frequency Analysis tab
ttk.Label(tab2, text = "Please select a file for frequency analysis: ").grid(
        column = 0,
        row = 0,
        pady = 20)

ttk.Button(tab2, text= "Browse", command=printFreqs).grid(
        column = 0,
        row = 2)

tabControl.pack(expand = 1, fill ="both") 
root.mainloop()

#keeping this in case I need it? 

#ttk.Scale(tab1,from_ = 0, to = 26,  
#        orient = tk.HORIZONTAL) .grid(
#        column = 0,
#        row = 3,
#        padx = 30,

#        pady = 30)
#from functools import partial
#partial(encipher,inputField.get(),key))
#label1.grid(row = 10, column = 1)

#v1 = tk.DoubleVar() 
#  
#def show1():   
#      
#    sel = v1.get() 
#    keyLabel.config(text = sel, font =("Courier", 14))  