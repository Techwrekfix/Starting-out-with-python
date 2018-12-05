#This program calculates Body Mass Index(BMI)

#Asking user to enter height and weight
weight = float(input('Please enter your weight in pounds: '))
height = float(input('Plesae enter your height in inches: '))

#Calculating BMI
BMI = (weight * 703)/(height**2)
#Displaying BMI
print('\nPlease your Body Mass Index =',format(BMI,'.1f'))

#Determining the BMI
if BMI < 18.5:
    print('Please you are underweight because your BMI of',\
          format(BMI,'.1f'),' is less than 18.5')
elif BMI < 26.0:
    print('Please you have optimal weight because your BMI of',\
          format(BMI,'.1f'),' is between 18.5 and 25')
else:
    print('Please you are overweight because your BMI of',\
          format(BMI,'.1f'), ' is more than 25')
