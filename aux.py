import random

def generate_random_doctor_name():
    return str(random.randint(100, 999))

def add_doctor(specialty, doctor_name, doctors_available):
    for key in doctors_available:
        if specialty == key:
            doctors_available[key].append(doctor_name)
            break
        
def generate_rating():
    return str(random.randint(1, 5))

def generate_patient_number():
    return str(random.randint(1000, 9999))

def triagem(specialities_available):
    return random.choice(specialities_available)

def select_hospital(hospitais):
    return random.choice(hospitais)

def generate_level():
    levels=["principiante", "avançado"]
    return random.choice(levels)
    
level_weights = {
    "principiante": 1,
    "avançado": 3
}

def calculate_weights(doctor1, doctor2):
    weight1 = int(doctor1[1]) * level_weights[str(doctor1[2])]
    weight2 = int(doctor2[1]) * level_weights[str(doctor2[2])]

    total_weight = weight1 + weight2
    prob1 = weight1 / total_weight
    prob2 = weight2 / total_weight
    
    return prob1, prob2

def choose_doctor(doctor1, doctor2):
    prob1, prob2 = calculate_weights(doctor1, doctor2)
    doctors = [doctor1, doctor2]
    choice = random.choices(doctors, weights=[prob1, prob2], k=1)[0]
    return choice[0]

