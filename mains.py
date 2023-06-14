
from classes import *
from locations import *
from items import *
from tokenhandler import *
import random
import pygame
import time
import threading
from pgmap import *
from methods import *
from NPCs import *


       


# #game start

#intro sequence
idnumber = str(random.randint(1000,9999))
print('\n')
print("Greetings on behalf of Material Solutions Incorporated (MSI), Associate Remote ROVER Engineer #{}!  ".format(idnumber))
print("It seems that this is your first time uplinking to a ROVER! Fear!")
print('\n')
print("As you know, Associated Remote ROVER Engineer #{}, MSI's TS909 ROVER is a simple little soil testing and drilling rig. We wish you could see how cute it is!".format(idnumber))
print("MSI is looking for available and ethically reachable deposits of Neutronium , which is why your ROVER is currently located on the conveniently nearby terrestrial planet of REDACTED.")
print("Excitingly you are part of the first probe that we have sent to this planet! Our satellite scan shows that there is no significant intelligent life on this planet. In the extremely unlikelty event that you do encounter some low level lifeform, please do not acknowledge it and carry on with your mission. ")
print("Please locate and test (five) suitable excavation sites, and return your ROVER safely back to its landing dock. ")
print("And, don't worry, your ROVER is currently at the landing dock. \n")
print("You you already well know your ROVER is an extremely simple device. There are only a few things you can do:")
print("Type in 'test_soil' to test your location and determine if it is a suitable excavation site.  Type in 'drill' followed by an object to drill into it.")
print("test_soil and drill both will cost you one point of energy. You start with 3 energy, and you can get more by using: 'pickup' to gather energy crystal.")
print("Lastly you can check your energy level by typing in 'energy', you can see how many suitable excavation sites you have found by typing in 'progress', and you can see what is in your inventory by typing in 'inventory'. ")
print("This is the full extent of your ROVER's capabilites. Typing in nonexistent or unauthorized commands will risk breaking your ROVER.")
print("We know you will be successful!\n")


#game loop, DECLARE PLAYER STARTING LOCATION BEFORE ENTERING GAMELOOP
#                  [column][row]
me.location = map_array[3][4] 






running = True




while gamegoing:

    #consider refresh method / game tick: here location change tick

    
    #for when player returns to landingdock: a3, and has win condition -----> end game
    if me.location == landing and me.wincondition == True:
        print("Congratualtions Associated Remote ROVER Engineer #{}, your missions was a success! You will now be disconnected from your ROVER. Please sign back on tomorrow at 7:00 am for your next assignment. ".format(idnumber))
        quit()

#####################################TEST CONDITION AREA REMEMBER TO REMOVE AFTER USE##############################
    


###################################################################################################################




    #must update every time which is stupid
    loc_dict = {'west':me.location.west,'east':me.location.east, 'north':me.location.north, 'south':me.location.south}


    #CHANGE THIS, IF ME.LOCAITON.EVENTFLAG == TRUE THEN ME.LOCATION.EVENT
    if me.location.eventflag == True:
        
        me.location.event()

    
    

    #show greeting for specific location that just entered
    
    #if there are items in location, print their greeting so we dont forget their existence -- add this to look 
    look()
    
    #now that we have visitied with location, its firstime attribtue is false and must stay that way
    me.location.firsttime = False

    #at the moment arbitrary condition for command loop
    commanding  = True

    #begin command loop
    while commanding:
        loc_dict = {'west':me.location.west,'east':me.location.east, 'north':me.location.north, 'south':me.location.south}
        
        #consider refresh / command tick method
        
        command = input("EXECUTE COMMAND:").lower()
        print('\n')
        command = command.split()
        if len(command) == 0:
            continue
        verb = command[0]

               


        #handles location changing and failure to do so   special case for walking 
        if verb == 'go' or verb == 'walk':

            #if they only say go or walk
            if len(command) == 1:
                print("Where do you want to {} ?".format(verb))
                continue

            # me.location.west == None
            if command[1] not in loc_dict  or loc_dict[command[1]] == None :
                print("You can not go {}".format(command[1]))
                
                if command[1] in me.location.whynot:
                    print(me.location.whynot[command[1]])

                continue

            #player goes in new direciton --> update player locaiton --> end command loop
            else:
                
                #we can probably make this a controller class method
                nextLocation = loc_dict[command[1]]
                me.location =  nextLocation
                
                break


        #checks to see if there is a valid verb in command
        if verb in verbs:
            
            pass
        else:
            print("ROVER:I can only understand commands that start with a verb.")
            continue
        

        
        
        #finds number of tokens in command and sends command array to appropraite handler method    
        tokenhandler(command)
        

        

        #print empty line5
        print("\n")






    






