#This program is Quiz about US states
#and their capitals

def main():
    dictionary = create_dictionary()
    determine_user_answer(dictionary)

def create_dictionary():
    us_states = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
                 'Arkansas':'Little Rock','Carlifornia':'Sacramento',
                 'Colorado':'Denver','Connecticut':'Hartford','Delware':
                 'Dover','Florida':'Tallahassee','Georgia':'Alanta','Hawaii':
                 'Honolulu','Idaho':'BOise','Illinois':'Springfield','Indiana':
                 'Indianapolis','Iowa':'Des Moines','Kansas':'TOpeka',
                 'Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':
                 'Augusta','Maryland':'Annapolis','Massachusetts':'Boston',
                 'Michigan':'Lansing','Minnesota':'St. Paul','Mississipi':
                 'Jackson','Missouri':'Jefferson City','New York':'Albany',
                 'North Carolina':'Raleigh','North Dakota':'Bismarck','Ohio':
                 'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem',
                 'Pennsylvania':'Harrisburg','Rhode Island':'Providence',
                 'South Carolina':'Columbia','South Dakota':'Pierre',
                 'Tennessee':'Nashville','Texas':'Austin','Utah':
                 'Salt Lake City','Vermont':'Montpelier','Virginia':'Richmond',
                 'Washington':'Olympia','West Virginia':'Charleston',
                 'Wisconsin':'Madison','Wyoming':'Cheyenne'}
    return us_states

def determine_user_answer(us_states_and_capitals):
    correct_answers = 0   #counts the number of correct answers
    incorrect_answers = 0 #counts the number of wrong answers
    
    #Asking user for the number of questions
    number_of_questions = int(input('Enter your preferred '
                                    'number of questions: '))
    #Making sure user entry is within range of
    #us_states_and_capitals which is 50
    if number_of_questions > len(us_states_and_capitals):
        number_of_questons = len(us_states_and_capitals)
    print()

    #Initalizing a loop to ask the questions
    for items in range(number_of_questions):
        key,value = us_states_and_capitals.popitem()
        print('Enter the capital of',key,end='')
        capital = input(': ')
        if capital == value:
            correct_answers += 1
        else:
            incorrect_answers += 1
    print()
    print('You answered',correct_answers,'questions correct')
    print('You had',incorrect_answers,'questions wrong')

main()
        
        
    
