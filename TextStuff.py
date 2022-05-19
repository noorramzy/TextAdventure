#for the random text of the game!
from time import sleep
from Player import *
#from Util import myPrint



def introduction():
    print("\nWell then " + Player.name + " welcome to Martinsville, Conneticut.")
    print("")
    input("press enter to continue... ")
    # print("\nI am the mayor, Toby Adams. I am also the one who hired you.")
    # input("")

    # print("A mile past the edge of town, there is an abandoned estate.\nIt belonged to the Dubois family.") 
    # print("Most recently, it was home to Pierre Dubois, and his... unique collection.") 
    # print("")
    # input("press enter to continue... ")
    # print("")
    # print("Dubois was an avid collector of artifacts. Especially those with more... supernatural components.")     

    # print("")
    # input("")
    # print("On November 17, 1992, however, Dubois suddenly dissapeared.")
    print("On November 17, 1992, Pierre Dubois, the owner of the Dubois estate up the hill mysteriously dissapeared.") 
    input("")
    print("Some poeple here like to say that a mystery man visiited that night, but no one is really sure what happened to him.")
    
    input("")
    
    print("Dubois was an avid collector of artifacts. Especially those that he though to be cursed or holy.")     
    input("")
    print("Ever since his dissapearance, the town has been plagued with misfortunes. We attribute it to the Dubois estate.")
    input("")
    print("The people of the town have tried to rid themselves of the curse of the Dubois Estate for many years, but no attempts have been successful.") 
    input("")
    print("The issue is, the only time anyone is able to enter the house is on the eve of Dubois's disspearance.")
    input("")
    print("The brave (or stupid, depending who you ask) voulenteers who try and break the curse from the source, often return... changed...")
    input("")
    print("If they return at all.")

    input("")

    print("Now, 30 years later, you have been hired to clear out the Dubois estate, and hopefully break the curse.")
    input("")
    print("The question is... are you brave enough to try?")
    print("")

    ans = input("type '1' to enter the house, or '2' to decline the challenge: ")

    if ans == "1":
        describeHouse()
    else:
        print("well then, I wish you luck in your return home. Please refer any other curse breakers you know to me.")

def describeHouse():
    print("")
    print("You make your way up an old stone path.")
    input("")
    print("Up ahead, you see a tall wrought iron gate.")
    input("")
    print("You push on the gate, and it swings open to reveal the facade of the Dubois manor.")

    
    print("")
    input("press enter to continue... ")
    print("")

    print("The dark brick exterior looms over you. As you step onto the front step, the large oak door swings open...")
    
    print("")
    input("press enter to step inside")
    print("")

    print("The entryway in front of you is dark... ")
    input("")
    print("As soon as you step across the threshold, the door slams shut behind you.")
    input("")
    print("You whirl around to face the door, and your flashlight lands on a lightswitch")
    input("")


    print("")
    input("press enter to try the lightswitch")
    print("")

    print("The lights slowly flicker on, revealing a large entrance hall, full of strange items.")
    input("")
    print("you look around, and take better stock of your bearings.")
    input("")
    print("To the West (left), a solid wood door stands closed. Next to it, a painting hangs.")
    input("")
    print("To the East (right), there is a paneled wood door, and a small console table with a vase on top.")
    input("")    
    print("To the North (ahead of you), there is are closed double doors.")
    input("")



def skipBackstory():
    print("\nYou make your way up to the house. It is desolate like the town people described.")
    input("")
    print("You pass through the open gate, and push on the door.")
    input("")
    print("It swings open easily.")
    input("")
    print("You step inside, and just as you cross the threshold, the door slams shut.")

    print("")
    input("press enter to continue...")

    print("")

    print("You push on the door, but it is locked.")
    input("")
    print("You feel along the wall, and find a lightswitch to your right.")
    input("")
    print("The light flickers on.")
    input("")
    print("You look around, and try to get your bearings.")
    input("")
    print("To the West (left), a solid wood door stands closed. Next to it, a painting hangs.")
    input("")
    print("To the East (right), there is a paneled wood door, and a small console table with a vase on top.")
    input("")    
    print("To the North (ahead of you), there is are closed double doors.")
    input("")

def describeHall():
    print("You look around, and try to get your bearings")
    input("")
    print("To the West (left), a solid wood door stands closed. Next to it, a painting hangs.")
    input("")
    print("To the East (right), there is a paneled wood door, and a small console table with a vase on top.")
    input("")    
    print("To the North (ahead of you), there is are closed double doors.")
    input("")

def describeStudy():
    print("You enter what seems to be Dubois's private study.")
    input("")
    print("You walk to the front of the room, where a large desk is covered in peices of paper.")
    input("")
    print("You turn to survey the room, the desk now behind you.")
    input("")
    print("To the West (left), there is a closed wood paneled door.")
    input("")
    print("To the East (right), a large armchair sits next to a fire place, still covered in soot.")
    input("")
    print("To the North (forward), a closed white door.") 

def describeLounge():
    print("You find yourself in a formal sitting room.")
    input("")
    print("You walk to the South of the room, where a large sword hangs from the wall.")
    input("")
    print("You turn and face North, surveying the room.")
    input("")
    print("A couch and chairs surround a coffee table which still has drink glasses on it...")
    input("")
    print("To the East (Right), there is a solid wood door.")
    input("")
    print("Next to it, there is a large cabinate.")
    input("")
    print("To the North (ahead), there is a dark green door with an ornate gold dornob.")
    input("")

def describeDining():
    print("You enter what seems to be the house's dining room.")
    input("")
    print("In the center of the room, there is a large table, fully set for a fancy meal.")
    input("")
    print("You circle it so that you are at the head, and can get a better grasp of your surroundings.")
    input("")
    print("Behind you (South), there are closed double doors.")
    input("")
    print("To the East of the room (Right), there is a large buffet cabinate, with many drawers.")
    print("Next to it, there is a slim door, painted dark red.")
    input("")
    print("To the West (Left) of the room, there is a door with a purple handle.")
    input("")
    print("Across the room from you (North), a large yellow door stands shut.")

def describeLibrary():
    print("You walk into a room with many shelves. The library.")
    input("")
    print("You walk to one side, and survey the room.")
    input("")
    print("Behind you (South), there is a closed white door.")
    input("")
    print("To the East (right), there is a stand alone shelf packed with books.")
    input("")
    print("To the North (ahead of you), there is a navy coloured door.")
    input("")
    print("To the West (left), there is a dark red door.")
    input("")
    print("Next to it, there is a shelf with only three books.")

def describeBilliard():
    print("You find your self in a room with a billiard table.")
    input("")
    print("To the East, there is a closed purple door.")
    input("")
    print("To the West, there is a wooden inlayed chest against the wall.")
    input("")
    print("To the South, there is a grey door. Next to it, a few items hang from a hook on the wall.")
    input("")
    print("To the North, there is a green door.")
    input("")
    print("In the center of the room, there is a billiard table set, ready to play.")

def describeBallroom():
    print("You enter a large room. It is the ballroom.")
    input("")
    print("To the East of the room, a ornately panneled wall. At the far end, there is a black door.")
    input("")
    print("To the West, there is a frosted glass door.")
    input("")
    print("At the center of the room there is a cello, a violin and a piano, ready for a band to play.")
    input("")
    print("At the South end of the room, a large gilded mirror spans the length of the wall.")

def describeKitchen():
    print("You enter the kitchen")
    input("")
    print("To the West, there is a wall with many cabinets.")
    input("")
    print("To the South, there is a grey door.")
    input("")
    print("To the West, there is a black door.")
    input("")
    print("To the North, there is a counter with a few drawers.") 
    input("")
    print("On the counter, there is a framed photo.")

def describeConservatory():
    print("You enter a warm room. It has many plants. It seems like a conservatory.")
    input("")
    print("To the West, there is a frosted glass door.")
    input("")
    print("To the East, there is a large shelf, it holds small potted plants")
    input("")
    print("To the North, there is a wrought iron door. To it's left, there is a stone lion stature.")
    input("")
    print("To the South, there is a navy door.")
    input("")
    print("In the center of the room, there is a glass table, with a white orchard on top.")

def describeGarden():
    print("You walk out of the conservatory, and into a large garden. The wrought iron door is now behind you.")
    input("")
    print("The plants are very overgrown, but you can make out a few objects.")
    input("")
    print("Around the perimeter of the garden, there is an iron fence.")
    input("")
    print("Directly ahead, to the North, you see a gate, that leads out of the house.")
    input("")
    print("To the West, there is a dense wall of bushes.")
    input("")
    print("To the East, there is a fountain. It has a statue of an angel in the middle.")
    
def describeAttic():
    print("You pass through the mirror into a small room.")
    input("")
    print("You look out the window, and realize you must be in the attic.")
    input("")
    print("You look around the room.")
    input("")
    print("To the South, the mirror you passed through.")
    input("")
    print("To the West, you see a map on the wall.")
    input("")
    print("To the North, there is a mirror identical to the golden one but with a silver frame.")
    input("")

def describeCrypt():
    print("You enter the crypt. In the center of the room, there is a wooden coffin.")
    input("")


def describeBushes():
    print("You push through the bushes, and find yourself in a small clearning, surrounded by the overgrown bushes.")
    input("")
    print("In front of you, there is a small stone building.")
    input("")
    print("Two columns that flank the stone door.")
    input("")

def curseBreak():
    print("You reach out and touch the cross.")
    print("Suddenly, from behind you, you hear a rustling sound.")
    print("You turn to look, and see a man covered in dust.")
    input("")
    print("'Who are you?' you ask")
    print("'I am Pierre Dubois!' he says, 'You have freed me, and broken the curse!")
    input("")
    print("Dubois explains that he had met with a mysterious antique dealer who promised him a very rare item.")
    print("However, the dealer was actually an evil wizard and locked Pierre Dubois in the walls of the crypt.")
    input("")
    print("You finally broke the curse of the Dubios estate! All that is left is to make it out...")

def madeItOutNotCurseFree():
    print("You made it out of the house alive!")
    print("however... the curse is not broken.")


