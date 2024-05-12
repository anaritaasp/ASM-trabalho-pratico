from spade import agent
from termcolor import colored

class gestorUnidadeAgent(agent.Agent): 
    
    def __init__(self, jid, password,specialty):
         super().__init__(jid, password)
         self.specialty = specialty
        
    async def setup(self): 
        print (colored("O agente gestor da unidade de especialidade  {}".format(str(self.jid))+ "  foi inicializado...","blue"))
    
