from os import name
from sys import _enablelegacywindowsfsencoding
import time
import webbrowser

def Welcome():
    name = open("test.txt", "r")
    print(name.read())
    hi = input("These are your current pronowns do you want to change them?")
    if hi == "yes" or hi == "Yes" or hi == "YES":
        name = open("test.txt","w")
        pronowns = input("what are your new pronowns?")
        name.write(pronowns)
    elif hi == "no" or hi == "No" or hi == "NO":
        name.close()
    else: print ("invalid input")
Welcome()