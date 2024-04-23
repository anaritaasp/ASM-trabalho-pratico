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
    "Cardiologia": 1,
    "Pediatria": 1,
    "Neurologia": 1,
}

def main():
    # Criar a instância do gestor hospitalar
    # O gestor hospitalar representa o individuo que gere o hospital
    hospital_manager_jid = 'hospital_manager@' + XMPP_SERVER
    hospital_manager_agent = HospitalManagerAgent(hospital_manager_jid, PASSWORD)

    # Iniciar o agente do gestor hospitalar e esperar que fique pronto
    res_hospital_manager = hospital_manager_agent.start(auto_register=True)
    res_hospital_manager.result()

    # Criamos gestores para cada especialidade do hospital
    # um gestor para a unidade de cardiologia, um para a pediatria e outro para a neurologia 
    # estes gestores devem servir de ponte de comunicação entre os médicos e os pacientes e o gestor do hospital
    # ele deve passar informações ao gestor hospitalar sobre se já se excedeu o número máximo de pacientes para cada unidade
    specialty_managers = {}
    for specialty in MAX_PATIENTS_PER_SPECIALTY:
            specialty_manager_jid = f'{specialty.lower()}_manager@{XMPP_SERVER}'
            specialty_managers[specialty] = SpecialtyManagerAgent(specialty_manager_jid, PASSWORD, MAX_PATIENTS_PER_SPECIALTY, agent_manager=hospital_manager_agent)

    # passamos o gestor hospitalar como um parametro do agent_manager
    # inicializamos os agentes de gestor de especialidade
    for specialty in specialty_managers:
        res_specialty_manager = specialty_managers[specialty].start(auto_register=True)
        res_specialty_manager.result()

    # conectamos os agentes pacientes e os agentes médicos e inicializamos
    patient_agents_list = []
    doctor_agents_list = []

    for specialty, max_patients in MAX_PATIENTS_PER_SPECIALTY.items():
        specialty_manager_jid = f'{specialty.lower()}_manager@{XMPP_SERVER}'
        for i in range(1, max_patients + 1):
            # dormir 1 segundo a cada 10 pacientes adicionados
            if i % 10 == 0:
                time.sleep(1)

            patient_jid = f'paciente_{specialty.lower()}{i}@{XMPP_SERVER}'
            patient_agent = PatientAgent(patient_jid, PASSWORD)
            patient_agent.set('service_contact', specialty_manager_jid)
            patient_agent.set('especialidade', specialty)
            res_patient_agent = patient_agent.start(auto_register=True)
            res_patient_agent.result()
            patient_agents_list.append(patient_agent)

            doctor_jid = f'doutor_{specialty.lower()}{i}@{XMPP_SERVER}'
            doctor_agent = DoctorAgent(doctor_jid, PASSWORD)
            doctor_agent.set('service_contact', specialty_manager_jid)
            doctor_agent.set('especialidade', specialty)
            res_doctor_agent = doctor_agent.start(auto_register=True)
            res_doctor_agent.result()
            doctor_agents_list.append(doctor_agent)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # parar todos os agentes
        for patient_agent in patient_agents_list:
            patient_agent.stop()

        for doctor_agent in doctor_agents_list:
            doctor_agent.stop()

        hospital_manager_agent.stop()
    
    except any:
                # parar todos os agentes
        quit_spade()

    print('Agentes terminados')

    # Finish all the agents and behaviors running in your process
    quit_spade()

if __name__ == '__main__':
    main()
