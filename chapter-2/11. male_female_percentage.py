#This program displays Male and Female percentages

number_of_male = float(input('Enter the number of male ' \
                             'students in the class: '))
number_of_female = float(input('Enter the number of female ' \
                               'students in the class: '))
#calculating the total and percentage
#of male and female in the class
total = number_of_male + number_of_female
percentage_of_male = (number_of_male / total) * 100
percentage_of_female = (number_of_female / total) * 100

#displaying the results
print('The percentage of males in the class = ',format(percentage_of_male,\
                                                      '.2f'),'%', sep='')

print('The percentage of females in the class = ',format(percentage_of_female,\
                                                      '.2f'),'%', sep='')
