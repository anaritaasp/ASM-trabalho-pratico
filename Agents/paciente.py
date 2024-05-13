from spade.agent import Agent
from termcolor import colored
from Behaviours.RequireDoctor import RequireDoctor
from Behaviours.ReceiveDoctorName import ReceiveDoctorName

class pacienteAgent(Agent): 
    
    def __init__(self, jid, password, a_name, triagem):
         super().__init__(jid, password)
         self.a_name = a_name
         self.triagem = triagem
         self.medico_assigned= None # inicializamos o nome do doutor como None
        
        
    async def setup(self):
        print (colored("O paciente {}".format(str(self.jid))+ " foi inicializado ...","blue"))
        if self.get("status") == "não_atendido":
            ask_for_doctor=RequireDoctor(self.a_name,self.triagem)
            self.add_behaviour(ask_for_doctor)
            receive_Doctor_name = ReceiveDoctorName()
            self.add_behaviour(receive_Doctor_name)
    
    def set_medico_assigned(self, medico_name):
        self.medico_assigned= medico_name