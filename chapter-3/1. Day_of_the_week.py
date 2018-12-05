#This program displays the days of the week
#by just type in the numeric number of the day

#Assigning the days of the week to numbers
Mon = 1
Tue = 2
Wed = 3
Thurs = 4
Fri = 5
Sat = 6
Sun = 7
#Getting the number of the day from user
number_of_day = int(input("Enter the number of the day: "))

#Determining the day
if number_of_day == Mon:
    print("The day is Monday")
elif number_of_day == Tue:
    print("The day is Tuesday")
elif number_of_day == Wed:
    print("The day is Wednesday")
elif number_of_day == Thurs:
    print("The day is Thursday")
elif number_of_day == Fri:
    print("The day is Friday")
elif number_of_day == Sat:
    print("The day is Saturday")
elif number_of_day == Sun:
    print("The day is Sunday")
else:
    print("Error")
