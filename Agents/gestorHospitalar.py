import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class HospitalManagerAgent(Agent):
    async def setup(self):
        print(f"O agente de gestão hospitalar {self.jid} está a começar")

        alert_behaviour = self.AlertBehaviour()
        self.add_behaviour(alert_behaviour)

    class AlertBehaviour(CyclicBehaviour):
        async def run(self):
            # Wait for alert messages from SpecialtyManagerAgents
            msg = await self.receive(timeout=10)
            if msg:
                print(f"Received alert: {msg.body} from {msg.sender}")
                # Handle the alert message here, for example, send notifications to relevant stakeholders
            else:
                print("No alerts received")
            await asyncio.sleep(10)  # Check for alerts every 10 seconds