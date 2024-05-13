from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored

class ProvideTreatment(CyclicBehaviour):
    def __init__(self, doctor_name):
        super().__init__()
        self.doctor_name = doctor_name

    async def run(self):
        msg = await self.receive(timeout=15) 
        #print("Message Received:", msg.body)
        if msg and msg.body.strip() == "Preciso de tratamento":
            print(colored(f"O médico {self.doctor_name} recebeu um pedido de tratamento do paciente {msg.sender}", "blue"))
            reply_msg = Message(to=msg.sender)
            reply_msg.body = "Tratamento providenciado"
            await self.send(reply_msg)