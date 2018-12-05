#This program displays a number of test average and grade
def main():
    score1 = int(input('Enter test score 1: '))
    score2 = int(input('Enter test score 2: '))
    score3 = int(input('Enter test score 3: '))
    score4 = int(input('Enter test score 4: '))
    score5 = int(input('Enter test score 5: '))
    average = calculate_average(score1,score2,score3,score4,score5)
    print()
    print('Score\tLetter Grade')
    print(score1,'\t',determine_grade(score1))
    print(score2,'\t',determine_grade(score2))
    print(score3,'\t',determine_grade(score3))
    print(score4,'\t',determine_grade(score4))
    print(score5,'\t',determine_grade(score5))
    print('\nYour average =',average)

def calculate_average(num1,num2,num3,num4,num5):
    average = (num1+num2+num3+num4+num5)/5
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
