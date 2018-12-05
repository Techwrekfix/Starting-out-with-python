#This program calcualtes Kinetic Energy

def main():
    object_mass = float(input('Enter the mass of the object in kilograms: '))
    object_velocity = float(input('Enter the velocity of the object'\
                                  ' in meters per second: '))
    energy = kinetic_energy(object_mass,object_velocity)
    print('\nThe Kinetic Energy of the object =',energy,'m/s')

def kinetic_energy(mass,velocity):
    KE = (mass * velocity**2)/2
    return KE
main()
