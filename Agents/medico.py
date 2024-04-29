from spade.agent import Agent

class medicoAgent(Agent): 
    
    def __init__(self, specialty):
        self.specialty = specialty
        
    async def setup(self):
        print ("Agent medico {}".format(str(self.jid))+ " starting...")
        