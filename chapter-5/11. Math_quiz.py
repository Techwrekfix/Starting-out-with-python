#This program displays a simple math quiz
import random

def main():
    number1 = random.randint(1,350)
    number2 = random.randint(1,350)
    correct_answer = calculate_correct_answer(number1,number2)
    print('\t',number1,'\n+\t',number2)
    question = int(input('Enter the answer : '))
    check_answer(question,correct_answer)

def calculate_correct_answer(num1,num2):
    correct_answer = num1 + num2
    return correct_answer

def check_answer(question,correct_answer):
    if question == correct_answer:
        print('\nCongratulations!',correct_answer,'is correct')
    else:
        print('\nWrong! the correct answwer =',correct_answer)
main()
