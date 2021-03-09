# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:35:56 2021
Provides some supporting functions to be used in the main file

@author: Ethan
"""

def decipher(ciphertext, key, alphaLen):
    """
    Translate from ciphertext to plaintext using Caesar cipher
    """
    decoded = ''
    for i in range(len(ciphertext)):
        new = chr(ord(ciphertext[i])-key)
        if ord(new)<ord('a'):
            new = chr(ord(new)+alphaLen)
        decoded += new
    return decoded

def encipher(plaintext, key, alphaLen):
    """
    Translate from plaintext to ciphertext using Caesa cipher
    """
    encoded = ''
    
    for i in range(len(plaintext)):
        new = chr(ord(plaintext[i])+key)
        if ord(new)>ord('z'):
            new = chr(ord(new)-alphaLen)
        encoded += new
    return encoded    

def readFile():
    """
    Open up given file, return the text it contains
    """
    from tkinter.filedialog import askopenfilename
    filename = askopenfilename()
    f=open(filename)
    text = f.read()
    f.close()
    return text

def cleanString(text):
    """
    This function removes non-letter characters from the text.
    """
    cleanedText = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in text:
        if char in alphabet:
            cleanedText += char
    return cleanedText

def count():
    """Make dict of chars and counts of their occurences in input file. 
    For each character encountered, adjust the count."""
    
    text = cleanString(readFile()).lower()
    
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