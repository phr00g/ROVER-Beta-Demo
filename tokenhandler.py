from classes import *
from locations import *
from items import *
import random
import pygame
import time
import threading
from pgmap import *








#one token command handler

def onetoken(command): #command = verb
    verb = str(command[0])
    if verb in singleverbs:
        verbs[verb]()
    else:
        print("I'm gonna need more than that :( ")
        pass

#two token command handler
def twotoken(command):#command = verb , item

        

    #verb = string of first command token
    verb = command[0]
   #currentItem = string of second command token
    currentItem = command[1]
    
    

    #if item is in locaiton inventory
    if currentItem in me.location.inventory:

        itemobject = me.location.inventory[currentItem]
    
    #pass item object to verb method if verb method in item's verbs dictionary
        if verb in itemobject.verbs:
            itemobject.verbs[verb](itemobject) #aka verb(item)
        
        #valid item but invalid verb for item
        else:
            print('Cannot {} {}'.format(verb,currentItem))
    
    #if item is in player inventory
    elif currentItem in me.inventory:
        itemobject = me.inventory[currentItem]

    #pass item object to verb method if verb method in item's verbs dictionary
        if verb in itemobject.verbs:
            itemobject.verbs[verb](itemobject) #aka verb(item)
        
        #valid item but invalid verb for item
        else:
            print('Cannot {} {}'.format(verb,currentItem))


    
    else:



        print("There is no {} here! ".format(currentItem))
        
 
    
    
#do not include for Midterm GDD / alpha build


def fourtoken(command):
    pass



#token number identifier / handler
def tokenhandler(command):
    length = len(command)
    
    if length == 1:
        onetoken(command)
    elif length ==2:
        
        #add walking / go condition
        twotoken(command)
    elif length ==3:
        print("I dont understand")
    elif length == 4:
        fourtoken(command)