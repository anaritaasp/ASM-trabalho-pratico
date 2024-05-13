from spade.agent import Agent
from aux import triagem
from Behaviours.ReceiveDoctorRequest import ReceiveDoctorRequest
from termcolor import colored
import random

class gestorHospitalAgent(Agent):
    def __init__(self, jid, password, specialties_and_max, doctors_available):
        super().__init__(jid, password)
        self.specialties_and_max = specialties_and_max
        self.doctors_available = doctors_available

    async def setup(self):
        print(colored("O agente gestor do Hospital {} foi inicializada ..".format(str(self.jid)),"blue"))
        print (colored("#### O Hospital UMINHO encontra-se aberto ####","blue"))
        entradaPacientes = ReceiveDoctorRequest(self)
        self.add_behaviour(entradaPacientes)
        
    def escolher_medico(self,specialty):
        if specialty in self.doctors_available:
                doctors_list = self.doctors_available[specialty]
                if doctors_list:
                    return random.choice(doctors_list)
                else:
                    print(f"Não há medicos disponíveis para essa especialidade {specialty}.")
                    return None
        else:
                print(f"A especialidade providenciada {specialty} não foi encontrada.")
                return None
            
    def adicionar_paciente(self, especialidade):
        if especialidade in self.specialties_and_max:
            maximo = self.specialties_and_max[especialidade][0]
            novo_valor = self.specialties_and_max[especialidade][1] + 1
            if novo_valor <= maximo:
                self.specialties_and_max[especialidade] = (maximo, novo_valor)
                return True
            else:
                return False # a especialidade está cheia
        else:
            return False # a especialidade não foi encontrada (just in case)




        
        
        
        
        
            

    
    
    
        
    
    
    


