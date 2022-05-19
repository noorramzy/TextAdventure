
from numpy import take
from Item import *
from Door import Door, LockedDoor, SeceretDoor, SeceretLockedDoor, LockedBehindYouDoor
from Openables import OpenableThing, LockedOpenableThing
from TextStuff import describeAttic, describeBallroom, describeBilliard, describeBushes, describeConservatory, describeCrypt, describeDining, describeGarden, describeHall, describeKitchen, describeLibrary, describeLounge, describeStudy, madeItOutNotCurseFree
#from Util import myPrint


class Room:
    def __init__(self, name):
        self.name = name
        self.locations = []
        self.doors = []
        self.firstEntry = True
        self.firstEntryMessage = None
        self.firstEntryFunction = None

    def enter(self, player):
        player.room = self
        if self.firstEntry and (self.entryMessage or self.firstEntryFunction):
            self.firstEntry = False
            if self.firstEntryFunction:
                return self.firstEntryFunction()
            else: 
                return self.entryMessage
        elif self.entryMessage:
            return self.entryMessage
        else:
            return "You are now in " + self.name + ". Select items to inspect"

    def addDoor(self, otherRoom, name, isLocked, keyName):
        doorType = Door
        if isLocked:
            doorType = LockedDoor
        d = doorType(name, self, otherRoom, keyName)
        self.doors.append(d)
        otherRoom.doors.append(d)
    
    def addSeceretDoor(self, otherRoom, name, isLocked, keyName):
        doorType = SeceretDoor
        if isLocked:
            doorType = SeceretLockedDoor
        sd = doorType(name, self, otherRoom, keyName)
        self.locations.append(sd)
        otherRoom.locations.append(sd)
    
    def addCloseBehindYouDoor(self, otherRoom, name, isLocked, keyName, otherKeyName):
        doorType = LockedBehindYouDoor
        if isLocked:
            doorType = LockedBehindYouDoor
        cd = doorType(name, self, otherRoom, keyName, otherKeyName)
        self.locations.append(cd)
        otherRoom.doors.append(cd)

class Front(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = []

# def createHall():

#     r = Room("hall")
#     r.locations = []
#     return r

class Hall(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [Item("Painting"), OpenableThing("Table", [TakableThing("blue key")]), OpenableThing("Vase", [TakableThing("white key")])]
        
        self.locations[0].description = "A painting of a woman. She is wearing a gold cross necklace that glints as if made of metal in the dim light."

        self.locations[1].description = "A small console table, made of dark wood."

        self.locations[2].description = "A blue china vase."
        
        # self.firstEntryMFunction = describeHall
        self.entryMessage = "You are in the hall."

class Study(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("desk", [HolyItem("cross necklace", 2), TakableThing("red key")]), Item("papers on desk"), Item("armchair"), OpenableThing("firepalce", [Item("burned logs"), Item("charred note")]) ]
        self.locations[0].description = "A solid oak desk, strewn with papers. The main drawer seems to be slightly ajar."
        # self.locations[0].contents[0].description = "You notice how similar it looks to the one the woman is wearing in the Hall painting."
        self.locations[0].contents[1].description = "A red coloured key... what does it open?"
        
        self.locations[1].description = "A mess maps, floor plans, newspaper clippings and book pages. \nUpon closer inspection, you notice part of a handwritten note that had been torn out of a notebook. \nThe part that still is legible reads \n'CHECK THE CUPPOARD - '"
       
        self.locations[2].description = "A very comfortable looking armchair!"
        
        self.locations[3].description = "A stone fireplace stained by soot and ashes. \nYou lean down to try and see what is inside."
        self.locations[3].contents[0].description = "A pile of burned logs."
        self.locations[3].contents[1].description = "A charred peice of paper with a handwritten message. \nYou can barely make what little writing is not burned. It reads:\n'- IN THE KITCHEN. CHECK THE BUSHES AND FIND THE CROSS.' "

        self.firstEntryFunction = describeStudy
        self.entryMessage = "You are in the study."

class Lounge(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [HauntedItem("sword", 3), Item("coffee table"), OpenableThing("cabinate", [TakableThing("yellow key"), HolyItem("silver coin", 1)])]
        self.locations[0].description = "You reach out to touch the sword. \nYou finger grazes the tip of the sword, and suddenly you are flung agains the opposite wall.\nYour hand gushes blood."
        self.locations[1].description = "A coffee table with two drink glasses left half full, as if the people drinking were in a rush to leave."
        self.locations[2].description = "A large cabinate, it seems to mainly store silverware and drink glasses."
        
        self.firstEntryFunction = describeLounge
        self.entryMessage = "You are in the lounge"

class Library(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("sparse book shelf", [OpenableThing("Book 1", [TakableThing("navy key")]), HauntedItem("Book 2", 2), OpenableThing("Book 3", [TakableThing("purple key")])])]
        
        self.locations[0].description = "A bookshelf with only three books. The first is red, the second is black, and the thrid is green."
        self.locations[0].contents[0].description = "Book 1"
        self.locations[0].contents[1].description = "You grab the second book off the shelf. \nYou flip to the first page, but ink starts to bleed from the book. \nYou quickly drop the book, but the ink on your hands burns.\n"
        self.locations[0].contents[2].description = "Book 3"
        
        self.firstEntryFunction = describeLibrary
        self.entryMessage = "You are in the library"

class DiningRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("dining table", [HauntedItem("fruit salad", 2), HauntedItem("glass of water", 2), HauntedItem("fork", 1)]), OpenableThing("buffet", [Item("plates")])]
        
        self.locations[0].description = "A lavishly set dining table, complete with.... a full meal?"
        self.locations[0].contents[0].description = "You reach out to see if the fruits are real... but as soon as you touch the plate, you start to feel dizzy."
        self.locations[0].contents[0].description = "You grab a glass of water from the table. Suddenly your hand burns, and you drop the glass."
        self.locations[0].contents[0].description = "One of the forks is slightly askew. You go to straighten it, but as soon as your finger touches the fork, you loose feeling in your hand. "

        self.locations[1].description = "A large buffet with a few drawers. You open them to see what is inside."
        self.locations[1].contents[0].description = "A few china plates. They don't really do anything. "
        
        self.firstEntryFunction = describeDining
        self.entryMessage = "You are in the Dining Room"

class Attic(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [Item("Map"), HauntedItem("Silver Mirror", 30)]
        self.locations[0] = "A map of what seems to be the estate. It is similar to the one the mayor showed you/ \nYou notice that there seems to be an extra room in West of the garden."
        self.locations[1] = "You go to inspect the silver mirror. \nYou reach out to touch it, but you are sucked in. \nYou cannot escape, and fall into the darkness :( "
        
        self.firstEntryFunction = describeAttic
        self.entryMessage = "You are in the Attic"

class BilliardRoom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("chest", [HolyItem("rosary beads", 2), TakableThing("silver key")]), OpenableThing("hook", [TakableThing("grey key")]), HauntedItem("billiard table", 3)]
        
        self.locations[0].description = "An ornate wooden chest."

        self.locations[1].description = "A hook hanging on the wall. From it hangs a chain with a grey key at the end."
        self.locations[2].description = "You walk to the center of the room to look at the billiard table. \nSuddenly, one of the cues levatates, breaking the balls and whacking you on the head."

        self.firstEntryFunction = describeBilliard
        self.entryMessage = "You are in the Billiard Room"

class Ballroom(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("wall panels", [TakableThing("bronze key")]), OpenableThing("musical instruments", [TakableThing("shiny key")])]
         
        self.locations[0].description = "Painted panels on the wall."
        self.locations[1].description = "A collection of musical instruments in the center of the room."
 
        self.firstEntryFunction = describeBallroom
        self.entryMessage = "You are in the Ball Room"
    
class Kitchen(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("cuppoard", [TakableThing("shovel"), TakableThing("green key")]), OpenableThing("drawer", [HauntedItem("knife", 1)]), Item("photograph")]
        

        self.locations[0].contents[0].description = "You notice the shovel is covered in dirt."
        self.locations[0].contents[1].description = "The key ring has a tag that says 'garden'."

        self.locations[1].contents[0].description = "You reach for the knife, and suddenly it floats up and stabs you."

        self.locations[2].description = "A photograph of a young boy standing in front of some bushes."
        
        self.firstEntryFunction = describeKitchen
        self.entryMessage = "A dirty kitchen"

class Conservatory(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("lion statue", [TakableThing("skeleton key")]), HauntedItem("orchid", 2)]

        self.locations[0].description = "A stone statue of a lion roaring."
        self.locations[1].description = "You go to inspect the white orchid. \nThe second you touch it, however, the room fills with a poisonous gas. \nLuckily, you manage not to breath much in."
        
        self.firstEntryFunction = describeConservatory
        self.entryMessage = "You are in the Conservatory."


class Garden(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("fountain", [HolyItem("fountain water", 4), OpenableThing("angel statue", [TakableThing("iron key")])]), ]
        
        self.firstEntryFunction = describeGarden
        self.entryMessage ="You are in the Garden."

class Bushes(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [OpenableThing("potted plant",[TakableThing("small key")])]
        
        self.firstEntryFunction = describeBushes
        self.entryMessage = "You are in the bushes"

class Crypt(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = [LockedOpenableThing("coffin", [SuperDuperHolyThing("cross", 5), TakableThing("gold key")], "small key"), HauntedItem("suit of armour", 6)]

        self.locations[0].description = "A dark wood coffin"
        self.locations[1].description = "You go to inspect the suit of armor. \nAs you approach it, it pulls out its sword and stabs you :("

        self.firstEntryFunction = describeCrypt
        self.entryMessage ="You are in the crypt"


    # def enter(self, player):
    #     player.room = self
        
    #     Door("crypt door", Crypt("the Crypt"), Bushes("the Bushes"), "green key").isLocked = True
    #     Door("crypt door", Crypt("the Crypt"), Bushes("the Bushes"), "green key").keyName = "gold key"

    #     if self.firstEntry and (self.entryMessage or self.firstEntryFunction):
    #         self.firstEntry = False
    #         if self.firstEntryFunction:
    #             return self.firstEntryFunction
    #         else: 
    #             return self.entryMessage
    #     elif self.entryMessage:
    #         return self.entryMessage
    #     else:
    #         return "you are now in " + self.name + ". Select items to inspect"


class Back(Room):
    def __init__(self, name):
        super().__init__(name)
        self.locations = []
        
        self.entryMessage = madeItOutNotCurseFree
