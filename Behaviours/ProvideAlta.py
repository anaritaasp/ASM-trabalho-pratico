from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored

class ProvideAlta(CyclicBehaviour):
    def __init__(self, agent):
        super().__init__()
        self.agent = agent

    async def run(self):
        msg = await self.receive(timeout=15)  # Timeout of 10 seconds
        if msg:
            per = msg.get_metadata('performative')
            if per == 'sair':
                content = msg.body.split(", ")
                patient_name = content[0].split(": ")[1]
                triagem = content[1].split(": ")[1]
                self.agent.remove_paciente(triagem)
                rep = msg.make_reply()
                rep.set_metadata('performative','out')
                rep.body = f"Out"
                await self.send(rep)
                print(colored(f"O gestor autoriza a saída do paciente {patient_name} da especialidade {triagem}.", "green"))
                