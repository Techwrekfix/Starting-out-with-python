#This program imports the Car class
#and creates an instance of it

import car_class

def main():
    #Asking user for the car model_year and make
    model = input('Enter the model year of the car: ')
    make = input('Enter the make of the car: ')
    speed = 0
    #Creating a Car object
    car = car_class.Car(make,model,speed)
    print()

    #Displaying current speed before calling
    #the accelerate method
    print('Current speed is:',car.get_speed()) 

    #Callin the accelerate method five times
    print('Displaying current speed for each of the five '
          'calls to the accelerate method.')
    for count in range(1,6):
        car.accelerate()
        print('Current Speed',count,':',car.get_speed())
    print()

    #Displaying current speed before calling
    #the brake method
    print('Current speed is:',car.get_speed())
    print('Displaying current speed for each of the five '
          'calls to the brake method.')
    for count in range(1,6):
        car.brake()
        print('Curretn Speed',count,':',car.get_speed())

main()

