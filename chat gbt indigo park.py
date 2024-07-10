from optparse import Option
from pickle import TRUE
import time
import webbrowser

# Global variables
end = "no"
Death = "alive"
ramplush = False
mollyplush = False
collectible3 = False
collectible4 = False
collectible5 = False
player_name = ""

# Prepare the file to write completion details
complete = open("test.txt", "w")
complete.write("Well done for completing the game\n")
complete.close()
def menu():
    opton = input('''
New Game [N]
Continue [C]''')
    if opton == ("N"):
        Maingame()
    elif opton == ("C"):
        Playerdata = open("DATA.txt", "r")
        

def Maingame():
    global end, Death, ramplush, mollyplush, player_name
    
    while end != "Yes" and end != "Death1" and end != "Death2":
        print("You were urban exploring before you found an abandoned park and decided to enter it")
        option = input('''You see an open door. What do you do? 
Enter the doorway [A]
Try to move the rubble [B]
''')

        if option == "A":
            while end != "Yes" and end != "Death1" and end != "Death2":
                print("You enter the room")
                print('''You look around and see a TV screen
You walk towards the TV...
It suddenly activates and you see a raccoon on the screen''')
                print("Hi, I'm Rambally. Rambally the Raccoon and welcome to Indigo Park. To get registered, go to the registration desk on your left")
                
                option = input('''What do you do?
Go to the desk on your left [A]
Brainlessly walk left [B]
''')
                
                if option == "A":
                    print("Let me just get a good look at you... I don't recognize you, please insert some details ~Rambally")
                    time.sleep(2.0)
                    player_name = input("What is your name? ")
                    print(f"Hi {player_name}, meet me at the main gate and I'll let you in")
                    time.sleep(1.0)
                    
                    while end != "Yes" and end != "Death1" and end != "Death2":
                        print("What's the hold-up? The gate should be open... my mistake, the gate is not open. Seems like an error, boot up the generator to get the gate up")
                        time.sleep(2.0)
                        option = input('''Should you turn on the generator?
No [A]
Yes [B]
''')

                        if option == "A":
                            print("... Nothing happened")
                            time.sleep(1.0)
                        elif option == "B":
                            print("You turn on the generator and go back to the gate.")
                            time.sleep(1.0)
                            print("Alright, for real this time. Welcome to Indigo Park.")
                            time.sleep(0.5)
                            
                            while end != "Yes" and end != "Death1" and end != "Death2":
                                option = input('''What do you want to do?
Inspect Rambally plushy [A]
Inspect mysterious plushy [B]
Walk into the park [C]
''')
                                
                                if option == "A" and not ramplush:
                                    print("Well done, you have collected the Rambally plushy")
                                    ramplush = True
                                    time.sleep(1.0)
                                elif option == "A" and ramplush:
                                    print("You have already collected this plush")
                                    time.sleep(1.0)
                                elif option == "B" and not mollyplush:
                                    print("Well done, you have collected the mysterious plushy")
                                    mollyplush = True
                                    time.sleep(1.0)
                                elif option == "B" and mollyplush:
                                    print("You have already collected this plush.")
                                    time.sleep(1.0)
                                elif option == "C":
                                    end = "Yes"
                                    print("You enter the park")
                                    time.sleep(1.0)
                                    
                                    while end != "Yes" and end != "Death1" and end != "Death2":
                                        print("The entrance collapses leaving you trapped inside the entrance")
                                        option = input('''Where do you go?
Into Rambally railway? [A]
Try to move the rubble [B]
''')
                                        
                                        if option == "A":
                                            webbrowser.open_new("https://youtu.be/kaZxq9I0zUQ?si=6on3TxXcsp8MrSRq")
                                            end = "Yes"
                                        if option == "B":
                                            Death = "crushed by boulders"
                                            end = "Death2"
                                else:
                                    print("Unable to do this action")
                        else:
                            print("Please choose an option")
                        time.sleep(0.5)
                elif option == "B":
                    print("Buddy, you're going the wrong way. The registration desk is this way (points to the left)")
                    time.sleep(0.9)
                else:
                    print("Please choose [A] or [B] and type it in the square brackets. (please wait for the next text before typing)")
        elif option == "B":
            Death = "boulders"
            end = "Death1"
        else:
            print("Please choose A or B DONT TYPE IT IN SQUARE BRACKETS!. (please wait for the next text before typing)")
        time.sleep(1.0)

Maingame()

if end == "Death1":
    print("You died to", Death, "Close and reopen the game to try again")
if end == "Death2":
    print("Hey buddy, wake up please. ~Rambally. You died to", Death, "close and reopen to try again")
if end == "Yes":
    complete = open("test.txt", "a")
    complete.write(player_name)
    complete.close()
    complete = open("test.txt", "r")
    print(complete.read())
    complete.close()