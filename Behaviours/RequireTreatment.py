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
        medico_nome= self.doctor_name.strip()
        medico_jid= medico_nome+"@"+XMPP_SERVER #por algum motivo tá com .
        medico_jid_limpo = medico_jid.split('.')[0] #remove .
        #print(medico_jid_limpo)
        msg = Message(to=str(medico_jid_limpo))
        msg.body = "Preciso de tratamento"
        await self.send(msg)
