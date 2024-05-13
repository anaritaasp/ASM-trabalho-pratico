from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored

class ReceiveDoctorRequest(CyclicBehaviour):
    def __init__(self, agent):
        super().__init__()
        self.agent = agent

    async def run(self):
        msg = await self.receive(timeout=15)  # Timeout of 10 seconds
        if msg:
            content = msg.body.split(", ")
            patient_name = content[0].split(": ")[1]
            triagem = content[1].split(": ")[1]
            if self.agent.adicionar_paciente(triagem) == True:  # Check availability
                rep = msg.make_reply()
                print(msg.sender)
                medico_assigned = self.agent.escolher_medico(triagem)
                rep.set_metadata('performative','inform')
                rep.body = f"O médico é: {medico_assigned}."
                await self.send(rep)
                print(colored(f"O paciente {patient_name} deu entrada na especialidade {triagem} com o medico {medico_assigned}.", "green"))
            else:
                reply_msg = Message(to=msg.sender)
                reply_msg.body = f"Não há medicos disponiveis {triagem} no momento."
                await self.send(reply_msg)
                print(colored(f"O paciente não foi aceite {patient_name} para a especialidade {triagem}.", "red"))
        