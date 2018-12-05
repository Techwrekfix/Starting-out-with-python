#This program converts feets to inches

def calculate_feet_to_inches(feet):
    inches = feet * 12
    return inches

def main():
    number_of_feet = float(input('Enter the number of feet: '))
    feet_to_inches = calculate_feet_to_inches(number_of_feet)

    #displaying the results
    print(number_of_feet,'feet =',feet_to_inches,'inches')

main()
