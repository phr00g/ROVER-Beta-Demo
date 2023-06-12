from methods import *
from classes import *
#to stop random complaints
from methods import pickup,drop,verbs



torch = item('torch')
torch.verbs['pickup'] = pickup
torch.verbs['drop'] = drop

#at landing
crystal1 = item('crystal')
crystal1.verbs['pickup'] = pickup
crystal1.iscrystal = True


#on dead roger body
crystal2 = item('crystal')
crystal2.verbs['pickup'] = pickup
crystal2.iscrystal = True
