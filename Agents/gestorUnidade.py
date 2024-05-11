from spade import agent


class gestorUnidadeAgent(agent.Agent): 
    
    def __init__(self, jid, name, specialty):
        super().__init__(jid, name)
        self.specialty = specialty
        
    async def setup(self): 
        print ("O agente Gestor da unidade de especialidade  {}".format(str(self.jid))+ "  foi inicializado...")
