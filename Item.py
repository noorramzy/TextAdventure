#from Util import myPrint

from TextStuff import curseBreak


class Item:
    def __init__(self, name):
        self.name = name
        self.description = ""

    def inspect(self, player):
        return self.description


class TakableThing(Item):
    def __init__(self, name):
        super().__init__(name)
        self.taken = False 
        
    def inspect(self, player):
        self.taken = True
   
    #check for takable thing - get rid of use from takable
        player.room.locations.remove(self)

        player.inventory.append(self)

        if self.description:
            return "You picked up the " + self.name + ". " + self.description
        else:
            return "You picked up the " + self.name
    
    def use(self, area):
        if area.locked == True:
            return ("not a useful action")


class HauntedItem(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.Haunted = True
        self.damage = damage
    
    def inspect(self, player):
        player.hp -= self.damage

        print(self.description)
        input("\npress enter to continue...\n")
        if player.hp > 0:
            return "THIS ITEM IS HAUNTED. You lost " + str(self.damage) + "HP. \nYOUR HP IS NOW " + str(player.hp)
        if player.hp <= 0:
            return "THIS ITEM IS HAUNTED."

class HolyItem(Item):
    def __init__(self, name, holyness):
        super().__init__(name)
        self.Holy = True
        self.holyness = holyness
    
    def inspect(self, player):
        player.hp += self.holyness
        player.room.locations.remove(self)

        # print(self.description)
        input("\npress enter to continue...\n")

        return "THIS ITEM IS HOLY, it will protect you from " + str(self.holyness) + "HP damage."


class SuperDuperHolyThing(HolyItem):
    def __init__(self, name, holyness):
        self.name = name
        self.description = ""
        self.Holy = True
        self.holyness = holyness

    def inspect(self, player):
        player.hp += self.holyness
        player.room.locations.remove(self)

        player.cursed = False

        curseBreak()

        print("curse broken")


