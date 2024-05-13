from spade.agent import Agent
from termcolor import colored
from Behaviours.ProvideTreatment import ProvideTreatment

class medicoAgent(Agent): 

    def __init__(self, jid, password, a_name, specialty):
         super().__init__(jid, password)
         self.a_name = a_name
         self.specialty = specialty
        
        
    async def setup(self):
        print (colored("O agente medico  {}".format(str(self.jid))+ " foi inicializado ...","blue"))
        tratamento_resposta = ProvideTreatment(self.a_name)
        self.add_behaviour(tratamento_resposta)
        