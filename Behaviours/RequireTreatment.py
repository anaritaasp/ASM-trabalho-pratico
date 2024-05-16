from spade.behaviour import OneShotBehaviour
from spade.message import Message
from termcolor import colored
from dados import XMPP_SERVER

class RequireTreatment(OneShotBehaviour):

    def __init__(self, patient_name, doctor_name):
        super().__init__()
        self.patient_name = patient_name
        self.doctor_name = doctor_name

    async def run(self):
        print(colored(f"O paciente {self.patient_name} requisita tratamento do médico {self.doctor_name}", "green"))
        medico_nome = self.doctor_name.rstrip('.')
        medico_jid = medico_nome + "@" + XMPP_SERVER
        msg = Message(to=medico_jid)
        msg.body = "Preciso de tratamento"
        rep=msg.make_reply()
        rep.set_metadata('performative','tratamento')
        await self.send(msg)
