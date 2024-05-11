from spade.agent import Agent

class medicoAgent(Agent): 
    
    def __init__(self, jid, name, specialty):
        super().__init__(jid, name)
        self.specialty = specialty
        
        
    async def setup(self):
        print ("O agente medico  {}".format(str(self.jid))+ " foi inicializado ...")
        