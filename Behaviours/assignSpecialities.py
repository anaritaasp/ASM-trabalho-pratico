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

        # número máximo de pacientes
        await self.send_max_patients_info(1, specialties.keys())

        if self.agent.specialties is None:
            self.agent.specialties = specialties


        for specialty in specialties:
            gestor_name = f"Gestor de {specialty}"
            gestor_agent = gestorUnidadeAgent(f"gestor{specialty}@{XMPP_SERVER}", gestor_name, specialty)
            self.agent.add_subagent(gestor_agent)
            await gestor_agent.start()

    async def send_max_patients_info(self, max_patients, specialties):
        msg = Message(to="rececionista@" + XMPP_SERVER, body=f"{max_patients},{';'.join(specialties)}")
        await self.send(msg)
