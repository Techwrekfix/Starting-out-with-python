#This program uses dictionary to process world series winners

#NOTE: Getting the original source file will make this code efficient

#Global Constants
STARTIING_YEAR = 1903
ENDING_YEAR = 2009

def main():
    #Open the file for reading(Make is the correct file name)
    infile = open('WorldSeriesWinners.txt','r')

    #Creatig dictionaries
    dictionary_1, dictionary_2 = two_dicts(infile)

    #close the file
    infile.close()

    #Ask user for a year and display results
    user_choice(dictionary_1, dictionary_2)

def two_dicts(file):
    #create a dictionary
    world_series = {}

    #read the first line in the file
    line = file.readline()
    
    for items in range(STARTIING_YEAR,ENDING_YEAR + 1):
        line = line.strip('\n')
        world_series[items] = line
        
        #read the next line in the file
        line = file.readline()

    #creating the second dictionary
    overall_wins = {}
    count = 1   #To count the number of times a team
                #has won the world series
    for items in range(STARTIING_YEAR,ENDING_YEAR + 1):
        team_name = world_series[items]
        if team_name not in overall_wins:
            overall_wins[team_name] = count
        else:
            overall_wins[team_name] += 1

    return world_series, overall_wins

def user_choice(dict_1,dict_2):
    #ask user for a year
    user_year = int(input('Enter a year between 1903 through 2009: '))
    #validate user_year
    while user_year < 1903 or user_year > 2009:
        user_year = int(input('please enter a correct year: '))
    print()

    #Determine user answer
    if user_year >1902 and user_year < 2010 and \
                   user_year != 1904 and user_year != 1994:
        print(dict_1[user_year],'won in',user_year,'and has won'
              ' the world series',dict_2[dict_1[user_year]],'time(s).')
    
    elif user_year == 1904:
        print('World Series was not played in 1904.')
    elif user_year == 1994:
        print('World Seiries was not played in 1994.')

main()

        

        
