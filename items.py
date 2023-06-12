from classes import *

torch = item('torch')
torch.verbs['pickup'] = pickup
torch.verbs['drop'] = drop


crystal1 = item('crystal')
crystal1.verbs['pickup'] = pickup
crystal1.iscrystal = True




