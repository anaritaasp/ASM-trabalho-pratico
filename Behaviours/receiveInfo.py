from spade.behaviour import OneShotBehaviour
from spade.message import Message

class ReceiveMaxPatientsBehavior(OneShotBehaviour):
    async def run(self):
        msg = await self.receive(timeout=60)  # Wait for a message for 60 seconds
        if msg:
            # Parse the message to extract max patients and specialties
            max_patients, specialties = msg.body.split(',')
            max_patients = int(max_patients)
            specialties = specialties.split(';')
            
            # Save the received max patients and specialties in the agent's attributes
            self.agent.max_patients = max_patients
            self.agent.specialties = specialties
            self.agent.current_patients = 0
            
            print("A rececionista recebeu a informação de início.")
        else:
            print("A rececionista timed out enquanto esperava.")
