from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored
from dados import XMPP_SERVER

class ReceiveFromGestor(CyclicBehaviour):
    def __init__(self, patient_name, triagem, hospital_name):
        super().__init__()
        self.patient_name = patient_name
        self.triagem = triagem
        self.hospital_name= hospital_name
        
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
                    print(colored(f"O paciente {self.patient_name} foi atribuido ao médico: {medico_assigned}", "green"))
            elif per == "encaminhamento":
                novo_hospital_text = msg.body  # Supondo que o corpo da mensagem contenha o nome do novo hospital
                colon_index = novo_hospital_text.find(":")
                novo_hospital = novo_hospital_text[colon_index + 1:].strip()
                print(colored(f"O paciente {self.patient_name} foi encaminhado para o hospital {novo_hospital}.", "green"))
                self.agent.changeHospital(novo_hospital)
                

            elif per == 'daalta':
                if  msg.body.strip() == "Tratamento providenciado":
                    self.alta = "alta"
                    print(colored(f"O paciente recebeu a confirmação de que o tratamento foi providenciado pelo médico {msg.sender}", "green"))
                    gestor_jid =self.hospital_name + XMPP_SERVER
                    rep = Message(to=gestor_jid)  
                    rep.body = f"Paciente: {self.patient_name}, Triagem: {self.triagem}"
                    rep.set_metadata("performative", "sair")
                    await self.send(rep)
                    print(colored(f"O paciente {self.patient_name} da especialidade {self.triagem} deve ter alta.", "green"))
            elif per == 'out':
                print(colored(f"O paciente {self.patient_name} saiu do hospital", "green"))
                await self.agent.stop()
        else:
            None 
        
