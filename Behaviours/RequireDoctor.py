from spade.behaviour import OneShotBehaviour
from spade.message import Message
from termcolor import colored
from dados import XMPP_SERVER

class RequireDoctor(OneShotBehaviour):
    def __init__(self, hospital,patient_name, triagem):
        super().__init__()
        self.hospital=hospital
        self.patient_name = patient_name
        self.triagem = triagem
        
    async def run(self):
        msg = Message(to=self.hospital + XMPP_SERVER)  
        msg.body = f"Paciente: {self.patient_name}, Triagem: {self.triagem}"
        msg.set_metadata("performative", "request")
        await self.send(msg)
        print(colored(f"O paciente {self.patient_name} requer um médico da especialidade {self.triagem} ao gestor do hospital {self.hospital}.", "green"))
