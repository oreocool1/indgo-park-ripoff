import time
import webbrowser
end = "no"
Death = "alive"
while end != "Yes" and end != "Death1" and end != "Death2":
    print("You were urban exploring before you found and an abandond park anddeided to enter it")
    option = input (''' You see an open door What do you do 
    Enter the doorway [A]
    Try move the rubble[B]''')
    if option == "[A]":
        print("You enter the room")
        print('''you look around and see a TV screean
        You walk towards the TV... 
        it sodenly actavates and you see a racoon on the screen''')
        print("Hi im rambally. Rambally the Racoon and welcome to indio park. to get registerd go to the regstration desk on your left")
    elif option == "[B]":
        Death = "bolders"
        end = "Death1"
if end == "Death1":
    print ("You died to" , Death , "Close and reopen the game to try again")
