#This program displays the roman numeral version
#of a number entered by a user

#Assigning the numeric numbers to a variable
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10

#Prompting the user to enter a numeric number
number = int(input("Enter a numeric number: "))

#Displaying the roman numeral version of the
#numeric number entered
if number == one:
    print("I")
elif number == two:
    print("II")
elif number == three:
    print("III")
elif number == four:
    print("IV")
elif number == five:
    print("V")
elif number == six:
    print("VI")
elif number == seven:
    print("VII")
elif number == eight:
    print("VII")
elif number == nine:
    print("IX")
elif number == ten:
    print("X")
else:
    print("ERROR")
