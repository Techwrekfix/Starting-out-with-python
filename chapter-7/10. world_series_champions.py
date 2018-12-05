#This program lets user enters a name of a team and displays
#how many times the team has won the world series

def main():
    winners_list = get_winners_list()
    team_name = get_team_name()
    search_winner = start_searching(winners_list,team_name)

def get_winners_list():
    winners_list = []

    infile = open('world_series_champions.txt','r')

    for index in infile:
        index = index.rstrip('\n')
        winners_list.append(index)
    return winners_list

def get_team_name():
    team_name = input('Enter the name of the team you want to search: ')
    return team_name

def start_searching(winners_list,team_name):
    search_list = []
    count = 0
    for search in winners_list:
        if search == team_name:
            count += 1
            search_list.append(search)
    print()
    if count >= 1:
        print(team_name,'has won the world series',count,\
              'time(s) in the period of 1903 through 2009')
    else:
        print(team_name,'has never won the world series'\
              ' in the period of 1903 through 2009')

main()
