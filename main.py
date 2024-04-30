import time
from spade import quit_spade
from Agents.gestorHospital import gestorHospitalAgent
from Agents.rececionista import RececionistaAgent
from dados import XMPP_SERVER, PASSWORD

def main():
   
    gestorHospital = gestorHospitalAgent("gestorHospitalar@" + XMPP_SERVER, PASSWORD)
    rececionista = RececionistaAgent("rececionista@" + XMPP_SERVER, PASSWORD)
 # Start all agents
    gestorHospital.start()
    rececionista.start()

    # Wait for some time to let the agents perform their tasks
    time.sleep(10)

    # Stop all agents
    gestorHospital.stop()
    rececionista.stop()



    # Quit Spade
    quit_spade()

if __name__ == '__main__':
    main()
