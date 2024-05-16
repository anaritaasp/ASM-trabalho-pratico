from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored

class ReceiveFromPatient(CyclicBehaviour):
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
                self.agent.remover_paciente(triagem)
                rep = msg.make_reply()
                rep.set_metadata('performative', 'out')
                rep.body = f"Out"
                await self.send(rep)
                print(colored(f"O gestor autoriza a saída do paciente {patient_name} da especialidade {triagem}.", "green"))
            elif per == 'request':
                content = msg.body.split(", ")
                patient_name = content[0].split(": ")[1]
                triagem = content[1].split(": ")[1]
                resultado = self.agent.adicionar_paciente(triagem)
                if resultado == True: # Check availability
                    rep = msg.make_reply()
                    print(triagem)
                    medicos_assigneds = self.agent.escolher_medico(triagem)
                    doct1 = str(medicos_assigneds[0])  # Accessing the first element of the first tuple
                    doct2 = str(medicos_assigneds[1])  # Accessing the first element of the second tuple
                    rep.set_metadata('performative', 'inform')
                    rep.body = str(medicos_assigneds)
                    print("this:",rep.body)
                    await self.send(rep)
                    print(colored(f"O paciente {patient_name} deu entrada na especialidade {triagem} e pode escolher o médico {doct1} ou {doct2}.", "green"))
                elif isinstance(resultado, str) and resultado.startswith("O paciente deve ser reencaminhado para o hospital:"):
                    rep = msg.make_reply()
                    rep.set_metadata('performative', 'encaminhamento')
                    # Separar a string e pegar o segundo elemento
                    rep.body = f"O paciente deve ser encaminhado para o hospital: {self.agent.hospitalParceiro}"  # Retornar apenas a mensagem após "O paciente deve ser reencaminhado para o hospital:"
                    await self.send(rep)
                    print(colored(f"O paciente {patient_name} deve ser reencaminhado para o Hospital {self.agent.hospitalParceiro}", "green"))
                else:
                    reply_msg = Message(to=str(msg.sender))  
                    reply_msg.body = f"Não há médicos disponíveis {triagem} no momento."
                    await self.send(reply_msg)
                    print(colored(f"O paciente não foi aceite {patient_name} para a especialidade {triagem}.", "red"))
