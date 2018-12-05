#This program returns the maximum of two integers

def main():
    num1= int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))
    max = determine_max(num1,num2)
    print('The maximum integer is',max)
    

def determine_max(integer1,integer2):
    if integer1 > integer2:
        return integer1
    else:
        return integer2
main()
