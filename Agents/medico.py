import time
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour

class DoctorAgent(Agent):
    async def setup(self):
        print(f"Doctor Agent {self.jid} is starting")
        self.specialty = self.get('specialty')
        self.service_contact = self.get('service_contact')
        print(f"Doctor Agent {self.jid} provides {self.specialty} service")

        response_behaviour = self.ResponseSpecialtyBehaviour()
        self.add_behaviour(response_behaviour)

    class ResponseSpecialtyBehaviour(OneShotBehaviour):
        async def run(self):
            print(f"Doctor Agent {self.agent.jid} is waiting for {self.agent.specialty} service request")
            msg = await self.receive(timeout=10)
            if msg:
                print(f"Doctor Agent {self.agent.jid} received request: {msg.body}")
                await self.send(
                    to=msg.sender,
                    body=f"{self.agent.specialty} service provided by {self.agent.jid}"
                )
            else:
                print(f"No request received for {self.agent.specialty} service")

