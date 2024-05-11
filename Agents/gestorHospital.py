from spade.agent import Agent
from spade.agent import Message

class gestorHospitalAgent(Agent):
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)
        
    async def setup(self):
        print("O agente Gestor Hospitalar {} foi inicializado...".format(str(self.jid)))
        
    
    

