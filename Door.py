
from tkinter import S
from Item import *
from Openables import *
from Room import *

#from Util import myPrint

class Door(OpenableThing):
    def __init__(self, name, roomOne, roomTwo, keyName): 
        self.name = name
        self.roomOne = roomOne
        self.roomTwo = roomTwo
        self.keyName = keyName


    def enter(self, player):
        if player.room == self.roomOne:
            return self.roomTwo.enter(player)
        else:
            return self.roomOne.enter(player)

    def inspect(self, player):
        return self.enter(player)
           

class LockedDoor(Door):
    def __init__(self, name, roomOne, roomTwo, keyName):
        self.name = name
        self.roomOne = roomOne
        self.roomTwo = roomTwo
        self.keyName = keyName
        self.isLocked = True

    def inspect(self, player):
        if self.isLocked:
            for item in player.inventory:
                if item.name.lower() == self.keyName:
                    self.isLocked = False
                    print("\n---------------------\n")
                    print("you unlocked the door using the  " + self.keyName + " and walked through\n" )
                    return self.enter(player)
            return "This door is locked, you need a key. \nIf you have a key, make sure it is the right one"
        
        else:
            return self.enter(player)



class LockedBehindYouDoor(Door):
    def __init__(self, name, roomOne, roomTwo, keyName, otherKeyName):
        self.name = name
        self.roomOne = roomOne
        self.roomTwo = roomTwo
        self.keyName = keyName
        self.otherKeyName = otherKeyName
        self.isLocked = True

    def inspect(self, player):
        if self.isLocked:
            for item in player.inventory:
                if item.name.lower() == self.keyName:
                    print("\n---------------------\n")
                    print("you unlocked the door using the  " + self.keyName + " and walked through\n" )
                    self.keyName = self.otherKeyName
                    return self.enter(player)
            return "This door is locked, you need a key. \nIf you have a key, make sure it is the right one"
        else:
            return self.enter(player)



class SeceretDoor(Door):
    def __init__(self, name, roomOne, roomTwo, keyName): 
        self.name = name
        self.roomOne = roomOne
        self.roomTwo = roomTwo
        self.keyName = keyName


    def enter(self, player):
        if player.room == self.roomOne:
            return self.roomTwo.enter(player)
        else:
            return self.roomOne.enter(player)

    def inspect(self, player):
        print("You found a seceret passageway\n")
        self.enter(player)
        return "" 
           

class SeceretLockedDoor(SeceretDoor):
    def __init__(self, name, roomOne, roomTwo, keyName):
        self.name = name
        self.roomOne = roomOne
        self.roomTwo = roomTwo
        self.keyName = keyName
        self.isLocked = True

    def inspect(self, player):
        if self.isLocked:
            for item in player.inventory:
                if item.name.lower() == self.keyName:
                    self.isLocked = False
                    print("You found a seceret passage way! \nUsing the " + self.keyName + ", you unlocked the door.\n")
                    self.enter(player)
                    return ""
            return "You seem to be on to something, but you are missing a crucial item."
 
        else:
            return self.enter(player)







