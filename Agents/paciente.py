from spade.agent import Agent

class pacienteAgent(Agent): 
    
    def __init__(self, jid, name):
        super().__init__(jid, name)
    
    async def setup(self): 
        print ("O agente Paciente  {}".format(str(self.jid))+ "  deu entrada no hospital...")

    async def kill(self):
        print("O agente Paciente {} teve alta do hospital...".format(str(self.jid)))
        await self.stop()  