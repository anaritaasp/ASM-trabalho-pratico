"""from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored

class ReceiveDoctorRequest(CyclicBehaviour):
    def __init__(self, agent):
        super().__init__()
        self.agent = agent

    async def run(self):
        msg = await self.receive(timeout=10)  # Timeout of 10 seconds
        if msg:
            content = msg.body.split(", ")
            patient_name = content[0].split(": ")[1]
            triagem = content[1].split(": ")[1]
            if self.agent.adicionarPaciente(triagem) == True:  # Check availability
                reply_msg = Message(to=msg.sender)
                reply_msg.body = f"Deu entrada no hospital."
                self.agent.
                await self.send(reply_msg)
                print(colored(f"O paciente {patient_name} deu entrada na especialidade {triagem}.", "green"))
            else:
                reply_msg = Message(to=msg.sender)
                reply_msg.body = f"Sorry, there are no available doctors for triage {triagem} at the moment."
                await self.send(reply_msg)
                print(colored(f"Rejected patient {patient_name} with triage {triagem}.", "red"))
        else:
            print("No message received.")"""