import time
from spade import quit_spade
from Agents.gestorHospital import gestorHospitalAgent
from Agents.medico import medicoAgent
from Agents.paciente import pacienteAgent
from aux import generate_random_doctor_name,add_doctor,generate_patient_number,triagem,select_hospital,generate_level,generate_rating
from dados import XMPP_SERVER, PASSWORD
from termcolor import colored

class Hospital:
    def run_hospital(self):
        nome_gestor_uminho = "gestorHospitalUminho@"
        nome_gestor_porto = "gestorHospitalPorto@"
        gestores =[nome_gestor_uminho, nome_gestor_porto]
        
        #HOSPITAL DO MINHO
    
        print(colored("#### HOSPITAL UMINHO ####",'yellow'))
        
        # Indicamos as especialidades existentes e o número máximo de pacientes
        specialties_and_max_minho = {
                "cardiologia":(5,0),
                "neurologia":(5,0),
                "pediatria":(5,0)
            }
        
        speciality_list_minho = list(specialties_and_max_minho.keys())
        
        doctors_avaliable_minho= {
            "cardiologia":[],
            "neurologia":[],
            "pediatria":[]
        }
        
        medicos_agents_list = []
        # Criamos 5 agentes médicos para cada especialidade:
        for speciality in speciality_list_minho:
            for _ in range(5):
                random_doctor_name = generate_random_doctor_name()
                doctor_name =(speciality + random_doctor_name)
                doctor_name_and_scores = (doctor_name, generate_rating(),generate_level())
                add_doctor(speciality,doctor_name_and_scores,doctors_avaliable_minho) 
                medico_jid = f"{doctor_name}@"+XMPP_SERVER
                medico_agent = medicoAgent(medico_jid, PASSWORD, doctor_name, speciality)
                res_medico_agent= medico_agent.start(auto_register=True)
                res_medico_agent.result()
                medicos_agents_list.append(medico_agent)
        
        # Criamos o agente gestor do Hospital - com toda a informação necessária 
        gestor_minho_jid = nome_gestor_uminho+XMPP_SERVER
        hospital_name_m="UMINHO"
        gestorHospitalMinho = gestorHospitalAgent(gestor_minho_jid, PASSWORD, specialties_and_max_minho, doctors_avaliable_minho,nome_gestor_porto,hospital_name_m)
        res_gestorHospital_m =gestorHospitalMinho.start(auto_register=True)
        res_gestorHospital_m.result()
        
        #HOSPITAL DO PORTO
        
        print(colored("#### HOSPITAL UPORTO ####",'yellow'))
        
        # Indicamos as especialidades existentes e o número máximo de pacientes
        specialties_and_max_porto = {
                "dermatologia":(5,0),
                "psiquiatria":(5,0),
                "hematologia":(5,0)
            }
        
        speciality_list_porto = list(specialties_and_max_porto.keys())
        
        doctors_avaliable_porto= {
            "dermatologia":[],
            "psiquiatria":[],
            "hematologia":[]
        }
        
        medicos_agents_list = []
        # Criamos 5 agentes médicos para cada especialidade:
        for speciality in speciality_list_porto:
            for _ in range(5):
                random_doctor_name = generate_random_doctor_name()
                doctor_name =(speciality + random_doctor_name)
                doctor_name_and_scores = (doctor_name, generate_rating(),generate_level())
                add_doctor(speciality,doctor_name_and_scores,doctors_avaliable_porto) 
                medico_jid = f"{doctor_name}@"+XMPP_SERVER
                medico_agent = medicoAgent(medico_jid, PASSWORD, doctor_name, speciality)
                res_medico_agent= medico_agent.start(auto_register=True)
                res_medico_agent.result()
                medicos_agents_list.append(medico_agent)
        
        # Criamos o agente gestor do Hospital - com toda a informação necessária   
        gestor_porto_jid = nome_gestor_porto+XMPP_SERVER
        hospital_name_p="UPORTO"
        gestorHospitalporto = gestorHospitalAgent(gestor_porto_jid, PASSWORD, specialties_and_max_porto, doctors_avaliable_porto,nome_gestor_uminho,hospital_name_p)
        res_gestorHospital_p =gestorHospitalporto.start(auto_register=True)
        res_gestorHospital_p.result()
        
        # Esperamos que estes os agentes anteriores terminem
        time.sleep(10)
        
        specialities_norte = ["cardiologia","neurologia","pediatria","dermatologia","psiquiatria","hematologia"]
        
        # Criamos os agentes pacientes
        pacientes_agents_list=[]
        for i in range(15):
            #time.sleep(1)
            paciente_name = generate_patient_number()
            paciente_jid = f"{paciente_name}@"+XMPP_SERVER
            pacient_triagem = triagem(specialities_norte)
            hospital_assigned = select_hospital(gestores)
            paciente_agent = pacienteAgent(paciente_jid, PASSWORD, hospital_assigned,paciente_name, pacient_triagem)
            paciente_agent.set("status","não_atendido")
            res_paciente_agent= paciente_agent.start(auto_register=True)
            pacientes_agents_list.append(paciente_agent)
        
            
        # Handle interruption of all agents
        while (gestorHospitalMinho.is_alive() and gestorHospitalporto.is_alive):
            try:
             time.sleep(1)
            except KeyboardInterrupt:
                # stop de todos os agentes médicos 
                for medicos in medicos_agents_list:
                    medicos.stop()
                # stop de todos os agentes pacientes
                for pacientes in pacientes_agents_list:
                    pacientes.stop()
                # stop o gestor do hospital
                break
        print(colored("Os agentes foram terminados",'yellow'))
        print(colored("#### O Hospital encontra-se fechado ####",'yellow'))
        print(colored("####   ####",'yellow'))

        # finish all the agents and behaviors running in your process
        quit_spade()

if __name__ == '__main__':
    hospital= Hospital()
    hospital.run_hospital()
