from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from Behaviours.receiveInfo import ReceiveMaxPatientsBehavior
from Behaviours.receiveDoctorList import ReceiveDoctorListBehavior
from Behaviours.handlePatient import HandlePatientRequests

class RececionistaAgent(Agent):
    async def setup(self):
        print("Agent Rececionista {} starting...".format(str(self.jid)))
        
        # Add behavior to receive max patients and specialties
        self.add_behaviour(ReceiveMaxPatientsBehavior())
        self.add_behaviour(ReceiveDoctorListBehavior())
        self.add_behaviour(HandlePatientRequests())

