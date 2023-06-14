from classes import *
from methods import drill, open_image
from items import *
import pygame
import os
from lang import encode,decode
from NPCs import *
import webbrowser


#just to appease false positive problem form ide
from NPCs import roger,michael







#instantiate ALL locations, connecting them and adding attributes will occur latera34
#test = location()





width = 8
height = 9

# Create a 2D array of Location objects
#must be global becasue it is used in pygame thread
global map_array
map_array = [[location(x, y) for y in range(height)] for x in range(width)]

# Assign the up, down, left, and right attributes for each Location object
for x in range(width):
    for y in range(height):
        #dumb word to prevent key error
        temp_location = map_array[x][y]
        if y > 0:
            temp_location.north = map_array[x][y - 1]
        if y < height - 1:
            temp_location.south = map_array[x][y + 1]
        if x > 0:
            temp_location.west = map_array[x - 1][y]
        if x < width - 1:
            temp_location.east = map_array[x + 1][y]

    
#create all PERMANENT disconnections, remember iteration later so dont be redundant!
#[col][row]

#starting west wall
map_array[3][2].west = None
map_array[3][3].west = None
map_array[3][4].west = None
map_array[3][5].west = None
map_array[3][6].west = None

#south east abyss
map_array[6][5].north = None
map_array[6][5].west = None
map_array[6][5].east = None
map_array[6][5].south = None
map_array[6][6].north = None
map_array[6][6].west = None
map_array[6][6].east = None
map_array[6][6].south = None

#east shrine room north and south
map_array[7][6].south = None
map_array[7][6].north = None

#south east cave abyss border
map_array[5][8].north = None
map_array[6][8].north = None
map_array[7][8].north = None
#and the bridge
map_array[5][8].west = None




#top left corner
map_array[7][0].west = None

#tar pit
map_array[5][1].west = None
map_array[5][1].north = None
map_array[6][1].east = None
map_array[6][1].north = None

map_array[5][2].west = None
map_array[5][2].south = None
map_array[6][2].east = None
map_array[6][2].south = None


#west volcano crest
map_array[1][5].north = None
map_array[1][5].west = None
map_array[1][5].east = None
map_array[1][5].south = None

#inverse volcano
map_array[1][3].north = None
map_array[1][3].west = None
map_array[1][3].east = None
map_array[1][3].south = None

#top right corner sleeping giant
map_array[7][1].north = None




#adding minerals to correct sites
map_array[7][0].hasmineral = True
map_array[7][0].istestable = True


map_array[4][8].hasmineral = True
map_array[4][8].istestable = True 


map_array[6][7].hasmineral = True
map_array[6][7].istestable = True


map_array[1][3].hasmineral = True
map_array[1][3].istestable = True





#iterates through all locations and if can be left, but not entered from same direciton, assigns that direction None
#it fixes the map and prevent a lot of work
for row in map_array:
    for loc in row:

        #if i can go up, but then not go back down, i will no longer be able to go up
        if loc.north != None and loc.north.south != loc:
            loc.north = None

        if loc.south != None and loc.south.north != loc:
            loc.south = None

        if loc.west != None and loc.west.east != loc:
            loc.west = None

        if loc.east != None and loc.east.west != loc:
            loc.east = None











#apply all greetings here attributes in next section

#landing###############################  
landing =map_array[3][4]
landing.greeting = '''ROVER: This is your landing dock. This is not a suitable testing site. The land is flat with a thin layer of orange dust. To the north there appears 
to be a more flat rockland and a low vibrating hum. To the east is a large hill with a gray metallic sheen.
To the south is the center of a massive crater. To the west is a large abyss which I can not travel across'''    #There appears to be an energy crystal on the floor'''

landing.desc = "your landing site"



#crater###########

crater = map_array[3][5]
crater.greeting = '''ROVER:You are at the center of a very large crater. This must be the result of some sort of interplanetary collision. To the south is an ascent to the southern
lip of the crater. To the east is an ascent to the eastern lip of the crater. The landing dock is to the north. To the west is a large abyss which I cannot travel across. '''
crater.istestable = True

#flatrock area w rumble
rumble = map_array[3][3]
rumble.greeting = '''ROVER: There is not much to see around here. There are a few large boulders, with a cement color laying around. I am picking up a low pitched rumble through
the thin atmosphere, its origin is beneath the ground. To the north is terrain that is more of the same, but there is a large slab that seems to be floating at least 100 meters in the sky
and there is nothing supporting it. Curious. To the east is the mouth of a large cave with stalagtites growing in the up and down direction. It looks like the mouth of a giant fish. 
The landing dock is south of here. '''

#fishcave###############
fishcave = map_array[4][3]
#there is a person here




fishcave.inventory['alien'] = roger

def fishcave_event():
    if 'alien' in fishcave.inventory and roger.isalive == True:
        message = 'again and again you come your puny devices infect use and pollute our ether when will you ever be satisfied'
        message = encode(message)

        yn = input('''ROVER: There appears to be an alien lifeform in this cave. I have taken a low resolution scan. Would you like me to print it on your device? y/n''')
        
        if yn == 'y':
            print("\nExporting scan ....")
            open_image('roger.png')

        print("ROVER: It appears that it is attempting to use some crude for of communication. I will observe and translate.")
        print("ROVER: Okay, here is a rough translation: {}".format(message))

    else:
        fishcave.eventflag = False

#whenever lcoation is visited for first itme, location.event is triggered
fishcave.eventflag = True

fishcave.event = fishcave_event

fishcave.greeting = ('''ROVER: There does not appear to be anything of value in this cave. To the west in the flat rock land, to the north through a small opening appears to be a flat 
clearing, and to the east is a larger cave mouth leading outside. The alien is brooding in the corner, but appears to maintain its focus upon us.''')

def fishcave_update():
    fishcave.greeting = '''ROVER: There does not appear to be anything of value in this cave. To the west in the flat rock land, to the north through a small opening appears to be a flat 
clearing, and to the east is a larger cave mouth leading outside. The remains on the alien lay here.'''

#involked in drill in methods.py
fishcave.update = fishcave_update

     
#floating rock town##########
floating = map_array[3][2]

floating.greeting = '''ROVER: We are just beneath the giant floating slab. From this angle it is impossible to see what 
is directly above us. I can sense a very faint low frequence hum coming from the southern direciton. To the east appears to be the mouth of a cave, and to the north there appears to be nothing of
note. This site is not suitable for excavation. '''

#31 clearing##################### 
map_array[3][1]. greeting = '''This is a standard clearing. The ground is flat with a thin layer of orange dust. 
To the south I can see a large slab floating very high in the sky. To the north appears to be some sort of swamp. To the east there seems 
to be some sort of monument or shrine, thin and tall. From here it is difficult to tell. This site is not suitable for excavation.'''


## OBELISK NUMBER 1
obelisk1 = map_array[4][1] 
obelisk1.eventflag = True

def obelisk1event():
    print("ROVER: There is a very large obelisk made from an array of local.....")
    print("Signal disrupted please wait....")
    opened = webbrowser.open('https://newemailssadfsdfsh.s3.us-west-2.amazonaws.com/index.html')
    print("....materials and sediments. It is crude and unsightly. ")
    #add rest of greeting here just cause
    print('''ROVER:To the south appers to be the mouth of some sort of cave, I do not see anything of note to the west, to the east is a
    steep descent to a very vast tar pit that we will not be able to reach. To the north is some sort of very high and large smoke spiral.
    I think your people call them 'vortexes'. ''')

obelisk1.event = obelisk1event

####crater lip south of landing############

craterlipsouth = map_array[3][6]
craterlipsouth.eventflag = True

craterlipsouth.greeting = '''ROVER:We are at the souther lip of a very large crater. We are surrounded by a very dark, glassy residue that does not seem 
familiar to this terrain. To the south is a flat with a topsoil layer composed of mostly salt. There does not seem to be anything of note to the east. To the north is the center of the crater
and to the east is an endless abyss which I can not travel across.'''

craterlipsouth.inventory['alien'] = michael

def craterlipsouthevent():
    
    if 'alien' in craterlipsouth.inventory and michael.isalive == True:
        message = 'you do not have to do what all of your associates have done, you can save us. If you can ever find a way to listen to us you will find we can work together. better yet destroy those signal towers and leave us alone'
        message = encode(message)

        yn = input('''ROVER: There appears to be an alien lifeform in the smoke. I have taken a low resolution scan. Would you like me to print it on your device? y/n''')
        
        if yn == 'y':
            print("\nExporting scan ....")
            #we change this when we make michael's photo
            open_image('roger.png')

        print("ROVER: It appears that it is attempting to use some crude for of communication. I will observe and translate.")
        print("ROVER: Okay, here is a rough translation: {}".format(message))

    else:
        craterlipsouth.eventflag = False


craterlipsouth.eventflag = True
craterlipsouth.event = craterlipsouthevent


#####salt flat center################
saltcenter = map_array[3][7]
saltcenter.istestable = True
saltcenter.hasmineral = True

saltcenter.greeting = '''ROVER: We are in the middle of a salt flat. The wind has formed some dunes, but otherwise there is not much of note. To the north is the southern
lip of the crater. To the west and to the east are more of the same salt flat. To the south there is a clearing with nothing noteworthy.'''

####salt flat east

salteast = map_array[4][7]
salteast.greeting = '''ROVER:This is simply another salt flat. Fewer dunes than the salt flat to the west. To the east is the beginning of a forest
composed of some sort of cellulose. To the south is the mouth of a cave that appears very dark.  '''


#### Cluulose FOrest Entrance with large tree holding alien

forestentrance = map_array[5][7]


forestentrance.inventory['tree'] = tree

forestentrance.greeting = '''ROVER:This is the mouth of a large forest of trees. They are made of cellulose but beyond that I am not sure. To the west is
    the salt flat. To the north there is nothing of interest. To the east is deeper, more dense forest.'''




def entranceupdate():
    print("ROVER: After drilling the very large tree it fell, and a star shaped trinket fell on the floor. It appeears to be some sort of relic.")
    forestentrance.inventory['star'] = star


forestentrance.update = entranceupdate
    














#add all items


#
landing.inventory['crystal'] = crystal1













