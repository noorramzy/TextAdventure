##integration time 
#204 26/4/2022
from Util import print

from Player import *
from Item import *
from Openables import *
from TextStuff import *
from Room import *

def startGame():
    introduction()

    p = Player("monty")

    #p.introduce()
    # will save name here from player input 

    #how to identify nrew room? What will happen here 

def tryingBox():
    p = Player("monty")

    box = OpenableThing("Box", ["key", "shoe"])
    print(box.inspect(p))

def tryingDoor():
    pass


tryingBox()






