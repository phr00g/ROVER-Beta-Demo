from classes import *
from items import *
import pygame

#special case and order for starting location




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










#adding minerals to correct sites
map_array[7][0].hasmineral = True
map_array[7][0].istestable = True


map_array[4][8].hasmineral = True
map_array[4][8].istestable = True 


map_array[6][7].hasmineral = True
map_array[6][7].istestable = True


map_array[1][3].hasmineral = True
map_array[1][3].istestable = True


#add all items

map_array[3][4].inventory['crystal'] = crystal1










