import time
from spade.message import Message
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour

class PatientAgent(Agent):
    async def setup(self):
        print(f"Patient Agent {self.jid} is starting")
        self.specialty = self.get('specialty')
        self.service_contact = self.get('service_contact')
        print(f"Patient Agent {self.jid} needs {self.specialty} service")

        request_behaviour = self.RequestSpecialtyBehaviour()
        self.add_behaviour(request_behaviour)

    class RequestSpecialtyBehaviour(OneShotBehaviour):
        async def run(self):
            print(f"Patient Agent {self.agent.jid} is requesting {self.agent.specialty} service")
            msg = await self.send(Message(to=self.agent.service_contact, body=f"I need {self.agent.specialty} service"))

            print(f"Patient Agent {self.agent.jid} sent request: {msg}")
