from spade.agent import Agent
from aux import triagem
from Behaviours.registerPatient import registerPatientBehav

class RececionistaAgent(Agent):
    def __init__(self, jid, password, specialties_and_max, doctors_available, current_number_of_patients):
        super().__init__(jid, password)
        self.specialties_and_max = specialties_and_max
        self.doctors_available = doctors_available
        self.current_number_of_patients = current_number_of_patients


    
    async def setup(self):
        print("A agente Rececionista {} foi inicializada ..".format(str(self.jid)))
        print ("#### O Hospital UMINHO encontra-se aberto ####")
        
        
        
        
            

    
    
    
        
    
    
    


