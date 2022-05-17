# Made by Dominik Kujawa.

# Annotated Map For Myself.
# |-----|  |-----|  |-----|
# |     |--|     |--|     | Bedroom, Altar Room, Ruined Staircase.
# |-----|  |-----|  |-----|
#             |        |
#             |        |
# |-----|  |-----|  |-----|
# |     |--|     |--|     | Prison, Courtyard, Hallway.
# |-----|  |-----|  |-----|
#    |        |        |
#    |        |        |
# |-----|  |-----|  |-----|
# |     |  |     |  |     | Tower 1, Inner Hall, Tower 2.
# |-----|  |-----|  |-----|
#             |
#             |
#          |-----|
#          |  ?  | Entrance Hall                                                                                                                                                                                                                    zoe
#          |-----|

# Imports.
import time as tm
import random as rng
import sys

# Explanation, real quick.
# '' means nothing, that's empty.
# Sometimes i use bruhmoment and bruhunmoment as true or false variables, because I got bored. They mean true or false.
# I haven't seen the light of day in 5 years.

# Defining Variables.

prisonItems = ['steel bar']
# The steel bar is used to bust open the prison cell door.

tower1Items = ['satchel']
# The satchel allows the player to hold more than 1 item at a time, and doesn't technically count as an item.

tower2Items = ['suspicious book']
# The book is used to open up tower1

courtItems = ['']

bedItems = ['strange tablet']
# strange tablet is used to activate the altar.

entranceItems = ['']

innerItems = ['']

altarItems = ['small orb']
# Small orb is used to change the fountain to a bloody fountain in the courtyard.

rstairItems = ['bucket']
# Bucket is used to get the blood filled bucket, which is used to activate the altar.

hallItems = ['']
# These are all of the room items. Descriptions for rooms that have items.
# If an item is shown as '' that means there is no item in that list.

prisonNotes = ['memory loss']
tower1Notes = ['']
tower2Notes = ['']
courtNotes = ['strange mechanism']
bedNotes = ['my last goodbye']
entranceNotes = ['not a way out']
innerNotes = ['']
altarNotes = ['ritual instructions']
rstairNotes = ['a way up no more']
hallNotes = ['']
# And these are all of the notes found in rooms!
# The reason they're a seperate variable is because notes don't count as items.
# You can't drop them, and they're not put in the satchel or heldItem.
# Instead, they're put in the journal.

challenge = 'false'
# This determines if challenge mode is active.
# It's set to false, unless the player inputs in a code at the start of the game

global ritual
ritual = 0
# This is responsible for seing if the ritual is active.
# The ritual is responsible for opening the front gate, and letting the player finish the game.

bloodFountain = 'false'
# This determines if the fountain has water or blood in it.

global vaultnote
vaultnote = rng.randint(1000, 9999)
# this is a number which is put into a note.
# the number is randomly generated each playthrough.
# it's used for the tablet at the end of the game.

# Map variables, as they are at the start.
# So, hidden, essentially.
# ""Passage"" parts of the map are the parts in between the rooms -
# Essentially the parts ""under"" the rooms.
# All of the rooms have two parts to them, as well as having 3 different states, with the exception of passages -
# passages only have 2 states, while having technically 8 parts - 3 for the uppermost passage, 3 for the middle passage, and 2 for the lower passage.
# The 3 states of the rooms are as follows:
# Hidden - The default except for the prison (as it's the start area) - a bunch of question marks hiding the room; A Fog of War, if you will.
# Shown - This basically displays the fact that the room exists and, essentially, Just shows the room as it is.
# Current Location - This only applies to a part 2 (P2) of rooms - It shows that the player is inside that room.
# Rooms are seperated into two parts - P1, which is basically the top and bottom, and P2, which is the middle.
bedMapP1 =(
"????????"
)
bedMapP2 =(
"????????"
)

altarMapP1 =(
"?????????"
)
altarMapP2 =(
"?????????"
)

rstairMapP1 =(
"????????"
)
rstairMapP2 =(
"????????"
)

courtyardMapP1 =(
"?????????"
)
courtyardMapP2 =(
"?????????"
)

hallMapP1 =(
"????????"
)
hallMapP2 =(
"????????"
)

tower1MapP1 =(
"????????"
)
tower1MapP2 =(
"????????"
)

innerMapP1 =(
"?????????"
)
innerMapP2 =(
"?????????"
)

tower2MapP1 =(
"????????"
)
tower2MapP2 =(
"????????"
)

entranceMapP1 =(
"???????"
)

entranceMapP2 =(
"???????"
)
mapLeftPassage1 =(
"????????"
)
mapMidPassage1 =(
"?????????"
)
mapRightPassage1 =(
"????????"
)

mapLeftPassage2 =(
"   |    "
)

mapMidPassage2 =(
"?????????"
)
mapRightPassage2 =(
"????????"
)
mapLeftPassage3 =(
"??????????????????"
)
mapMidPassage3 =(
"???????"
)
prisonMapP1 =(
"|-----| "
)
prisonMapP2 =(
"|  0  |-"
)
mapLeftPassage1 =(
"        "
)

global towerOpen
towerOpen = 'false'
# This tells the player if they can enter tower1 or not.

global Journal
Journal = ['']
# This saves the player's findings such as notes.
# This doesn't necessarily work as an inventory system, rather, what the character writes down/finds. Used for Lore.

global heldItem
heldItem = ['']
# Item currently in the player's hand.

global satchelItems
satchelItems = ['bedroom key']
# Items in the satchel.
# The Satchel is like an extended inventory, limited to 3 items.

global roomin
roomin = 'prison'
# The room the player is in. In this case, they start in the prison room.

global stuck
stuck = 'true'
# This determines if the player is currently able to move between rooms. Enough said.

global satchelobtain
satchelobtain = 'false'
# This tells the game if the player has the satchel.
# false means they don't, true means they do. Start without it.

global bedlocked
bedlocked = 'true'
# This says if the bedroom is locked or not.

# This is used to clear space, so that the player's screen doesn't get cluttered with text.
def clear():
    print("\n" * 100)

# This is used to set the reading speed. Player can change this at any time during gameplay.
def readingSpeedSet():

    global rspd
    rspd = 16
# This sets reading speed (rspd) to global so i can use it anywhere i want.
# I use this (global and reading speed) a few times.
# This also sets it to 16 so the while statement below this comment is true.

    while rspd >= 16 or rspd <=1:
        try:
            rspd = int(input("""
Please set the read speed.
this will affect the speed at which text progresses.
This can be changed at any time, by performing the action 'set speed'
The time is in seconds. Please only use numbers. The max is 15, and the minimum is
2 to ensure you're able to read everything.
""")) # This asks the player what they want to set their reading speed to.
            if rspd >= 16 or rspd <=1:
                clear()
                print("Please pick a number between 1-16")
            # This is in case the player picks a number that I deem too large or too small.
            # I don't want the player to miss text on accident.

        except ValueError:
            print('Use a Number') # This runs if the player doesn't pick a number, because some people try to be smart.







# These are all the actions that the player can do.
def actions():
    # this sets the correct variables to global. These have all been explained beforehand.
    global satchelobtain
    global challengeTimer
    global stuck
    global towerOpen
    global bloodFountain
    global vaultnote
    global ritual
    global challenge
    clear()
    # This asks the player if they want to view the map on room entry.
    # runs a while loop that, while false, will keep asking the player until they say yes or no.

    mapViewH = 'false'
    while mapViewH == 'false':
        clear()
        mapView = input("""Would you like to view the map?
""").lower()
        if mapView == 'yes' or mapView == 'y':
            mapViewH = 'true'
            map()
        elif mapView == 'no' or mapView == 'n':
            mapViewH = 'true'
    gone = 'false'
    while gone != 'true':
        if challenge == 'true':
            # this checks if challenge mode is on and decreases the amount of moves the player has left after each action if it is.
            challengeTimer = challengeTimer - 1
            if challengeTimer == 0:
                # This is basically a game over.
                clear()
                print("""You try to make it through the castle. After walking for what feels like an eternity,
your weak body collapses. You've failed, and you only have yourself to blame.
Game Over.""")
                tm.sleep(rspd)
                sys.exit()
        clear()
        roomaction = input("""What do you want to do?
""").lower() # This asks the player what they want to do, obviously
# This runs in a while loop so the player can continue doing actions until they move in which case gone will be set to true until they enter another room.
        if roomaction == 'move' and stuck == 'true':

            clear()
            print('You are currently unable to move')
            tm.sleep(rspd)
            # This basically tells the player they can't move. Used only in prison, basically.

        elif roomaction == 'move':

            clear()
            youreHereOff()
            gone = 'true'
            moverooms()
            tm.sleep(rspd)
            # This allows the player to move, by running the moverooms function.

        elif roomaction == 'search':
# This prints a short passage. The main use of this is to display items in the room.
            clear()
            searchingRoom()
            tm.sleep(rspd)

        elif roomaction == 'pick up':
# This runs the pickingUp script, which refers to the pickup script, etc.
            clear()
            pickingUp()
            tm.sleep(rspd)
            clear()

        elif roomaction == 'check map':
# This allows the player to check the map, running the map function.
            map()

        elif roomaction == 'check inventory':
# This allows the player to check their inventory.
# It displays their held item, as well as the items in their satchel, if they have it.
            clear()
            # this runs if the player isn't holding anything.
            if heldItem[0] == '':
                print("You aren't currently holding anything")
                if satchelobtain == 'true' and '' not in satchelItems:
                    print("""You do however have the following in your satchel :
{}""".format(satchelItems[0:])) # this runs if, the player actually has something in their satchel.
                elif satchelobtain == 'true' and '' in satchelItems:
                    print("You also have nothing in your satchel.") # and this runs if they have nothing in their satchel.
                tm.sleep(rspd)

            # this runs if the heldItem is something other than nothing.
            elif heldItem[0] != '':
                print("You're holding a {}".format(heldItem))
                if satchelobtain == 'true' and '' not in satchelItems:
                    print("""You also have the following in your satchel :
{}""".format(satchelItems[0:])) # same as above.
                elif satchelobtain == 'true' and '' in satchelItems:
                    print("You also have nothing in your satchel.") # same as above.
                tm.sleep(rspd)
            clear()

        elif roomaction == ('use {}'.format(heldItem[0])):
            clear()
# This runs the use function so that the player can use an item!
# They can only use the item they're holding - the {} is just for added interaction.

            # This allows the player to break out of their prison cell at the start.
            # They need the steel bar for it.
            if roomin == 'prison' and 'steel bar' in heldItem and stuck == 'true':
                print("You use the steel bar to break the prison cell open. You can now move.")
                stuck = 'false'
                tm.sleep(rspd)

            # This allows the player to open the western-tower doo.
            # They need the suspicious book, which gets consumed after use.
            elif roomin == 'prison' and 'suspicious book' in heldItem and towerOpen == 'false':
                print("""You put the book on the bookshelf. Suddenly, the tower door springs open.
you can now enter the tower.""")
                heldItem.remove('suspicious book')
                heldItem.append('')
                tm.sleep(rspd)
                towerOpen = 'true'

            # This allows the player to change the fountain water from water to blood.
            # I like to call this one 'Jesus'.
            # They need the small orb which gets consumed after use.
            elif roomin == 'courtyard' and 'small orb' in heldItem and bloodFountain == 'false':
                print("""You insert the circular orb into the mouth of the creature on the fountain.
suddenly, the water turns red. You assume it's blood. Maybe now it could be of some use.""")
                heldItem.remove('small orb')
                heldItem.append('')
                tm.sleep(rspd)
                bloodFountain = 'true'

            # This allows the player to fill the bucket with blood.
            # This only works if the fountain is filled with blood.
            # This requires a bucket, which gets turned into a blood bucket. (bucket filled with blood was too wordy.)
            elif roomin == 'courtyard' and 'bucket' in heldItem and bloodFountain == 'true':
                print("You fill the bucket with blood.")
                heldItem.append('blood bucket')
                heldItem.remove('bucket')
                tm.sleep(rspd)

            # This gives the player a hint that they need to do something with the fountain.
            # It doesn't fill the bucket with water, but it gives the player a hint that they're on the right track.
            # Not diverting them from the fountain, but also telling them that they should experiment with it.
            elif roomin == 'courtyard' and 'bucket' in heldItem and bloodFountain == 'false':
                print("""You feel as if there's no use for filling the bucket with water.
Maybe if the fountain dispensed a different liquid...""")
                tm.sleep(rspd)

            # This allows the player to use the blood bucket on the altar to do a part of the ritual.
            # it adds one to the ritual count, and if that count reaches 2, the game finishes, referring to the endGame function.
            elif roomin == 'altar' and 'blood bucket' in heldItem:
                print("""You pour the blood into the slot in the altar. It glows red.
the bucket mysteriously breaks in front of your eyes. It's clearly of no more use.""")
                ritual = ritual + 1
                heldItem.remove('blood bucket')
                heldItem.append('')
                tm.sleep(rspd)
                if ritual == 2:
                    endGame()

            # Same here but with the tablet.
            # This refers back to the vaultnote variable
            # Which is called vaultnote because vaults are secure, and it's a somewhat secure code, which can't be brute-forced unless you have a l o t of time.
            # Gets rid of the tablet if done correctly.
            elif roomin == 'altar' and 'strange tablet' in heldItem:
                try:
                    # This asks the palyer to input in a code.
                    codeRightWrong = int(input("""You place the tablet on the altar. It glows a light blue.
The tablet has numbers on it. It seems as if you need to input in a few.
what numbers do you put in? : """))
                    if codeRightWrong == vaultnote:
                        # This runs if the code is correct.
                        print("The tablet starts gently vibrating.")
                        tm.sleep(rspd)
                        ritual = ritual + 1
                        heldItem.remove('strange tablet')
                        heldItem.append('')
                        if ritual == 2:
                            endGame()
                    else:
                        # This happens if the player doesn't enter the correct passcode.
                        print("Nothing happens.")
                        tm.sleep(rspd)
                # This runs if the player doesn't enter a number.
                except ValueError:
                    print("You try to find letters on the tablet, yet you can't. The code, obviously fails.")
                    tm.sleep(rspd)

            else:
                clear()
                print("You cannot use this item, at least not here, or you're not holding anything.")
                tm.sleep(rspd)
            clear()

        elif roomaction == 'set speed':
# This refers to the readingSpeedSet function used at the start of the game.
# In case the player decides they don't like the speed they chose.
            clear()
            readingSpeedSet()
            tm.sleep(rspd)

        elif roomaction == 'drop':
# This refers to the dropping function which then uses the drop function etc.
            clear()
            dropping()
            tm.sleep(rspd)

        elif roomaction == 'help':
# This displays the help menu.
            clear()
            help()

        elif roomaction == 'take from satchel':
            # This allows the player to take items from the satchel, if they have it.
            if satchelobtain == 'true':
                clear()
                takeItem()
            # this runs if the player doesn't have a satchel.
            else:
                clear()
                print("You don't have a satchel to take from.")
                tm.sleep(rspd)

        elif roomaction == 'store':
            # This allows the player to put an item in the satchel if they have it.
            if satchelobtain == 'true':
                clear()
                storeItem()
            # this runs if the player doesn't have a satchel.
            else:
                clear()
                print("You don't have anything to put items in.")
                tm.sleep(rspd)

        # This runs the look around function, giving a description of the room they're in.
        elif roomaction == 'look around':
            clear()
            lookAround()

        # This runs the readingNotes function which refers to the readNote function which alows the player to
        # 1. read the note in the room.
        # 2. add the note to their journal.
        elif roomaction == 'read':
            clear()
            readingNotes()

        # This runs the journal function so the player can check their journal.
        elif roomaction == 'check journal':
            clear()
            JournalF()

        elif roomaction == 'swap':
            clear()
            swapItems()

        # This allows the player to view how many moves they have left in challenge mode.
        # It doesn't consume any moves, and is the only action that doesn't do so.
        elif roomaction == 'check moves' and challenge == 'true':
            clear()
            # This runs on 25 or more moves left.
            if challengeTimer >= 25:
                print("You still have time left. {} moves.".format(challengeTimer))
                tm.sleep(rspd)
                clear()
                # This runs between 25 and 15 moves left.
            elif challengeTimer < 25 and challengeTimer > 15:
                print("You're running out of time. {} moves.".format(challengeTimer))
                tm.sleep(rspd)
                clear()
                # This runs between 16 and 5 moves left.
            elif challengeTimer <= 15 and challengeTimer > 5:
                print("You're slowly fading away. {} moves.".format(challengeTimer))
                tm.sleep(rspd)
                clear()
                # This runs on 5 moves left and under.
            elif challengeTimer <= 5:
                print("Every second counts. {} moves.".format(challengeTimer))
                tm.sleep(rspd)
                clear()
            challengeTimer = challengeTimer + 1










# This is the map of the place, as printed in-game.
# It calls back to different variables in the map.
def map():
    clear()
    print("""{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}{}
{}{}
{}{}
{}{}
{}{}
""".format(bedMapP1, altarMapP1, rstairMapP1,
bedMapP2, altarMapP2, rstairMapP2,
bedMapP1, altarMapP1, rstairMapP1,
mapLeftPassage1, mapMidPassage1, mapRightPassage1,
prisonMapP1, courtyardMapP1, hallMapP1,
prisonMapP2, courtyardMapP2, hallMapP2,
prisonMapP1, courtyardMapP1, hallMapP1,
mapLeftPassage2, mapMidPassage2, mapRightPassage2,
tower1MapP1, innerMapP1, tower2MapP1,
tower1MapP2, innerMapP2, tower2MapP2,
tower1MapP1, innerMapP1, tower2MapP1,
mapLeftPassage3, mapMidPassage3,
mapLeftPassage3, entranceMapP1, mapLeftPassage3,
entranceMapP2, mapLeftPassage3, entranceMapP1))
    tm.sleep(rspd)


# These are all rooms.
# They are all essentially carbon copies of each over, with different names.
# Most of the room differences are in functions (Pick up, Use, Read, etc.)

def altar():
    global roomin
    global altarMapP2
    altarMapP2 =(
"-|  0  |-"
    )
# This tells the map to show that the player is in this room
    roomin = 'altar'
# This tells the game what room the player is in.
    actions()
# This runs the actions function which, well, allows the player to perform actions. wow.

def bedroom():
    global roomin
    global bedMapP2
    bedMapP2 =(
"|  0  |-"
    )
    roomin = 'bedroom'
    actions()

def staircase():
    global roomin
    global rstairMapP2
    rstairMapP2 =(
"-|  0  |"
    )
    roomin = 'staircase'
    actions()

def hallway():
    global roomin
    global hallMapP2
    hallMapP2 =(
"-|  0  |"
    )
    roomin = 'hallway'
    actions()

def prison():
    global roomin
    global prisonMapP2
    prisonMapP2 =(
"|  0  |-"
    )
    roomin = 'prison'
    actions()

def courtyard():
    global roomin
    global courtyardMapP2
    courtyardMapP2 =(
"-|  0  |-"
    )
    roomin = 'courtyard'
    actions()

def tower1():
    global roomin
    global tower1MapP2
    tower1MapP2 =(
"|  0  | "
    )
    roomin = 'tower1'
    actions()

def tower2():
    global roomin
    global tower2MapP2
    tower2MapP2 =(
    " |  0  |"
    )
    roomin = 'tower2'
    actions()

def inner():
    global roomin
    global innerMapP2
    innerMapP2 =(
    " |  0  | "
    )
    roomin = 'inner'
    actions()

def entrance():
    global roomin
    global entranceMapP2
    entranceMapP2 =(
    "|  0  |"
    )
    roomin = 'entrance'
    actions()

# THis is the function responsible for changing a map state from
# 'You are here' to 'This room exists.'
# What these do is just change the way the map is printed. There's nothing much to explain.
# It defines all of the variables as global so that they're not treated as local ones, yada yada.
def youreHereOff():
    global altarMapP2
    global entranceMapP2
    global innerMapP2
    global tower2MapP2
    global tower1MapP2
    global prisonMapP2
    global courtyardMapP2
    global hallMapP2
    global rstairMapP2
    global bedMapP2
    if roomin == 'entrance':
        entranceMapP2 =(
        "|     |"
        )
    elif roomin == 'inner':
        innerMapP2 =(
        " |     | "
        )
    elif roomin == 'tower2':
        tower2MapP2 =(
        " |     |"
        )
    elif roomin == 'tower1':
        tower1MapP2 =(
        "|     | "
        )
    elif roomin == 'courtyard':
        courtyardMapP2 =(
        "-|     |-"
        )
    elif roomin == 'prison':
        prisonMapP2 =(
        "|     |-"
        )
    elif roomin == 'hallway':
        hallMapP2 =(
        "-|     |"
        )
    elif roomin == 'altar':
        altarMapP2 =(
        "-|     |-"
        )
    elif roomin == 'staircase':
        rstairMapP2 =(
        "-|     |"
        )
    elif roomin == 'bedroom':
        bedMapP2 =(
        "|     |-"
        )

# This is the script used for picking up items.
def pickup(roomItem):
    global heldItem
    global satchelItems
    global satchelobtain
    clear()

    pickup = input("""What item do you wish to pick up?
""").lower() # This asks the player what they want to pick up.
    if pickup in roomItem and pickup == 'satchel':
        roomItem.remove(pickup)
        satchelobtain = 'true'
        clear()
        print("""You have found the satchel. It can hold up to 3 items at a time.
You now also have access to actions that require the satchel. Check inventory will also display items in your satchel.
Hint : You have to use the satchel to progress.""")
        # This checks if the player picked up the satchel since it's entirely seperate from the heldItem, etc.

    elif pickup in roomItem and '' in heldItem:
    # This checks for if the item is in the room and if the player isn't currently holding anything.

        heldItem.append(pickup)
        roomItem.remove(pickup)
        clear()
        if len(roomItem) <= 0:
            roomItem.append('')
        clear()
        print('You hold onto the {}'.format(pickup))
        heldItem.remove('')
        tm.sleep(rspd)
        # The player picks up the item. Self explanatory.

    elif pickup in roomItem and '' not in heldItem:
        # If the player is holding something this code is executed instead.

        if satchelobtain == 'true' and len(satchelItems) < 3:
        # This essentially checks if the player has the satchel and if they have less than 3 items in it.
            picksatch = 'h'
            while picksatch == 'h':
                clear()
                picksatch = input("""You can't hold onto another item however, you do have space in your satchel.
Do you wish to store the item in your satchel?
""") # This asks for if the player wants to put the item in the satchel.
                if picksatch == 'yes' or 'y':
                    satchelItems.append(pickup)
                    roomItem.remove(pickup)
                    if '' in satchelItems:
                        satchelItems.remove('')
                    clear()
                    if len(roomItem) <= 0:
                        roomItem.append('')
                    print('You put the {} in your satchel.'.format(pickup))
                elif picksatch == 'no' or 'n':
                    clear()
                    print('You decide against putting the item in your satchel.')
        elif satchelobtain == 'true' and len(satchelItems) >= 3:
        # This code is executed if the player has the satchel but doesn't have enough space.
            clear()
            print("You can't pick up the item as you're already carrying one and your satchel is full.")
        else:
        # This code is executed if neither of the top are true - in layman's terms, if the player has no satchel
            clear()
            print("You are unable to pick up the item as you're already carrying one.")
    else:
        clear()
        print("This item isn't in this room, or it doesn't exist.")
    # This runs if nothing else is true lmao.

# This is used to move between rooms.
# If the player can't go in a direction, it will ask them to re-input the movement.
# It checks for if a player is able to go to the room, by checking what room they're in, and what direction they typed in.
# This will either allow them to enter a room or will tell them they can't go that way.
def moverooms():
    global mapRightPassage1
    global bedlocked
    direction = 'null'
# This sets the direction to null so the while loop below works properly.
    while direction != 'west' and direction != 'east' and direction != 'north' and direction != 'south':
        direction = input("""What way do you want to go? (use cardinal directions)
""").lower()
# This checks for if direction is equal one of the four cardinal directions. If it isn't, the player is forced to pick one, since it's a while loop.
# The input below the while loop asks the player what way they want to go

    if (direction == 'west' and roomin == 'staircase'
    or direction == 'north' and roomin == 'courtyard'):

        global altarMapP1
        altarMapP1 =(
        " |-----| "
        )
        altar()

    if direction == 'east' and roomin == 'bedroom':
        clear()
        if bedlocked == 'true':
            useKey = 'bruhmoment'
            if 'bedroom key' in heldItem:
                useKey = input("""You're going to leave the room, however,
are you sure you don't want to permanently unlock the door?
Might be handy.
""").lower()
                clear()
                if useKey == "yes" or useKey == "y":
                    bedlocked = 'false'
                    print("The door is now permanently unlocked.")
                elif useKey == "no" or useKey == "n":
                    print("The door remains locked.")

                print("You use the key, and leave the bedroom.")
                tm.sleep(rspd)
                altar()
            else:
                print("The room is locked, and you aren't currently holding a key.")
            if satchelobtain == 'true':
                print("Check if the key is in your satchel.")
                tm.sleep(rspd)
        else:
            altar()


    elif direction == 'west' and roomin == 'altar':

        global bedMapP1
        clear()
        if bedlocked == 'true':
            useKey = 'bruhmoment'
            if 'bedroom key' in heldItem:
                useKey = input("""You're going to enter the room, however,
would you like to use the key to permanently unlock the door?
note that this isn't reversible.
""").lower()
                clear()
                if useKey == "yes" or useKey == "y":
                    bedlocked = 'false'
                    print("The door is now permanently unlocked.")
                elif useKey == "no" or useKey == "n":
                    print("The door remains locked.")

                print("You use the key, and finally enter the bedroom..")
                tm.sleep(rspd)
                bedMapP1 =(
                "|-----| "
                )
                bedroom()
            else:
                print("The room is locked, and you aren't currently holding a key.")
            if satchelobtain == 'true':
                print("Check if the key is in your satchel.")
                tm.sleep(rspd)
            altar()

        elif bedlocked == 'false':
            print("You enter the bedroom.")
            bedroom()

    elif direction == 'north' and roomin == 'hallway' or direction == 'east' and roomin == 'altar':

        global rstairMapP1
        rstairMapP1 =(
        " |-----|"
        )
        mapRightPassage1 =(
        "    |  "
        )
        staircase()

    elif (direction == 'south' and roomin == 'altar' or direction == 'west' and roomin == 'hallway'
    or direction == 'east' and roomin == 'prison' or direction == 'north' and roomin == 'inner'):

        global courtyardMapP1
        global mapMidPassage2
        global mapMidPassage1
        courtyardMapP1 =(
        " |-----| "
        )
        mapMidPassage2 =(
        "    |    "
        )
        mapMidPassage1 =(
        "    |    "
        )
        courtyard()

    elif (direction == 'east' and roomin == 'courtyard' or direction == 'south' and roomin == 'staircase'
    or direction == 'north' and roomin == 'tower2'):

        global hallMapP1
        global mapRightPassage2
        hallMapP1 =(
        " |-----|"
        )
        mapMidPassage2 =(
        "    |    "
        )
        mapRightPassage2 =(
        "    |    "
        )
        mapRightPassage1 =(
        "    |   "
        )
        hallway()

    elif direction == 'south' and roomin == 'hallway':

        global tower2MapP1
        tower2MapP1 =(
        " |-----|"
        )
        tower2()

    elif direction == 'north' and roomin == 'entrance' or direction == 'south' and roomin == 'courtyard':

        global innerMapP1
        global mapLeftPassage3
        global mapMidPassage3
        innerMapP1 =(
        " |-----| "
        )
        mapLeftPassage3 =(
        "         "
        )
        mapMidPassage3 =(
        "   |  "
        )
        inner()

    elif direction == 'north' and roomin == 'tower1' or direction == 'west' and roomin == 'courtyard':

        prison()

    elif direction == 'south' and roomin == 'prison':
        if towerOpen == 'true':
            global tower1MapP1
            tower1MapP1 =(
            "|-----| "
            )
            tower1()
        elif towerOpen == 'false':
            clear()
            print("""The door is locked.
It seems as if it's tied to some sort of mechanism.""")
            tm.sleep(rspd)
            prison()

    elif direction == 'south' and roomin == 'inner':

        global entranceMapP1
        entranceMapP1 =(
        "|-----|"
        )
        entrance()

    else:
        print("You're unable to go that way. Try again.")
        tm.sleep(rspd)
        clear()
        moverooms()
    return direction

# Function used for dropping items
def drop(roomItem):
    drop = 'false'
    clear()
    while drop == 'false':
        drop = input("""Which item would you like to drop?
Note you can only drop items that you're holding.
""")
    if drop in heldItem and '' not in heldItem:
# This checks if the player actually has the item they're trying to drop, and if they aren't holding anything.
        clear()
        roomItem.append(drop)
        heldItem.remove(drop)
        heldItem.append('')
        if '' in roomItem:
            roomItem.remove('')
        print("You dropped the {}".format(drop))

    else:
        print("You don't currently have that item, or aren't actually holding anything.")

# This is responsible for the player searching the room.
# I have a seperate function calling back to this one, to save space.
def searchRoom(roomItems, roomNotes):
    if len(roomItems) >= 1 and '' not in roomItems:
        print('Looking around you find the following : {}'.format(roomItems[0:]))
    elif '' in roomItems:
        print("After looking around for a bit, you don't find anything.")
    if len(roomNotes) == 1 and '' not in roomNotes:
        print("You also see a note, lying on the floor, titled '{}'".format(roomNotes[0]))

def readNote(roomNote):
    global Journal
    if '' not in roomNote:
        if '' in Journal:
            Journal.remove('')
        Journal.append(roomNote[0])
        clear()
        print('You find a note titled {}'.format(roomNote[0:]))
        tm.sleep(rspd)
        clear()
    elif '' in roomNote:
        print("There's no notes in the room.")
        tm.sleep(rspd)
        clear()

# This function calls back to the pick up function, checking what room the player is in,
# And actiong accordingly.
def pickingUp():
    if roomin == 'prison':
        pickup(prisonItems)
    elif roomin == 'bedroom':
        pickup(bedItems)
    elif roomin == 'inner':
        pickup(innerItems)
    elif roomin == 'tower1':
        pickup(tower1Items)
    elif roomin == 'tower2':
        pickup(tower2Items)
    elif roomin == 'entrance':
        pickup(entranceItems)
    elif roomin == 'courtyard':
        pickup(courtItems)
    elif roomin == 'altar':
        pickup(altarItems)
    elif roomin == 'hallway':
        pickup(hallItems)
    elif roomin == 'staircase':
        pickup(rstairItems)
    else:
        print('You are currently unable to perform this action.')

# And this function calls back to the drop function,
# It's the same thing like pickingUp is to pickup
def dropping():
    if roomin == 'prison':
        drop(prisonItems)
    elif roomin == 'bedroom':
        drop(bedItems)
    elif roomin == 'inner':
        drop(innerItems)
    elif roomin == 'tower1':
        drop(tower1Items)
    elif roomin == 'tower2':
        drop(tower2Items)
    elif roomin == 'entrance':
        drop(entranceItems)
    elif roomin == 'courtyard':
        drop(courtItems)
    elif roomin == 'altar':
        drop(altarItems)
    elif roomin == 'hallway':
        drop(hallItems)
    elif roomin == 'staircase':
        drop(rstairItems)
    else:
        print('You are currently unable to perform this action.')

# And.. this calls back to the reading function.
# But, this time it prints the note if it's in the room. neat.
# Although it's a lot of text, it's all just notes. literally.
def readingNotes():
    if roomin == 'prison':
        readNote(prisonNotes)
        if "memory loss" in prisonNotes:
            print("""If you're reading this, you probably have absolutely no idea what's going on. And that's fine.
All you need to know is that you have to escape this place. You'll know what to do as you go.
Sincerely, Someone you know.""")
            tm.sleep(rspd)
            clear()
            prisonNotes.pop(0)
            prisonNotes.append('')
    elif roomin == 'bedroom':
        readNote(bedNotes)
        if "my last goodbye" in bedNotes:
            print("""This is the end of the line for me. Finally, as I take what I assume will be my last few breaths, I realise what this was all about.
It's all the same. All a cycle. I'll drink this, again. And wake up in that cell, in what I hope will be my last attempt.
Everything is in place now. All is where it's supposed to be. Hopefully, I'll be able to escape. If you're reading this :
I hope you don't screw up.
Sincerely, You.""")
            tm.sleep(rspd)
            clear()
            bedNotes.pop(0)
            bedNotes.append('')
    elif roomin == 'inner':
        readNote(innerNotes)
    elif roomin == 'tower1':
        readNote(tower1Notes)
    elif roomin == 'tower2':
        readNote(tower2Notes)
    elif roomin == 'entrance':
        readNote(entranceNotes)
        if 'not a way out' in entranceNotes:
            print("""I tried the entrance door to no avail. Not only does it seem to be locked, it also seems to be barricaded from the outside.
Wonder who would do this and why? This castle doesn't seem that bad -
There's enough things on the second floor for someone to live here for a few years. But, that doesn't change the fact that I want to escape.
What bothers me more is that I still don't know how I got here...""")
            tm.sleep(rspd)
            clear()
            entranceNotes.pop(0)
            entranceNotes.append('')
    elif roomin == 'courtyard':
        readNote(courtNotes)
        if 'strange mechanism' in courtNotes:
            print("""The mouth seems to be tied to some type of mechanism. I think it's supposed to store some sort of.. orb?
I can't fully work out what it would do, however it does peak my curiosity.""")
            tm.sleep(rspd)
            clear()
            courtNotes.pop(0)
            courtNotes.append('')
    elif roomin == 'altar':
        readNote(altarNotes)
        if 'ritual instructions' in altarNotes:
            print("""To initiate the final sequence, for this nightmare to end:
in no particular order, poor blood into the designated slots.
and place the stone tablet inside the rectangular slot, and input in these numbers :
{}. Then, it shall all come to an end.""".format(vaultnote))
            tm.sleep(rspd)
            clear()
            altarNotes.pop(0)
            altarNotes.append('')
    elif roomin == 'hallway':
        readNote(hallNotes)
    elif roomin == 'staircase':
        readNote(rstairNotes)
        if 'a way up no more' in rstairNotes:
            print("""I've broken the staircase. I realise that for my next attempts to work properly,
I shouldn't have access to those rooms. I've noticed that I spend way too much time on them.
Though, I've encountered an oversight. I only have one more vial left - Leaving me with just one last attempt.
No matter, as I'm almost certain that with my next attempt I will emerge victorious.""")
            tm.sleep(rspd)
            clear()
            rstairNotes.pop(0)
            rstairNotes.append('')
    else:
        print('You are currently unable to perform this action.')

# Same as above but for searching the rooms, except this time with two variables.
def searchingRoom():
    if roomin == 'prison':
        searchRoom(prisonItems, prisonNotes)
    elif roomin == 'bedroom':
        searchRoom(bedItems, bedNotes)
    elif roomin == 'tower1':
        searchRoom(tower1Items, tower1Notes)
    elif roomin == 'tower2':
        searchRoom(tower2Items, tower2Notes)
    elif roomin == 'altar':
        searchRoom(altarItems, altarNotes)
    elif roomin == 'entrance':
        searchRoom(entranceItems, entranceNotes)
    elif roomin == 'hallway':
        searchRoom(hallItems, hallNotes)
    elif roomin == 'courtyard':
        searchRoom(courtItems, courtNotes)
    elif roomin == 'staircase':
        searchRoom(rstairItems, rstairNotes)
    elif roomin == 'inner':
        searchRoom(innerItems, innerNotes)
    else:
        print('You are currently unable to perform this action.')

# This is responsible for the ending sequence.
# There is 4 endings in total - One for completing normal mode,
# Two for getting a certain amount of moves in challenge mode,
# And one for collecting 3 or more notes in challenge mode while still having enough moves left to finish the game.
def endGame():
    global challenge
    global challengeTimer
    clear()
    if challenge == 'false':
        print("""The castle starts shaking. You black out, and wake up.
You wake up in a prison cell. You're facing a locked cell door...""")
        tm.sleep(rspd)
        print("""You've finished the game. Congratulations. The challenge mode code is 1987.
just type it in when the game asks if you want to read through the help menu. Who knows, the ending might be different.
""")
        tm.sleep(rspd + 1)
        # runs if the player has more than 4 moves remaining, and has less than 3 notes in their journal.
    elif challenge == 'true' and challengeTimer > 4 and len(Journal) < 3:
        print("""The castle starts crumbling around you. It feels as if the fabric of reality is trying to pull itself apart.
A white flash blinds you, as you find yourself outside the castle. You watch it become nothing more than rubble.
It's finally over. You made it.
""")
        tm.sleep(rspd)
        # runs if the player have less than or equal to 4 moves remainging, and has less than 3 notes in their journal.
    elif challenge == 'true' and challengeTimer <= 4 and len(Journal) < 3:
        print("""The castle starts crumbling around you. It feels as if the fabric of reality is trying to pull itself apart.
A white flash blinds you, and you go with it, as you feel like your tired body is being torn into a thousand pieces.
You took too long. Try getting through in 35 moves or less. Or, try and learn more about the castle.
""")
        tm.sleep(rspd)
        # no matter how many moves they have remaining, this runs if they have 3 or more notes.
    elif challenge == 'true' and len(Journal) >= 3:
        print("""A flash of white light blinds you as you get teleported out of the castle. With all of your findings, and the castle intact,
you inform the local historians and researchers about the place. Upon investigation of the castle, they find a great fortune.
It's later found that the castle, and the fortune by default, belong to you. You've conquered the castle, and found it's secrets.
It's yours now. Congratulations!

Note from the dev :
If you're reading this, you got the best ending. Which, all in all, isn't that difficult to get but it's something.
Hopefully you enjoyed the game.
""")
    print("Thanks For Playing.")
    input("""Press enter to continue
""")
    tm.sleep(rspd)
    sys.exit()

# This is supposed to allow you to store items in the satchel.
def storeItem():
    satchStore = 'false'
    clear()
    if satchelobtain == 'true' and '' not in heldItem and len(satchelItems) < 3:
        satchStore = input("""Do you want to store your currently held item ({}) in the satchel?
""".format(heldItem[0])).lower() # this asks the player if they want to store their item in the satchel.
        bruh = 'moment' # i was bored with true and false variables. Treat this as 'true'. It's there so the while loop exists.
        while bruh == 'moment':

            # if the player does want to store the item, this runs.
            if satchStore == 'yes' or satchStore == 'y':
                satchelItems.append(heldItem[0])
                heldItem.pop(0)
                heldItem.append('')
                clear()
                print("You put the item away in the satchel.")
                if '' in satchelItems:
                    satchelItems.remove('')
                bruh = 'unmoment'
                tm.sleep(rspd)
                clear()

            # If the player changes their mind, this runs.
            elif satchStore == 'no' or 'n':
                clear()
                print("You decide not to store the item in the satchel.")
                tm.sleep(rspd)
                bruh = 'unmoment'
                clear()

            # This tells the player that a yes or no answer can't be answered with gdkjhdsfkjdhjk
            else:
                clear()
                print('Incorrect Input, try again.')
                tm.sleep(rspd)

    # This occurs if you're holding something but you don't have a satchel.
    elif satchelobtain == 'false' and '' not in heldItem:
        print("You currently can't store the item anywhere.")
        tm.sleep(rspd)
        clear()

    # This occurs if you have a satchel but it's full.
    elif satchelobtain == 'true' and len(satchelItems) >= 3 and '' not in heldItem:
        print("Your satchel is currently full.")
        tm.sleep(rspd)
        clear()

    # This occurs if you're not holding anything.
    else:
        print("You aren't currently holding anything.")
        tm.sleep(rspd)
        clear()

# This is the journal feature.
# It allows the player to view notes they found throughout their playthrough.
# Only one of these is required to progress, and that's ritual instructions.
def JournalF():
    clear()
    global vaultnote
    if len(Journal) >= 1 and '' not in Journal:
        print("""These are the notes you've found so far :
{}""".format(Journal[0:]))
        noteTakingmp3 = input("""Which note do you want to read?
""").lower()
        clear()

        # found in the prison
        if noteTakingmp3 == 'memory loss' and noteTakingmp3 in Journal:
            print("""If you're reading this, you probably have absolutely no idea what's going on. And that's fine.
All you need to know is that you have to escape this place. You'll know what to do as you go.
Sincerely, Someone you know.""")
            tm.sleep(rspd)
            clear()

        # found in entrance hall
        elif noteTakingmp3 == 'not a way out' and noteTakingmp3 in Journal:
            print("""I tried the entrance door to no avail. Not only does it seem to be locked, it also seems to be barricaded from the outside.
Wonder who would do this and why? This castle doesn't seem that bad -
There's enough things on the second floor for someone to live here for a few years. But, that doesn't change the fact that I want to escape.
What bothers me more is that I still don't know how I got here...""")
            tm.sleep(rspd)
            clear()

        # found in the courtyard.
        elif noteTakingmp3 == 'strange mechanism' and noteTakingmp3 in Journal:
            print("""The mouth seems to be tied to some type of mechanism. I think it's supposed to store some sort of.. orb?
I can't fully work out what it would do, however it does peak my curiosity.""")
            tm.sleep(rspd)
            clear()

        # found in the ruined stairway.
        elif noteTakingmp3 == 'a way up no more' and noteTakingmp3 in Journal:
            print("""I've broken the staircase. I realise that for my next attempts to work properly,
I shouldn't have access to those rooms. I've noticed that I spend way too much time on them.
Though, I've encountered an oversight. I only have one more vial left - Leaving me with just one last attempt.
No matter, as I'm almost certain that with my next attempt I will emerge victorious.""")
            tm.sleep(rspd)
            clear()

        # found in the altar room. Has the code for the strange tablet.
        elif noteTakingmp3 == 'ritual instructions' and noteTakingmp3 in Journal:
            print("""To initiate the final sequence, for this nightmare to end:
in no particular order, poor blood into the designated slots.
and place the stone tablet inside the rectangular slot, and input in these numbers :
{}. Then, it shall all come to an end.""".format(vaultnote))
            tm.sleep(rspd)
            clear()

        # found in the bedroom.
        elif noteTakingmp3 == 'my last goodbye' and noteTakingmp3 in Journal:
            print("""This is the end of the line for me. Finally, as I take what I assume will be my last few breaths, I realise what this was all about.
It's all the same. All a cycle. I'll drink this, again. And wake up in that cell, in what I hope will be my last attempt.
Everything is in place now. All is where it's supposed to be. Hopefully, I'll be able to escape. If you're reading this :
I hope you don't screw up.
Sincerely, You.""")
            tm.sleep(rspd)
            clear()

        # this comes up if the player puts in something that's not in their journal.
        else:
            print("You don't currently have that note, or it doesn't exist.")
            tm.sleep(rspd)
            clear()
    # this comes up if '' is in the journal meaning it's empty.
    else:
        print("You haven't found any notes yet.")
        tm.sleep(rspd)
        clear()

# These are just the room descriptions. They don't have items in it, or anything. Mostly for immersion.
# Some descriptions are important though, like the courtyard or prison descriptions.
# For those the reading speed is increased by 1 second.
def lookAround():
    global roomin
    # for the prison.
    if roomin == 'prison':
        print("""The prison consists of a few cells, most of them empty. The celling of the area stretches across at least 4 floors,
however, there seems to be no staircase leading to the upper cells. There's two exits leading south and east.

There's also a bookeshelf, missing a book. It's extremely out of place.""")
        tm.sleep(rspd + 1)
        clear()

    # for the western tower.
    elif roomin == 'tower1':
        print("""The western tower looks mostly like the eastern tower, with the exception of a single, albeit barred window showing the outside.
You sigh as you gaze upon a grass field. You breathe in the fresh air, escaping through the window.
Like the other tower there's only one exit - north, leading into the prison.""")
        tm.sleep(rspd)
        clear()

    # for the southern tower
    elif roomin == 'tower2':
        print("""The tower looks like a standard tower. Made mostly of stone, there's nothing really noticable about it.
It doesn't really stand out, but, neither do most things in this place. There's only one exit - north, to the hallway.""")
        tm.sleep(rspd)
        clear()

    # for the courtyard.
    elif roomin == 'courtyard':
        print("""As you look around you take in the courtyard. It's definitely the most peaceful place around, with flowers blooming,
a fountain constantly dispensing water, and four exits, splitting to the north, south east and west.

Looking around, however, you can't help but notice something about the fountain.
The fountain has a statue of a creature, with it's mouth, empty, open in a circle - It feels like something is missing.""")
        tm.sleep(rspd + 1)
        clear()

    # for the altar.
    elif roomin == 'altar':
        print("""As soon as you enter the altar room you feel a menacing aura around the focal point of the room - the altar.
There's a rectangular slot in the altar, as well as a red-tinted funnel, obviously meant for a liquid.
There are door leading east, west and south.""")
        tm.sleep(rspd + 1)
        clear()

    # for the staircase.
    elif roomin == 'staircase':
        print("""This stairway looks like it collapsed long ago. Now it's nothing but rubble. Only a miracle could fix this.
There are doors leading to the west and south.""")
        tm.sleep(rspd)
        clear()

    # for the inner hall
    elif roomin == 'inner':
        print("""The inner hall is a huge, white hall made of marble. However, run-down, like the rest of the castle.
There's a hole in the celling, with rubble below it. The hole allows for sunlight, which doesn't do much,
but make you long for the outside. You can go north and south from here.""")
        tm.sleep(rspd)
        clear()

    # for the entrance.
    elif roomin == 'entrance':
        print("""The entrance hall isn't much different from the inner hall, with the exception of a giant door.
you try to open it, unsuccessfully however, as the door is locked. Seems like you can only go north from here.""")
        tm.sleep(rspd)
        clear()

    # for the hallway.
    elif roomin == 'hallway':
        print("""There's nothing really special about the hallway; it's run down, like most of the castle, with walls made of stone bricks,
and not much else. There's doors leading to the north, south and west.""")
        tm.sleep(rspd)
        clear()

    # for the bedroom
    elif roomin == 'bedroom':
        print("""The bedroom is in the most pristine condition anything in the castle is. There's a nice, red carpet covering the floor,
and a 2-person bed, nicely made, pointing to the fact that someone must've been here not that long ago.
Despite how clean the room is, there's not much else of note. You can only go east from here.""")
        tm.sleep(rspd)
        clear()

    # I don't know how it's even possible to get this message, but it's there just in case.
    else:
        print("""How did you even get this error?""")
        tm.sleep(rspd)
        clear()

# This is for taking items from the satchel.
def takeItem():
    clear()
    satchWant = 'false'

    if satchelobtain == 'true' and '' in heldItem:
        wantItem = input("""What item do you want to take from the satchel?
""").lower() # This asks the player what item they want to take.
        if wantItem in satchelItems:
            while satchWant == 'false':
                clear()
                satchWant = input("""Do you want to take this item ({}) from the satchel?
""".format(wantItem)).lower() # This asks for confirmation for if they want to take the item.
                if satchWant == 'yes' or satchWant == 'y':
                    heldItem.append(wantItem) # This adds the item to the held item.
                    heldItem.remove('') # This removes nothing from the held item.
                    satchelItems.remove(wantItem) # This removes that item from the satchel items.
                    if len(satchelItems) < 1:
                        satchelItems.append('')
                elif satchWant == 'no' or satchWant == 'n':
                    clear()
                    print("You don't take the item from your satchel.")
                    # this cancels the action if the player says no.
                    tm.sleep(rspd)
                    clear()

        elif wantItem not in satchelItems:
            clear()
            print("That item isn't currently in your posession.") # this comes up  if the item isn't in the satchel.
            tm.sleep(rspd)
            clear()

    # These are all things that come up if something wouldn't allow the player to use the action and should be self explanatory.
    elif satchelobtain == 'true' and '' not in heldItem:
        clear()
        print("You're currently holding an item. Get rid of the item, and then try again.")
        tm.sleep(rspd)
        clear()

    # This runs if the player doesn't have a satchel yet.
    elif satchelobtain == 'false':
        clear()
        print("You currently can't take an item from your satchel as you don't yet have a satchel.")
        tm.sleep(rspd)
        clear()

    # This runs if nothing else is true.
    else:
        clear()
        print("You are currently unable to use this command.")
        tm.sleep(rspd)
        clear()

# This is for switching items. I didn't want to code this in. It's easy, and I prefer having 2 functions seperate to this one for inventory management.
# However, I know that if I didn't put this in, someone would nitpick my code.
# I will also explain this in 1000% detail, just for you, Bayakly.
def swapItems():
    global heldItem # This sets heldItem to global so we can use it.
    global satchelItems # This sets satchelItems to global so we can use it.
    global satchelobtain # This sets satchelobtain to global so we can use it.
    clear() # This uses the clear function.
    if '' not in heldItem and '' not in satchelItems and satchelobtain == 'true':
       # This checks for if the player is holding something and if they have something in their satchel.
        SwitchH = 'IHopeYoureReadingThis'
       # This sets a variable so that the while loop runs.
        while SwitchH == 'IHopeYoureReadingThis':
            # This is the aforemenetioned while loop which runs because the previous variable is set to what it is.
            Switch = input("""Do you want to swap your currently held item [{}] with one of the items from your satchel {}?
""".format(heldItem[0], satchelItems[0:])).lower() # This asks the player if they want to perform the action, listing their items while at it.
            if Switch == 'yes' or 'y': # This checks for if the player wants to switch.
                clear() # This clears the screen.
                SwitchH = 'YesThisIsFalseNow' # This sets a variable so the while loop is now false.
                whichItem = input("""Which item would you like to swap from your satchel?
""").lower() # This asks the player which item they want to swap.
                if whichItem in satchelItems: # This checks for if the item is in the satchel.
                    clear() # If it is, it clears the screen first.
                    satchelItems.append(heldItem[0]) # Then it adds the player's heldItem to their satchelItems.
                    satchelItems.remove(whichItem) # This removes that item from existance it's pretty cool
                    heldItem.pop(0) # Then it removes the player's heldItem from existance.
                    heldItem.append(whichItem) # Then it adds the item they wanted to swap for.
                    print("You switched the two items with each other.") # This says that they switched the two items with one another.
                    tm.sleep(rspd) # This makes the game wait an amount of time set by the player beforehend.
                    clear() # This clears the screen.

                elif whichItem not in satchelItems: # This runs if the item mentioned is not in satchelItems.
                    clear() # This clears the screen.
                    print("That item is not in your satchel.") # This tells the player that they're wrong.
                    tm.sleep(rspd) # This waits a bit.
                    clear() # Bet you can't guess what this does.

                else: # This runs if somehow neither of the above are true??
                    print("Try again.") # seriously how would you do that.

            elif Switch == 'no' or 'y': # This runs if no.
                clear() # SCREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEN CLEEEEEEEEEEEAAAAAAAAAAAAR
                SwitchH = 'YesThisIsFalseNow' # yup the while loop is now untrue.
                print("You decide against swapping the items.") # The player has indeed decided against that as they said no.
                tm.sleep(rspd) # wait a bit
                clear() # and clean the screen.

    elif satchelobtain == 'false': # this runs if the satchel has not been obtained.
        print("You don't even have a satchel yet.") # indeed they dont.
        tm.sleep(rspd) # wait...
        clear() # ...clear.

    elif '' in heldItem: # this runs if the player is holding nothing.
        print("You're not currently holding anything.") # they aren't that is true.
        tm.sleep(rspd) # stop.
        clear() # wait a minute.

    elif '' in satchelItems: # this runs if the player has nothing in their satchel.
        print("You currently have no items in your satchel.") # you tell em print statement.
        tm.sleep(rspd) # wait
        clear() # contemplate life.

# It's the help command. it shows you a list of commands you can use. That's it.
def help():
    clear()
    print("""Here is a list of commands you can use:
move - Allows you to move between rooms.
pick up - Prompts you to pick up an item.
drop - Prompts you to drop an item.
check (map, inventory, journal) - Allows you to look through those menus.
use (followed by item you'd like to use) - Allows you to use the item if the item is usable.
search - Allows you to search the room, displaying items visible in the room.
help - Displays this menu.
set speed - Allows you to set the reading speed.
take from satchel - Allows you to take an item from the satchel, if you have one.
store - allows you to store an item in the satchel, if you have one.
look around – gives you a detailed description of a room
read – adds the note in the room to your journal, as well as displaying it.
swap - allows you to swap a satchel item with your held item.
check moves – allows you to check how many moves you have. (Only in challenge mode) (Only action that doesn’t decrease moves.)
""")
    input('Press enter to continue.').lower()
# This is one of the only things in this game that has this as a popup.
# This is because i feel the help menu is something the player should read carefully, and will probably take up more space than anything else.
# This is also in case the player can't read fast, and set the reading speed to a low value, so they know how to change it without the menu just. dissapearing.
# Accessibility, essentially.

clear()

# Start of the game.

welcomeValid = 'false'
while welcomeValid == 'false':
    print("""Welcome to the game!
Your goal is to escape the castle, the rest will be revealed as you go.
Do you want to have a read through the help menu first?
Note that you can access this menu in the game by using the 'help' command.""")
    firstHelp = input('').lower()
    if firstHelp == 'y' or firstHelp == 'yes':
        welcomeValid = 'true'
        help()
# This runs the help function if the player needs to know the commands.

    elif firstHelp == "1987":
        clear()
        print("""Challenge Mode activated.
You have a limited amount of moves.
Oh, the satchel is also gone. Really think about what your next move is going to be.
Have fun :  )""")
        challengeTimer = 41
        tm.sleep(8)
        challenge = 'true'
        tower1Items.remove('satchel')
        tower1Items.append("bedroom key")
        welcomeValid = 'true'
# In case the player decided to input in the code at the end of the game, it activates this.
# A challenge mode.

    elif firstHelp == 'n' or firstHelp == 'no':
        welcomeValid = 'true'
        print("All right. Let's start, then.")

    else:
        clear()
        print("Improper answer. Try again.")
        tm.sleep(2)
        clear()

clear()
readingSpeedSet()
clear()

# This is the actual beginning.
print("""You wake up in a prison cell. You're facing a locked cell door, with a steel bar, the shape of a crowbar, next to you.
You don't know how you got here, but you know you have to get out. You stand up.""")
tm.sleep(rspd)
prison()








