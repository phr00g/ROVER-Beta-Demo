from classes import *

#private methods ----------------------------------------------------------------

def open_image(file_name):
    folder_path = 'images'
    file_path = os.path.join(folder_path, file_name)
    os.startfile(file_path)
        




#ALL VERB METHODS GO BELOW : PUBLIC METHODS PRIVATE ABOVE

def pickup(item): #item is an object from item class

    
    if item.iscrystal == False:
        #add item from location to inventory
        me.inventory[item.name] = me.location.inventory[item.name]
        print(item.onpickup)
    else:
        me.energy += 1
        print("You now have {} energy!".format(me.energy))
    
    #remove item from location
    me.location.inventory.pop(item.name)
    
    me.location.update()
    
    

    if item.onpickupgreeting != None:
        me.location.greeting += item.onpickupgreeting





def drop(item):#arg is item object, drop item leaves player inventory enters current location inventory, inverse of pickup
    if item.name in me.inventory:
    #adds item object to current location inventory dictinoary item.name:item
        me.location.inventory[item.name] = me.inventory[item.name]

        #removes item from player inventory 
        me.inventory.pop(item.name)

        #print dropped message
        print(item.ondrop)
    
    else:
        print("You can't drop what you dont have :(")



def showinventory():
    if len(me.inventory) == 0:
        print("You have nothing in your inventory! ")
    else:
        for key in me.inventory:
            print(key)



#look method just reprints current location greeting:

def look():
    print(me.location.greeting)

def nullverb(): #this method is for verbs we want to recognize as reasonable but can not be done, 
                #for the sake of adding verb to verbs dictinoary:  'nullverb' : nullverb
    pass

def test_soil():



    #check if player has energy
    if me.energy >= 1:

        if me.location.istestable == True and me.location.hasbeentested == False:
            
            #remove 1 energy
            me.energy -= 1

            if me.location.hasmineral == True:
                #remove mineral from location
                me.location.hasmineral = False
                me.location.istestable == False
                me.location.hasbeentested == True
                print("You have tested and found this site suitable for excavation! Good job!")
                me.location.greeting += "You have tested and found this site suitable for excavation! Good job!"

                me.minerals += 1

                if me.minerals == 3:
                    #have the win condition and other stuff happen

                    print("Good job! Return to the landing dock for extraction and to complete your mission!")
                    me.wincondition  = True
                    pass


            else:
                print("ROVER:You have tested this site, and it site is not suitable for excavation.")
                print("ROVER:You now have {} energy".format(me.energy))
                me.location.greeting += "This site is not suitable for excavation."
            
            me.location.hasbeentested = True

        elif me.location.hasbeentested == True:
            print("ROVER: You can not test this site, as it has already been tested")

        else:
            print('ROVER: You can not test this site')


    else:
        print("You have no energy to drill!")



def energy():
    if me.energy >= 1:
        print("ROVER:You have {} energy!".format(me.energy))

    else:
        print("ROVER:You are completely out of energy! Explore around and find an energy crystal so you can proceeed with your mission!")

def loot(deadguy):
    if deadguy.isalive == False:
        print("ROVER:After searching through the soma of the {} we found:".format(deadguy.name))
        
        for key, val in deadguy.inventory.items():
            if val.iscrystal == True:
                me.energy += 1
                
                print("An energy crystal!")

            else:
                me.inventory[key] = val
                
                print("A {}".format(key))

        deadguy.verbs.pop('loot')
        deadguy.inventory = {}



#so far can only handle drillign people
def drill(itemperson):
    #if the thing is a person
    if itemperson.isalive == True:
        if itemperson.deathscream != "":
            print("ROVER:Right before I performed a drill operation on the {}, it tried to say something:".format(itemperson.name))
            print(itemperson.deathscream)
        print("ROVER:The {} is no more".format(itemperson.name))
        itemperson.isalive =False
        itemperson.verbs.pop('drill')
        itemperson.verbs['loot'] = loot
    me.location.update()








#verbs are methods, all verbs should be defined above ----------------------------------------------------------------------------------------------

#need single verbs dictionary
singleverbs = {'inventory':showinventory,'look':look,'test_soil':test_soil,'energy':energy}




#this should be a dictinoary 'verb':verb/method
verbs = {'pickup':pickup,'inventory':showinventory,'drop':drop,'loot':loot,'drill':drill}

#add singleverbs to verbs
verbs.update(singleverbs)