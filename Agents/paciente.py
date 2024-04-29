from spade.agent import Agent

class pacienteAgent(Agent): 
    async def setup(self):
        print ("Agent paciente {}".format(str(self.jid))+ " starting...")
        