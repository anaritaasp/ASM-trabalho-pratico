import time
from spade import quit_spade
from Agents.gestorHospital import gestorHospitalAgent
from Agents.gestorUnidade import gestorUnidadeAgent
from Agents.medico import medicoAgent
from Agents.paciente import pacienteAgent
from aux import generate_random_doctor_name,add_doctor,generate_patient_number,triagem
from dados import XMPP_SERVER, PASSWORD
from termcolor import colored

class Hospital:
    def run_hospital(self):
        
        
        print(colored("#### HOSPITAL UMINHO ####",'green'))
        
        # Indicamos as especialidades existentes e o número máximo de pacientes
        specialties_and_max = {
                "Cardiologia":(5,0),
                "Neurologia":(5,0),
                "Pediatria":(5,0)
            }
        
        speciality_list = list(specialties_and_max.keys())

        gestores_agents_list = []
        # Criamos os agentes gestores de cada unidade hospitalar
        for specialty in speciality_list:
            gestor_name = f"Gestor de {specialty}"
            gestor_jid = f"g{specialty}@"+XMPP_SERVER
            gestor_agent = gestorUnidadeAgent(gestor_jid, PASSWORD,specialty)
            res_gestor_agent = gestor_agent.start(auto_register=True)
            res_gestor_agent.result() 
            gestores_agents_list.append(gestor_agent)
        
        doctors_avaliable= {
            "Cardiologia":[],
            "Neurologia":[],
            "Pediatria":[]
        }
        
        medicos_agents_list = []
        # Criamos 5 agentes médicos para cada especialidade:
        for speciality in speciality_list:
            for _ in range(1):
                random_doctor_name = generate_random_doctor_name()
                doctor_name =(speciality + random_doctor_name)
                add_doctor(speciality,doctor_name,doctors_avaliable) 
                medico_jid = f"{doctor_name}@"+XMPP_SERVER
                medico_agent = medicoAgent(medico_jid, PASSWORD, doctor_name, speciality)
                res_medico_agent= medico_agent.start(auto_register=True)
                res_medico_agent.result()
                medicos_agents_list.append(medico_agent)
        
        print(doctors_avaliable) 
        # Criamos o agente gestor do Hospital    
        gestorHospital = gestorHospitalAgent("gestHospital@" + XMPP_SERVER, PASSWORD, specialties_and_max, doctors_avaliable)
        res_gestorHospital =gestorHospital.start(auto_register=True)
        res_gestorHospital.result()
        
        
        # Esperamos que estes os agentes anteriores terminem
        time.sleep(10)
        
        # Criamos os agentes pacientes
        pacientes_agents_list=[]
        for i in range(1):
            time.sleep(1)
            paciente_name = generate_patient_number()
            paciente_jid = f"{paciente_name}@"+XMPP_SERVER
            pacient_triagem = triagem(speciality_list)
            paciente_agent = pacienteAgent(paciente_jid, PASSWORD, paciente_name, pacient_triagem)
            paciente_agent.set("status","não_atendido")
            res_paciente_agent= paciente_agent.start(auto_register=True)
            res_paciente_agent.result()
            pacientes_agents_list.append(paciente_agent)
            
        # Handle interruption of all agents
        while gestorHospital.is_alive():
            try:
             time.sleep(1)
            except KeyboardInterrupt:
                # stop de todos os agentes gestores
                for gestores in gestores_agents_list:
                    gestores.stop()
                # stop de todos os agentes médicos 
                for medicos in medicos_agents_list:
                    medicos.stop()
                # stop de todos os agentes pacientes
                for pacientes in pacientes_agents_list:
                    pacientes.stop()

                # stop o gestor do hospital
                break
        print('Agents finished')

        # finish all the agents and behaviors running in your process
        quit_spade()

if __name__ == '__main__':
    hospital= Hospital()
    hospital.run_hospital()
