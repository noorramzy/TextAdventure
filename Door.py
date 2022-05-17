
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
                    self.enter(player)
                    return "you unlocked the door and walked through\n" 
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
        self.enterRoom(player)
        return "You found a seceret passageway\n" 
           

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
                    self.enter(player)
                    return "You found a seceret passage way! \nUsing the " + self.keyName + ", you unlocked the door.\n" 
            return "You seem to be on to something, but you are missing a crucial item."
 
        else:
            return self.enter(player)







