from spade.agent import Agent
from aux import triagem
from Behaviours.ReceiveFromPatient import ReceiveFromPatient
from Behaviours.ProvideAlta import ProvideAlta
from termcolor import colored
import random

class gestorHospitalAgent(Agent):
    def __init__(self, jid, password, specialties_and_max, doctors_available,hospitalParceiro, hospital_name):
        super().__init__(jid, password)
        self.specialties_and_max = specialties_and_max
        self.doctors_available = doctors_available
        self.hospitalParceiro = hospitalParceiro
        self.hospital_name= hospital_name

    async def setup(self):
        print(colored("O agente gestor do Hospital {} foi inicializado ..".format(str(self.jid)),"blue"))
        print (colored(f"#### O Hospital {self.hospital_name} encontra-se aberto ####","yellow"))
        entradaPacientes = ReceiveFromPatient(self)
        self.add_behaviour(entradaPacientes)
        saidaPacientes = ProvideAlta(self)
        self.add_behaviour(saidaPacientes)
        
    def escolher_medico(self,specialty):
        if specialty in self.doctors_available:
                doctors_list = self.doctors_available[specialty]
                if doctors_list:
                    return random.choice(doctors_list)
                else:
                    print(f"Não há medicos disponíveis para essa especialidade {specialty}.")
                    return None
        else:
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
             return f"O paciente deve ser reencaminhado para o hospital: {self.hospitalParceiro}" # a especialidade não foi encontrada (just in case)
    
    def remover_paciente(self, especialidade):
        if especialidade in self.specialties_and_max:
            maximo = self.specialties_and_max[especialidade][0]
            novo_valor = self.specialties_and_max[especialidade][1] - 1
            self.specialties_and_max[especialidade] = (maximo, novo_valor)




        
        
        
        
        
            

    
    
    
        
    
    
    


