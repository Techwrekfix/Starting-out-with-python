#This program grades the written portion of the
#driver's license exam.

def main():
    correct_answers = ['A','C','A','A','D','B','C','A','C','B','A','D','C',\
                       'A','D','C','B','B','D','A']

    student_answers = get_student_answers()
    compare_answers = get_compare_answers(correct_answers,student_answers)

def get_student_answers():
    infile = open('student_answers.txt','r')

    student_answers = infile.readlines()

    infile.close()

    index = 0
    while index < len(student_answers):
        student_answers[index] = student_answers[index].rstrip('\n')
        index += 1
    return student_answers

def get_compare_answers(correct_answers,student_answers):
    count = 0   #for counting number of correct and wrong answers
    print('Correct answers =',correct_answers)
    print('\nStudent_answers =',student_answers)
    wrong_answers = []

    for index in range(20):
        if correct_answers[index] == student_answers[index]:
            count += 1
        else:
            wrong_answers.append(index)
            count += 0

    if count < 15:
        print('\nYou failed, you must score at least 15')
    else:
        print('\nCongratulations, You passed')

    print('The total number of correctly answered questions is:',count)
    print('The total number of incorrectly answered questions is:',20 - count)
    print(wrong_answers,'is the question numbers of the'\
          ' incorrect answers')

main()    

        
