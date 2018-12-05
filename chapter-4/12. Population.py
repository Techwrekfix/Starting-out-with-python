#This program predicts the approximate size of
#a population of organisms

starting_number = float(input('Enter the starting number of Organisms: '))
population_increase = float(input('Enter in percentage the average '\
                                  'daily population increase: '))
number_of_days = int(input('Enter the number of days the Orgainms '\
                           'will multiply: '))
percentage_value = population_increase / 100

print('Day Aproximation\tPopulation')
print('----------------\t----------')
for number in range(1,number_of_days+1):
    print(number,'\t\t\t',starting_number)
    starting_number += (starting_number * percentage_value)   

