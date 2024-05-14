from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored

class ProvideTreatment(CyclicBehaviour):
    def __init__(self, doctor_name):
        super().__init__()
        self.doctor_name = doctor_name

    async def run(self):
        msg = await self.receive(timeout=15)
        if msg:
            per = msg.get_metadata('performative')
            if per == 'tratamento': 
                if msg.body.strip() == "Preciso de tratamento":
                    print(colored(f"O médico {self.doctor_name} recebeu um pedido de tratamento do paciente {msg.sender}", "green"))
                    rep=msg.make_reply()
                    rep.set_metadata('performative','daalta')
                    rep.body = "Tratamento providenciado"
                    await self.send(rep)
            