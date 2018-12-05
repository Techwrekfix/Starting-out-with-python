#This program displays a number of test average and grade
def main():
    base_number = 5
    total = 0.0
    for number in range(base_number):
        print('\nEnter test score',number+1,end='')
        score = int(input(' : '))
        total += score
        grade = determine_grade(score)
        print('Score Grade:',grade)
    average = calculate_average(total,base_number)   
    print('\nYour average =',average)

def calculate_average(total,base_number):
    average = (total)/base_number
    return average
    
def determine_grade(score):
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    elif score < 101:
        return 'A'
    
main()
