from turtle import st
from Player import *
from Item import *
from Openables import *
from TextStuff import *
from Room import *
from time import sleep

#from Util import myPrint

p = Player("")

hall = Hall("the Hall")
front = Front("the Front Door Step")
study = Study("the Study")
lounge = Lounge("the Lounge")
dining = DiningRoom("the Dining Room")
billiard = BilliardRoom("the Billiard Room")
conservatory = Conservatory("the Conservatory")
ball = Ballroom("the Ball Room")
garden = Garden("the Garden")
library = Library("the Library")
kitchen = Kitchen("the Kitchen")
attic = Attic("the Attic")
bushes = Bushes("the Bushes")
crypt = Crypt("the Crypt")
back = Back("the Outside")


def startGame():

    print("welcome to the game")
    name = input("enter your name: ")
    p = Player
    p.name = name
    print("\nhello " + p.name)
    
    # print("\ndo you know why you are here?")
    
    # working = True
    # while working == True:
    #     yn = input("answer with 'yes' or 'no': ")

    #     if yn.lower() == "no":
    #         introduction()
    #         # describeHouse()
    #         break
    
    #     elif yn.lower()== "yes":
    #         print("\nGood. Then we can skip the backstory.")
    #         input("")
    #         print("Keep your wits about you.")
    #         input("")
    #         print("I wish you luck.")
    #         input("")
    #         input("\npress enter to continue... ")
    #         print("\n---------------------")
    #         skipBackstory()
            
    #         break

    #     else:
    #         print("that is not a valid answer, please try again.")



startGame()

hall.addDoor(front, "front door", True, "gold key")
p.room = hall
#p.enterRoom(hall)

hall.addDoor(study, "paneled door", True, "white key")
hall.addDoor(lounge, "solid wood door", True, "blue key")
hall.addDoor(dining, "double doors", True, "gold key")

study.addDoor(library, "white door", True, "red key")

lounge.addDoor(billiard, "green door", True, "yellow key")

library.addDoor(conservatory, "navy door", True, "gold key") 
library.addSeceretDoor(conservatory, "shelf", True, "navy key")

billiard.addDoor(kitchen, "grey door", True, "silver key" )

dining.addDoor(ball, "purple door", True, "grey key")
dining.addDoor(library, "red door", True, "purple key")

dining.addDoor(ball, "yellow door", True, "gold key")

ball.addDoor(kitchen, "black door", True, "shiny key")
ball.addDoor(conservatory, "glass door", True, "bronze key")
ball.addSeceretDoor(attic, "mirror", False, "none")

conservatory.addDoor(garden, "wrought iron door", True, "skeleton key")

garden.addDoor(back, "iron gate", True, "iron key")
garden.addSeceretDoor(bushes, "bushes", False, "none")

bushes.addCloseBehindYouDoor(crypt, "crypt door", True, "green key", "gold key")

#while what is true
while True:
    if p.room == back:

        if p.cursed == True:
            print("You made it out alive, but the curse is not broken!")
            sleep(1)
            print("Do you want to return to the house and try to break it?")

            choice = input("Type '1' to return to the garden. Type '2' to leave the house: ")
            if choice == "1":
                p.room = garden
            elif choice == "2":
                print("You make your way away from the house. Maybe the curse breaking is better done by someone else.")
            else:
                print("That is not one of the options. Please try again.")
        
        else:
            print("You broke the curse and made it out alive!")
            print("The town of Martinsville thanks you " +  p.name)
            print("")

        break
    if p.hp <= 0:
        print("your HP is 0! You died!")
        break

    else:
        print("")
        print(p.room.enter(p))
        print("")
        print("Items:")

        i = 1
        for item in p.room.locations:
            print(str(i) + '. ' + item.name)
            i += 1

        print("\nDoors:")
        for item in p.room.doors:
            print(str(i) + '. ' + item.name)
            i += 1
        print('Which would you like to inspect?')
        
        idx = input()
        print("")

#DIE
        if idx == "":
            print("Not a valid input!!!!")
        # elif type(int(idx)) != int:
        #     print("Not a valid input!!!!")
        elif int(idx) <= len(p.room.locations):
            print(p.room.locations[int(idx)-1].inspect(p) or "")
        elif int(idx) >= len(p.room.locations) and int(idx) <= len(p.room.locations)+len(p.room.doors):
            print(p.room.doors[int(idx)-len(p.room.locations)-1].inspect(p) or "")
        else:
            print("That is not a valid input, please try again.")

        if p.room != back:
            print("")
            input("Press Enter to continue...")
            print("")
    
