from spade.agent import Agent

class ManagerAgent(Agent):
    def __init__(self, jid, password):
        super().__init__(jid, password)

    async def setup(self):
        print(f"Manager Agent {self.jid} is starting")

    def stop(self):
        print(f"Manager Agent {self.jid} is stopping")
        super().stop()
