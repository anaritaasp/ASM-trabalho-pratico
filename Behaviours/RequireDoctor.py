from spade.behaviour import OneShotBehaviour
from spade.message import Message
from termcolor import colored
from dados import XMPP_SERVER

class RequireDoctor(OneShotBehaviour):
    def __init__(self, patient_name, triagem):
        super().__init__()
        self.patient_name = patient_name
        self.triagem = triagem
        
    async def run(self):
        print("Requisito de médico")
        msg = Message(to="gestHospital@" + XMPP_SERVER)  
        msg.body = f"Paciente: {self.patient_name}, Triagem: {self.triagem}"
        msg.set_metadata("performative", "request")
        await self.send(msg)
        print(colored(f"Sent request from {self.patient_name} for a doctor with triage {self.triagem} to gestHospital.", "green"))
