#from Util import myPrint

MAX_HP = 10

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = MAX_HP
        self.inventory = []
        self.room = None
        self.cursed = True
    
    def sayHello(self):
        return("Hello")

    def enterRoom(self, room):
        self.room = room

    def getInventory(self):
        return (self.inventory)

        

    


        

    
        






