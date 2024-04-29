from spade.agent import Agent
from Behaviours.assignSpecialities import AssignSpecialities
class gestorHospitalAgent(Agent): 
    async def setup(self):
        print ("Agent Gestor Hospitalar {}".format(str(self.jid))+ " starting...")
        
        # behaviour para criar as especialidades
        self.add_behaviour(AssignSpecialities())
    

