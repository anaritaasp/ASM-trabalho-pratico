from spade.behaviour import OneShotBehaviour
from Agents.medico import medicoAgent
import random

class RegisterDoctor(OneShotBehaviour):
    
    async def run(self):
        try:
            print(f"A criar médicos da especialidade : {self.agent.specialty}")
            
            # Initialize doctor list if not already initialized
            if not hasattr(self.agent, 'doctors'):
                self.agent.doctors = []

            # Insert doctors into the list
            for _ in range(2):
                doctor_name = f"Doctor_{random.randint(1, 1000)}"
                self.agent.doctors.append((self.agent.specialty, doctor_name))
                
            print("Médicos registados com sucesso.")
        
        except Exception as e:
            print(f"Erro ao registar os médicos: {e}")
