import asyncio
from spade.agent import Agent
from termcolor import colored
from Behaviours.RequireDoctor import RequireDoctor
from Behaviours.ReceiveFromGestor import ReceiveFromGestor
from Behaviours.RequireTreatment import RequireTreatment
class pacienteAgent(Agent): 
    
    def __init__(self, jid, password, a_name, triagem):
         super().__init__(jid, password)
         self.a_name = a_name
         self.triagem = triagem
         self.medico_assigned= None # inicializamos o nome do doutor como None
         self.alta = None
         self.estado = None
        
        
    async def setup(self):
        print (colored("O paciente {}".format(str(self.jid))+ " foi inicializado ...","blue"))
        if self.get("status") == "não_atendido":
            ask_for_doctor=RequireDoctor(self.a_name,self.triagem)
            self.add_behaviour(ask_for_doctor)
            get_doctor = ReceiveFromGestor(self.a_name,self.triagem)
            self.add_behaviour(get_doctor)
    
    
    def set_medico_assigned(self, medico_name):
        self.medico_assigned = medico_name
        print(colored("Médico atribuído:", "green"), medico_name)
        if self.medico_assigned is not None:
            ask_for_treatment = RequireTreatment(self.a_name, self.medico_assigned)
            self.add_behaviour(ask_for_treatment)
            print(colored("Pedido de tratamento adicionado.", "green"))
    
    
    def set_estado(self, estado):
        self.estado= estado
        if self.alta == "out":
            print(f"O paciente {self.a_name} saiu do hospital")
            self.stop()
        
            