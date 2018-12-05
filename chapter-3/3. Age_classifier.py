#This program classifies users ages

#Getting age number from the user
age = int(input("Enter the person's age: "))

#Assigning the age to infant, a child,
#a teenager, or an adult

if age <= 1:
    print('The person is an infant.')
elif age < 13:
    print('The person is a child.')
elif age < 20:
    print('The person is a teenager.')
else:
    print('The person is an adult.')
