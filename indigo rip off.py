from os import name
from pickle import TRUE
from re import A
import time
import webbrowser
end = "no"
Death = "alive"
ramplush = False
mollyplush = False
collectible3 = False
collectible4 = False
collectible5 = False
complete = open("test.txt", "w")
complete.write("Well done for compleating the game")
complete.close()
def Maingame():
    global end
    while end != "Yes" and end != "Death1" and end != "Death2":
        print("You were urban exploring before you found and an abandond park and deided to enter it")
        option = input (''' You see an open door What do you do 
Enter the doorway [A]
Try move the rubble[B]
''')
        if option == "[A]":
            while end != "Yes" and end != "Death1" and end != "Death2":
                print("You enter the room")
                print('''you look around and see a TV screean
You walk towards the TV... 
it sodenly actavates and you see a racoon on the screen''')
                print("Hi im Rambally. Rambally the Racoon and welcome to indio park. to get registerd go to the regstration desk on your left")
                option = input('''What do you do?
Go to the desk on your left [A]
Brainlessly walk left  [B]
''')
                if option == "[A]":
                    print("Mhh let me just get a good look at you... mhh i dont recognise you please insert some details ~Rambally") 
                    time.sleep(2.0)
                    name = input("What is your name?")
                    print ("Hi", name, "Meet me at the main gate and i'll let you in")
                    time.sleep(1.0)
                    while end != "Yes" and end != "Death1" and end != "Death2":
                        print("Whats the hold up the gate should be open ... mhhhh my mistake the gate is not open seemes like an error boot up the genrator to get the gate up")
                        time.sleep(2.0)
                        option = input('''Should you turn on the Genrator?
No[A]
Yes[B]
''')
                        if option == "[A]":
                            print("... Nothing happend")
                            time.sleep(1.0)
                        elif option == "[B]":
                            print("You turn on the genrator and go back to the gate.")
                            time.sleep(1.0)
                            print("Alright for real this time Welcome to indigo park.")
                            time.sleep(0.5)
                            while end != "Yes" and end != "Death1" and end != "Death2":
                                option = input('''What do you want to do
Inspect Rambally plushy [A]
Inspect mysterious plushy [B]
Walk into the park [C]
''')
                                if option == "[A]" and not ramplush:
                                    print ("Well done you have collected the Rambally plushy")
                                    ramplush = True
                                    time.sleep(1.0)
                                elif option == "[A]" and ramplush:
                                    ("You have alreddy collected this plush")
                                    time.sleep(1.0)
                                elif option == "[B]" and not mollyplush:
                                    print("Well done you have collected the mysterious plushy")
                                    mollyplush = True
                                    time.sleep(1.0)
                                elif option == "[B]" and mollyplush:
                                    print("You have already collected this plush.")
                                    time.sleep(1.0)
                                elif option == "[C]":
                                    end = "Yes"
                                    print ("You enter the park")
                                    time.sleep(1.0)
                                    while end != "Yes" and end != "Death1" and end != "Death2":
                                        print("The enttrance clapses leaving you trapped inside the entrance")
                                        option = input('''where do you go?
into rambally railway? [A]
Try move the rubble[B]
''')
                                        if option == "[A]":
                                            webbrowser.open_new("https://youtu.be/kaZxq9I0zUQ?si=6on3TxXcsp8MrSRq")
                                            end = "Yes"
                                        if option == "[B]":
                                            Death = "crushed by bolders"
                                            end = "Death2"
                                else: print("Unable to do this action")
                        else: print("Please chose an option")
                        time.sleep(0.5)
                elif option == "[B]":
                    print("Buddy your going the rong way the regstration dest is this way (points to the left)")
                    time.sleep(0.9)
                else: print ("please chose [A] or [B] and tipe it in the square brakets.(please wait for next text before typing)")
        elif option == "[B]":
            Death = "bolders"
            end = "Death1"
        else:
            print ("please chose [A] or [B] and tipe it in the square brakets. (please wait for next text before typing)")
    time.sleep(1.0)
Maingame()
if end == "Death1":
    print ("You died to" , Death , "Close and reopen the game to try again")
if end == "Death2":
    print("Hey buddie wake up please.~Rambally. You died to",Death,"close and reopen to try again")
if end =="Yes":
    complete = open("test.txt", "a")
    complete.write(name)
    complete = open("test.txt", "r")
    print (complete.read())
    