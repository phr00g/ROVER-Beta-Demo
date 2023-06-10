
from classes import *
from locations import *
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
        




#testing torch object

# torch = item('torch')
# torch.name = 'torch'
# torch.isholdable = True
# #add pickup method to torch
# torch.verbs['pickup'] = pickup
# torch.verbs['drop'] = drop
# #print(torch.verbs)
# #torch pickup printed response


# starting_loc = location()   
# starting_loc.name = 'tutorial'
# starting_loc.greeting = 'You are surrouended by sand and the air is uncomfortably dry. You feel a bead of sweat dripping down your temple. A mahogany log cabin creaks with age. To the east you see a small castle.'

# small_castle = location()
# small_castle.greeting = 'You walk over the castle bridge and above the moat, a hungry and very ugly hippo gives you a wink that unsettles your stomach. It is too dark to see much, but there is a small fire next to a torch.'


# #adds torch item to small castle locations dictonary
# small_castle.inventory[torch.name] = torch

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
me.location = map_array[0][0] 

clock = pygame.time.Clock()



running = True
flash_timer = 0
flash_interval = 500  # milliseconds

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # # Flash the player's location
#     # current_time = pygame.time.get_ticks()

#     # if current_time - flash_timer >= flash_interval:
#     #     flash_timer = current_time
#     #     player_location = map_array[1][1] 

#     # Draw the map
#     draw_map()

#     # Control the frame rate
#     clock.tick(60)





while gamegoing:

    #consider refresh method / game tick: here location change tick


    #for when player returns to landingdock: a3, and has win condition -----> end game
    # if me.location == a3 and me.wincondition == True:
    #     print("Congratualtions Associated Remote ROVER Engineer #{}, your missions was a success! You will now be disconnected from your ROVER. Please sign back on tomorrow at 7:00 am for your next assignment. ".format(idnumber))
    #     quit()


    #at the moment arbitrary condition for command loop
    commanding  = True
    #must update every time which is stupid
    loc_dict = {'west':me.location.west,'east':me.location.east, 'north':me.location.north, 'south':me.location.south}

    #show greeting for specific location that just entered
    print(me.location.greeting)


    #begin command loop
    while commanding:
        
        #consider refresh / command tick method
        
        command = input("EXECUTE COMMAND:").lower()
        print('\n')
        command = command.split()
        verb = command[0]

        #handles commands without any verbs
        


        #handles location changing and failure to do so   special case for walking 
        if verb == 'go' or verb == 'walk':

            #if they only say go or walk
            if len(command) == 1:
                print("Where do you want to {} ?".format(verb))
                continue

            # me.location.west == None
            if command[1] not in loc_dict  or loc_dict[command[1]] == None :
                print("You can not go {}".format(command[1]))
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
        

        #here we need to accept verbs and then execute class based actions, verbs instructios should not be in command loop
        #if len(command) == 1, ==2, ==3 and so forth for different verb types
        #consider a verb handler methods for each verb type
        
        #finds number of tokens in command and sends command array to appropraite handler method    
        tokenhandler(command)
        

        #add funcitnoality that checks if plahyer's locaiton has changed, and breaks from command loop

        #print empty line
        print("\n")






    






