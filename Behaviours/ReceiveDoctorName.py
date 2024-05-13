from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored

class ReceiveDoctorName(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=15)  # Timeout of 10 seconds
        if msg:
            per = msg.get_metadata('performative')
            if per == 'inform':
                print('entrei')
                content = msg.body.split(": ")
                if len(content) == 2 and content[0] == "O médico é":
                    medico_assigned = content[1]
                    self.agent.set_medico_assigned(medico_assigned)
                    print(colored(f"Received doctor assignment: {medico_assigned}", "blue"))
            else:
                print(colored("Unexpected message format.", "red"))
        
