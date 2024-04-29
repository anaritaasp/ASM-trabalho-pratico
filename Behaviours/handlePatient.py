import random
import asyncio
from spade.behaviour import PeriodicBehaviour
from spade.agent import Agent
from spade.message import Message  
from Agents.paciente import pacienteAgent  
from dados import XMPP_SERVER

class HandlePatientRequests(PeriodicBehaviour):
    async def run(self):
         # Check if the number of current patients is less than the maximum allowed
        if self.agent.current_patients < self.agent.max_patients:
        # a "triagem" designa uma determinada especialidade para o paciente
            specialty = random.choice(self.agent.specialties)
            
            # o paciente é identificado pelo seu nr de utente (número random)
            patient_name = f"Paciente_{random.randint(1, 1000)}" 
            print(f"Paciente {patient_name} precisa da especialidade {specialty}...")

            # Criamos o agente paciente e a sua especialidade
            patient_agent = pacienteAgent(f"{patient_name}@{XMPP_SERVER}", specialty)
            await patient_agent.start()
            
            self.agent.current_patients += 1
            
            # tempo entre a chegada de pacientes novos
            await asyncio.sleep(5)
        
    async def find_doctor(self, specialty):
        # temos a lista de médicos
        doctors = [(spec, name) for spec, name in self.agent.received_doctors if spec == specialty]
        return doctors


    async def assign_doctor(self, patient_name, specialty):
        doctors = await self.find_doctor(specialty)
        if doctors:
            selected_doctor = random.choice(doctors)[1]  
            print(f"O médico {selected_doctor} vai tratar do paciente {patient_name}")

            # Simular o tempo de tratamento
            await asyncio.sleep(4)  # Adjust the delay time as needed
            
            print(f"O paciente {patient_name} foi tratado")

            # Kill the patient agent and reduce the number of current patients
            await self.kill_patient(patient_name)
            self.agent.current_patients -= 1

        else:
            print("Nenhum médico se encontra disponível para a especialidade.")
