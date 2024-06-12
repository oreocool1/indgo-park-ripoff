from os import name
import time
import webbrowser
end = "no"
Death = "alive"
while end != "Yes" and end != "Death1" and end != "Death2":
    print("You were urban exploring before you found and an abandond park anddeided to enter it")
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
                print ("Hi", name, "Meet me at the main gait and i'll let you in")
                #time.sleep(1.0)
                end = "Yes"
            elif option == "[B]":
                print("Buddy your going the rong way the regstration dest is this way (points to the left)")
                time.sleep(0.9)
            else: print ("please chose [A] or [B] and tipe it in the square brakets.(please wait for next text before typing)")
    elif option == "[B]":
        Death = "bolders"
        end = "Death1"
    else: print ("please chose [A] or [B] and tipe it in the square brakets. (please wait for next text before typing)")
    time.sleep(1.0)
if end == "Death1":
    print ("You died to" , Death , "Close and reopen the game to try again")
