import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class SpecialtyManagerAgent(Agent):
    def __init__(self, jid, password, max_patients_per_specialty,currpatients, agent_manager=None):
        super().__init__(jid, password)
        self.agent_manager = agent_manager
        self.max_patients_per_specialty = max_patients_per_specialty
        self.current_patients =
        
    async def get_specialty(self):
        # Replace this with your actual implementation to get the specialty
        # For example, you might retrieve it from a database or configuration file
        return "Cardiologia"

    async def setup(self):
        print(f"Agente de gestão de especialidade {self.jid} está a começar")
        self.specialty = await self.get_specialty()
        if self.specialty is None:
            print("Erro: Não foi possível encontrar a especialidade.")
            return
        self.max_patients = self.max_patients_per_specialty.get(self.specialty)
        if self.max_patients is None:
            print("Erro: Naõ foi possível obter o número máximo de pacientes.")
            return
        print(f"O agente {self.jid} controla a especialidade {self.specialty} com um máximo de {self.max_patients} pacientes.")

        alert_behaviour = self.AlertHospitalBehaviour()
        self.add_behaviour(alert_behaviour)


    class AlertHospitalBehaviour(CyclicBehaviour):
        async def run(self):
            # Conta o número de agentes pacientes que são controlados pelos agentes de especialidade
            patient_count = sum(1 for agent in self.agent. if agent.specialty == self.agent.specialty)
            if patient_count > self.agent.max_patients:
                print(f"Alertar o gestor hospitalar: a especialidade {self.agent.specialty} excedeu o número máximo de pacientes.")
                msg = Message()
                msg.to = self.agent.agent_manager.hospital_manager_jid
                msg.body = f"A especialidade {self.agent.specialty} excedeu o número máximo de pacientes."
                await self.send(msg)
            await asyncio.sleep(10)  # Check every 10 seconds