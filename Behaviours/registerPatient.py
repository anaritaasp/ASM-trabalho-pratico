from spade.behaviour import PeriodicBehaviour
from dados import XMPP_SERVER, PASSWORD
from Agents.paciente import pacienteAgent
from aux import generate_patient_number
from spade.agent import Agent
from spade.message import Message  

class createPatientAgent(PeriodicBehaviour):
    
    def createPatient():
        patient_id = generate_patient_number
        patientAgent = pacienteAgent(f"{patient_id}@{XMPP_SERVER}", patient_id)
        res_patient_agent= patientAgent.start(auto_register=True)
        res_patient_agent.result()
    