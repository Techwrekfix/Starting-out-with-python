#This a Car class module

class Car:
    #Initiliazing data attributes
    def __init__(self,model_year,make,speed):
        self.__model_year = model_year
        self.__make = make
        self.__speed = 0

    def set_mode_year(self,model_year):
        self.__model_year = model_year

    def set_make(self,make):
        self.__make = make

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
    
