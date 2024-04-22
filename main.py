import time
from spade import quit_spade
from Agents.manager import ManagerAgent
from Agents.paciente import PatientAgent
from Agents.medico import DoctorAgent
from Agents.gestorUnidade import SpecialtyManagerAgent
from Agents.gestorHospitalar import HospitalManagerAgent

XMPP_SERVER = "anaritaasp-nitro-an515-55"
PASSWORD = "NOPASSWORD"

MAX_PATIENTS_PER_SPECIALTY = {
    "Cardiologia": 10,
    "Pediatria": 5,
    "Neurologia": 8,
}

def main():
    # Create Hospital Manager Agent instance
    hospital_manager_jid = 'hospital_manager@' + XMPP_SERVER
    hospital_manager_agent = HospitalManagerAgent(hospital_manager_jid, PASSWORD)

    # Start Hospital Manager Agent and wait for it to be ready
    res_hospital_manager = hospital_manager_agent.start(auto_register=True)
    res_hospital_manager.result()

    # Create Specialty Manager Agents for each specialty
    specialty_managers = {}
    for specialty in MAX_PATIENTS_PER_SPECIALTY:
        specialty_manager_jid = f'{specialty.lower()}_manager@{XMPP_SERVER}'
        specialty_managers[specialty] = SpecialtyManagerAgent(specialty_manager_jid, PASSWORD)

        # Start Specialty Manager Agents
        res_specialty_manager = specialty_managers[specialty].start(auto_register=True)
        res_specialty_manager.result()

    # Initialize lists to save all active Agents
    patient_agents_list = []
    doctor_agents_list = []

    # Connect Patient Agents and Doctor Agents and start them
    for specialty, max_patients in MAX_PATIENTS_PER_SPECIALTY.items():
        specialty_manager_jid = specialty_managers[specialty].jid
        for i in range(1, max_patients + 1):
            # Sleep 1 second for each 10 patient agents added
            if i % 10 == 0:
                time.sleep(1)

            patient_jid = f'patient_{specialty.lower()}{i}@{XMPP_SERVER}'
            patient_agent = PatientAgent(patient_jid, PASSWORD)
            patient_agent.set('service_contact', specialty_manager_jid)
            patient_agent.set('specialty', specialty)
            res_patient_agent = patient_agent.start(auto_register=True)
            res_patient_agent.result()
            patient_agents_list.append(patient_agent)

            doctor_jid = f'doctor_{specialty.lower()}{i}@{XMPP_SERVER}'
            doctor_agent = DoctorAgent(doctor_jid, PASSWORD)
            doctor_agent.set('service_contact', specialty_manager_jid)
            doctor_agent.set('specialty', specialty)
            res_doctor_agent = doctor_agent.start(auto_register=True)
            res_doctor_agent.result()
            doctor_agents_list.append(doctor_agent)

    # Handle interruption of all agents
    while hospital_manager_agent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            # Stop all Patient Agents
            for patient_agent in patient_agents_list:
                patient_agent.stop()

            # Stop all Doctor Agents
            for doctor_agent in doctor_agents_list:
                doctor_agent.stop()

            # Stop Hospital Manager Agent
            hospital_manager_agent.stop()
            break

    print('Agents finished')

    # Finish all the agents and behaviors running in your process
    quit_spade()

if __name__ == '__main__':
    main()
