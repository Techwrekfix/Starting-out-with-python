#This program displays a date in the form
#(Month day, Year like March 12, 2014

#ALGORITHM in pseudocode

#1. get a date string in the form mm/dd/yyyy from the user
#2. use the split method to remove the seperator('/')
#   and assign the results to a variable.
#3. determine the month the user entered
#   if month is 01:
#      month is Januray
#   if month is 02:
#      month is February
#   if month is 03:
#      month is March
#   if month is 04:
#      month is April
#   this keep going till
#   if month is 12:
#      month is December
#3. using indexes, print the date in the variable

#CODE

def main():
    date_string = input('Enter a date in the form "mm/dd/yyyy": ')
    date_list = get_date_list(date_string)
    
def get_date_list(date_string):
    date_list = date_string.split('/')
    #Determining the month
    mm = date_list[0]
    if mm == '01':
        mm = 'January'
    elif mm == '02':
        mm = 'February'
    elif mm == '03':
        mm = 'March'
    elif mm == '04':
        mm = 'April'
    elif mm == '05':
        mm = 'May'
    elif mm == '06':
        mm = 'June'
    elif mm == '07':
        mm = 'July'
    elif mm == '08':
        mm = 'August'
    elif mm == '09':
        mm = 'September'
    elif mm == '10':
        mm = 'October'
    elif mm == '11':
        mm = 'November'
    elif mm == '12':
        mm = 'December'
    #displayin results
    print('A reform of the date you entered is: ',\
          mm,date_list[1]+',',date_list[2])

main()   
