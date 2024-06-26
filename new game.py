from socket import close
import time
import os

def Menu():
    print("Hi welcome to my text based game")
    print("This game is pritty self explanatory ")
    Play = input('''Please chose an option
    Continue
    New Game
Type option here ''')
    if Play == "Continue":
        test = open("test.txt","r")
        if test == "0":
            print("sorry there is no data please chose another option")
    elif Play == "New Game":
        L1()
        test = open("test.txt","w")
        test.write("1")
        test.close()
Menu()