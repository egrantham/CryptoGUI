# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:35:56 2021

@author: Ethan
"""

def decipher(ciphertext, key, alphaLen):
    decoded = ''
    for i in range(len(ciphertext)):
        new = chr(ord(ciphertext[i])-key)
        if ord(new)<ord('a'):
            new = chr(ord(new)+alphaLen)
        decoded += new
    return decoded

def encipher(plaintext, key, alphaLen):
    encoded = ''
    
    for i in range(len(plaintext)):
        new = chr(ord(plaintext[i])+key)
        if ord(new)>ord('z'):
            new = chr(ord(new)-alphaLen)
        encoded += new
    return encoded    

def getFile():
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename()
    f=open(filename)
    text = f.read()
    f.close()
    return text

def count():
    """Make dict of chars and counts of their occurences in input file. 
    For each character encountered, adjust the count."""
    
    text = getFile().lower()
    
    # keys are chars, values are # of occurences
    charDict = {}
    
    for letter in text:
        if letter in [' ', ',', '.', ';', "'"]:
            pass
        elif letter not in charDict.keys():
            charDict[letter] = 1
        else:
            charDict[letter] += 1
    return charDict
            