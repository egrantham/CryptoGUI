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
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')

# Global variables: key and length of the alphabet
key = 3
alphaLen = 26

########################################

def plotFreqs():
    plt.style.use('ggplot')
    
    charDict = Utilities.count()
    chars = [key for key in charDict.keys()]
    counts = [value for value in charDict.values()]

    # generate a list: (0,1,2,...,# of chars) for bar graph    
    x_pos = [i for i, _ in enumerate(chars)]
    
    plt.bar(x_pos, counts, color='green')
    plt.xlabel("Letters")
    plt.ylabel("Occurences")
    plt.title("Frequency of Letters in Text File")
    plt.xticks(x_pos, chars)
    
    plt.show()

def reset():
    # resets all values to default
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
        # Input Field   
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

        # Output Field
ttk.Label(tab1, text = "Ciphertext").grid(
        column = 0,
        row = 1)
outputField = ttk.Entry(tab1, textvariable = outputVar)
outputField.grid(
        column = 1,
        row = 1,
        padx = 30,
        pady = 30)

        # Key Entry Field
keyVar.set("3")

ttk.Label(tab1, text = "Key").grid(
        column = 0,
        row = 2)

ttk.Entry(tab1, textvariable = keyVar).grid(
        column = 1,
        row = 2,
        pady = 30)

        # Buttons
ttk.Button(tab1, text= "Change Key",command=setKey).grid(
        column = 2,
        row = 2) 

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

ttk.Button(tab2, text= "Browse", command=plotFreqs).grid(
        column = 0,
        row = 2)

tabControl.pack(expand = 1, fill ="both") 
root.mainloop()