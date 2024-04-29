from spade.behaviour import OneShotBehaviour
from spade.message import Message

class ReceiveDoctorListBehavior(OneShotBehaviour):
    async def run(self):
        # Wait for message from gestorUnidadeAgent with the list of doctors
        msg = await self.receive(timeout=60)
        if msg:
            # Parse the message body to extract the list of doctors
            doctors_list = msg.body.split('\n')
            # Print or process the list of doctors as needed
            print("Received list of doctors:")
            for doctor_info in doctors_list:
                print(doctor_info)
        else:
            print("Did not receive list of doctors within timeout period.")
