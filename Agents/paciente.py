from spade.agent import Agent
from termcolor import colored
from Behaviours.RequireDoctor import RequireDoctor

class pacienteAgent(Agent): 
    
    def __init__(self, jid, password, a_name, triagem):
         super().__init__(jid, password)
         self.a_name = a_name
         self.triagem = triagem
        
        
    async def setup(self):
        print (colored("O paciente {}".format(str(self.jid))+ " foi inicializado ...","blue"))
        if self.get("status") == "não_atendido":
            ask_for_doctor=RequireDoctor(self.triagem)
            self.add_behaviour(ask_for_doctor)