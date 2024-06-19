from os import name
from sys import _enablelegacywindowsfsencoding
import time
import webbrowser

def Welcome():
    name = open("test.txt", "r")
    print(name.read())
    option = input("These are your current pronowns do you want to change them?")
    if option == "yes" or option == "Yes" or option == "YES":
        name = open("test.txt","w")
        pronowns = input("what are your new pronowns?")
        name.write(pronowns)
        name = open("test.txt","r")
        print(name.read())
    elif option == "no" or option == "No" or option == "NO":
        name.close()
    else: print ("invalid input")
Welcome()