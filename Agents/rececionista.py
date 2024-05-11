from spade.agent import Agent
#from Behaviours.registerPatient import receivePatient

class RececionistaAgent(Agent):
    def __init__(self, *args, specialties_info=None, doctors_available=None,**kwargs):
        super().__init__(*args, **kwargs)
        self.specialties_info = specialties_info
        self.doctors_available = doctors_available
    
    async def setup(self):
        print("A agente Rececionista {} foi inicializada ..".format(str(self.jid)))
        print ("#### O Hospital UMINHO encontra-se aberto ####")
        
            

    
    
    
        
    
    
    


