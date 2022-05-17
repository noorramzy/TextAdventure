#from Util import myPrint

import imp
from Item import *
from Player import *

class OpenableThing(Item):
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents
        contents = []
        self.description = ""
    
    def inspect(self, player):
            for item in self.contents: 
                player.room.locations.append(item)
            
            string = self.name + " contains: " + ", ".join([item.name for item in self.contents]) + "\n"
            self.contents = []
            
            if self.description:
                return self.description + "\nYou checked the " + self.name + ". " + string
            else:
                return "You checked the " + self.name + ". " + string




class LockedOpenableThing(OpenableThing):
    def __init__(self, name, contents, keyName):
        self.name = name
        self.isLocked = True
        self.contents = contents
        contents = []
        self.keyName = keyName
        self.description = ""

    
    def inpect(self, player):
          if self.isLocked == True:
            for item in player.inventory:
                if item.name.lower() == self.keyName:
                    self.isLocked = False
                    for item in self.contents:
                        player.room.locations.append(item)
                    return "you opened the " + self.name + ". \nIt contains: " + ", ".join([item.name for item in self.contents])
            return "This" + self.name + " is locked, you need a key. \n if you have a key, make sure it is the right one"



            





            




