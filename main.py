import time
from spade import quit_spade
from Agents.gestorHospital import gestorHospitalAgent
from Agents.rececionista import RececionistaAgent
from Agents.gestorUnidade import gestorUnidadeAgent
from Agents.medico import medicoAgent
from aux import generate_random_doctor_name,add_doctor
from dados import XMPP_SERVER, PASSWORD

def main():
    
    print("#### HOSPITAL UMINHO ####")
    
    # Indicamos as especialidades existentes e o número máximo de pacientes
    specialties_and_max = {
            "Cardiologia":(5,0),
            "Neurologia":(5,0),
            "Pediatria":(5,0)
        }
    
    speciality_list = list(specialties_and_max.keys())
    
    gestorHospital = gestorHospitalAgent("gestordoHospital@" + XMPP_SERVER, PASSWORD)

     # Inicializamos o agente gestor hospitalar e verificamos se está pronto
    res_gestor = gestorHospital.start(auto_register=True)
    res_gestor.result()

    # Criamos os agentes gestores de cada unidade hospitalar
    for specialty in speciality_list:
        gestor_name = f"Gestor de {specialty}"
        gestor_agent = gestorUnidadeAgent(f"gestor{specialty}@{XMPP_SERVER}", gestor_name, specialty)
        res_gestor_agent = gestor_agent.start(auto_register=True)
        res_gestor_agent.result() 
    
    doctors_avaliable= {
        "Cardiologia":[],
        "Neurologia":[],
        "Pediatria":[]
    }
    
    # Criamos 5 agentes médicos para cada especialidade:
    for speciality in speciality_list:
        for _ in range(5):
            random_doctor_name = generate_random_doctor_name()
            doctor_name =(speciality + random_doctor_name)
            add_doctor(speciality,doctor_name,doctors_avaliable) 
            medico_agent = medicoAgent(f"{doctor_name}@{XMPP_SERVER}", doctor_name, speciality)
            res_medico_agent= medico_agent.start(auto_register=True)
            res_medico_agent.result()
    
    current_number_of_patients = 0
   
    # Criamos a agente rececionista    
    rececionista = RececionistaAgent("rececionista@" + XMPP_SERVER, PASSWORD, specialties_and_max, doctors_avaliable,current_number_of_patients)
    res_rececionista =rececionista.start(auto_register=True)
    res_rececionista.result()
    
    # Wait for some time to let the agents perform their tasks
    time.sleep(10)

    # Stop all agents
    #gestorHospital.stop()
    #rececionista.stop()

    # Quit Spade
    quit_spade()

if __name__ == '__main__':
    main()
