#This program displays the factorial of a number

number = int(input('Enter a nonnegative integer: '))
factorial = 1
for numbers in range(1,number+1):
    factorial *= numbers
print('The factorial of',number,'is:',factorial)

