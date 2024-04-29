from spade.agent import Agent
from Behaviours.registerDoctor import RegisterDoctor
from Behaviours.giveDoctorList import SendDoctorListBehavior

class gestorUnidadeAgent(Agent): 
    
    def __init__(self, jid, name, specialty):
        super().__init__(jid, name)
        self.specialty = specialty
        
    async def setup(self): 
        print ("Agent Gestor da unidade de especialidade {}".format(str(self.jid))+ " starting...")
        self.add_behaviour(RegisterDoctor()) #behaviour para criar agentes médicos para a sua especialidade
        self.add_behaviour(SendDoctorListBehavior())