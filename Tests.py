from Util import myPrint

from Player import *
from Item import *
from Openables import *

def sayHello():
    p = Player("person")
    if p.sayHello() != "Hello":
        print("FAIL")



def seeIfItemHasAnAction():
    item = Item("box")   
    if len(item.listActions()) < 1:
        print("FAIL") 

def canIOpenBox():
    box = OpenableThing("Box", ["key"])
    if "take" in box.listActions():
        print("take should not be an option for closed box")
    if "open" not in box.listActions():
        print("open should be an option for closed box")

    box.open()
    
    if "open" in box.listActions():
        print("open should not be an option for open box")
    if "take" not in box.listActions():
        print("look should be an option for open box")
    if "close" not in box.listActions():
        print("close should be an option for open box")

    box.inspect()


def canITakeItem():
    key = TakableThing("Key")
    if "take" not in key.listActions():
        print("you should be able to take a takable item")
    if "drop" in key.listActions():
        print("you should not be able to drop an item you did not take")
    
    key.take()

    if "take" in key.listActions():
        print("you should not be able to take an item again")
    if "drop" not in key.listActions():
        print("you should  be able to drop an item you did take")

sayHello()

seeIfItemHasAnAction()

canIOpenBox()

canITakeItem()