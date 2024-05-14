from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored
from dados import XMPP_SERVER

class ReceiveFromGestor(CyclicBehaviour):
    def __init__(self, patient_name, triagem):
        super().__init__()
        self.patient_name = patient_name
        self.triagem = triagem
        
    async def run(self):
        msg = await self.receive(timeout=15)  
        if msg:
            per = msg.get_metadata('performative')
            #print(msg.body)
            if per == 'inform':
                content = msg.body.split(": ")
                if len(content) == 2 and content[0] == "O médico é":
                    medico_assigned = content[1]
                    self.agent.set_medico_assigned(medico_assigned)
                    print(colored(f"O paciente foi atribuido ao médico: {medico_assigned}", "green"))
            elif per == 'daalta':
                if  msg.body.strip() == "Tratamento providenciado":
                    self.alta = "alta"
                    print(colored(f"O paciente recebeu a confirmação de que o tratamento foi providenciado pelo médico {msg.sender}", "green"))
                    rep = Message(to="gestHospital@" + XMPP_SERVER)  
                    rep.body = f"Paciente: {self.patient_name}, Triagem: {self.triagem}"
                    rep.set_metadata("performative", "sair")
                    await self.send(rep)
                    print(colored(f"O paciente {self.patient_name} da especialidade {self.triagem} deve ter alta.", "green"))
            elif per == 'out':
                print(colored(f"O paciente {self.patient_name} saiu do hospital", "green"))
                await self.agent.stop()
        else:
            print(colored("1-Unexpected message format.", "red"))
        
