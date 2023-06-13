
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


       


# #game start

#intro sequence
idnumber = str(random.randint(1000,9999))
print('\n')
print("Greetings, Materials Incorporated Associated Remote ROVER Engineer #{}!  ".format(idnumber))
print("It seems that this is your first time uplinking to a ROVER, luckily since you graduated just a few weeks ago you are up to date with all of the new model's capabilities!")
print('\n')
print("As you know, Associated Remote ROVER Engineer #{}, Materials incorporated's TS909 Rover is outfitted with many cutting edge features, but most relevant to your mission its new 'drilling' feature. ".format(idnumber))
print("Materials Incorporated is looking for available and ethically reachable deposits of REDACTED , which is why your ROVER is currently located on the conveniently nearby terrestrial planet of REDACTED")
print("Please locate and test (three) suitable excavation sites, and return your ROVER safely back to its landing dock. ")
print("Don't worry, your ROVER is currently at the landing dock. And by the way, just in case your manual isn't fully up to date, to test whether your current location is suitable for drilling, just type 'test_soil'.\n")

#game loop, DECLARE PLAYER STARTING LOCATION BEFORE ENTERING GAMELOOP
#                  [column][row]
me.location = map_array[3][4] 






running = True




while gamegoing:

    #consider refresh method / game tick: here location change tick

    
    #for when player returns to landingdock: a3, and has win condition -----> end game
    # if me.location == a3 and me.wincondition == True:
    #     print("Congratualtions Associated Remote ROVER Engineer #{}, your missions was a success! You will now be disconnected from your ROVER. Please sign back on tomorrow at 7:00 am for your next assignment. ".format(idnumber))
    #     quit()



    #CHANGE THIS, IF ME.LOCAITON.EVENTFLAG == TRUE THEN ME.LOCATION.EVENT
    if me.location.eventflag == True:
        
        me.location.event()

    
    #must update every time which is stupid
    loc_dict = {'west':me.location.west,'east':me.location.east, 'north':me.location.north, 'south':me.location.south}

    #show greeting for specific location that just entered
    print(me.location.greeting) 
    
    #now that we have visitied with location, its firstime attribtue is false and must stay that way
    me.location.firsttime = False

    #at the moment arbitrary condition for command loop
    commanding  = True

    #begin command loop
    while commanding:
        
        #consider refresh / command tick method
        
        command = input("EXECUTE COMMAND:").lower()
        print('\n')
        command = command.split()
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
            print("You are gonna have to start with a verb kiddo...")
            continue
        

        
        
        #finds number of tokens in command and sends command array to appropraite handler method    
        tokenhandler(command)
        

        

        #print empty line5
        print("\n")






    






