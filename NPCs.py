from items import *
from methods import *
from classes import *


roger = NPC('alien')
roger.verbs['drill'] = drill
roger.inventory['crystal'] = crystal2

michael = NPC('alien')
michael.verbs['drill'] = drill
michael.inventory['crystal'] = crystal2

#dead rover in forest east

rover1 = NPC('ROVER')
rover1.isalive = False
rover1.verbs['loot'] = loot
rover1.inventory['crystal'] = crystal2
rover1.inventory['flashlight'] = flashlight


