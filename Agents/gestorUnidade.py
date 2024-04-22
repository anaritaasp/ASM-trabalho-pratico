import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class SpecialtyManagerAgent(Agent):
    async def setup(self):
        print(f"Specialty Manager Agent {self.jid} is starting")
        self.specialty = self.get('specialty')
        self.max_patients = self.get('max_patients')
        print(f"Specialty Manager Agent {self.jid} manages {self.specialty} with maximum {self.max_patients} patients")

        alert_behaviour = self.AlertHospitalBehaviour()
        self.add_behaviour(alert_behaviour)

    class AlertHospitalBehaviour(CyclicBehaviour):
        async def run(self):
            # Count the number of patient agents managed by this specialty manager
            patient_count = sum(1 for agent in self.agent.agent_manager.agent_list if agent.specialty == self.agent.specialty)
            if patient_count > self.agent.max_patients:
                print(f"Alerting Hospital Manager: {self.agent.specialty} has exceeded the maximum number of patients")
                msg = Message(to=self.agent.agent_manager.hospital_manager_jid)
                msg.body = f"{self.agent.specialty} has exceeded the maximum number of patients"
                await self.send(msg)
            await asyncio.sleep(10)  # Check every 10 seconds
