import random

def generate_random_doctor_name():
    return str(random.randint(1000, 9999))

def add_doctor(specialty, doctor_name, doctors_available):
    for key in doctors_available:
        if specialty == key:
            doctors_available[key].append(doctor_name)
            break