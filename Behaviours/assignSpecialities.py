from spade.behaviour import OneShotBehaviour
from spade.message import Message
from Agents.gestorUnidade import gestorUnidadeAgent
from dados import XMPP_SERVER

class AssignSpecialities(OneShotBehaviour):
    async def run(self):
        # Available specialties
        specialties = {
            "Cardiologia": 1,
            "Neurologia": 1,
            "Pediatria": 1
        }

        # Indicate the need to create agents
        self.add_data_received_event(Message)

        # Send max patients and specialties info to the receptionist
        await self.send_max_patients_info(10, specialties.keys())

        if self.agent.specialties is None:
            self.agent.specialties = specialties

        # Check for incoming message to create director agents
        msg = await self.receive(timeout=60)
        if msg and msg.body == "CreateDirectorAgents":
            # Create an agent for each specialty
            for specialty in specialties:
                gestor_name = f"Gestor de {specialty}"
                gestor_agent = gestorUnidadeAgent(f"gestor{specialty}@{XMPP_SERVER}", gestor_name, specialty)
                self.agent.add_subagent(gestor_agent)

    async def send_max_patients_info(self, max_patients, specialties):
        msg = Message(to="rececionista@" + XMPP_SERVER, body=f"{max_patients},{';'.join(specialties)}")
        await self.send(msg)
