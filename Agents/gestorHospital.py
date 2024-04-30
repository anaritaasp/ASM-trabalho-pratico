from spade.agent import Agent
from Behaviours.assignSpecialities import AssignSpecialities
class gestorHospitalAgent(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specialties = None
        self.subagents = []

    def add_subagent(self, subagent):
        self.subagents.append(subagent)
        
        
    async def setup(self):
        print ("Agent Gestor Hospitalar {}".format(str(self.jid))+ " starting...")
        
        # behaviour para criar as especialidades
        self.add_behaviour(AssignSpecialities())
    

