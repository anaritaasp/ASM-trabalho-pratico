from spade.behaviour import OneShotBehaviour
from spade.message import Message
from dados import XMPP_SERVER

class SendDoctorListBehavior(OneShotBehaviour):
    async def run(self):
        # Prepare the list of doctors to send
        doctors_list = self.agent.doctors

        # Send the list of doctors to the receptionist
        msg = Message(to="rececionista@" + XMPP_SERVER)
        msg.body = "\n".join([f"{specialty}: {doctor}" for specialty, doctor in doctors_list])
        await self.send(msg)
