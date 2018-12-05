#This program is about a rainfall statistics

MONTHS = 12     #Number of months to record rainfall

def main():
    #haha, the main funtion represents my algorithm
    rainfall = get_rainfall_data()
    total_rainfall = calcualte_annual_total_rainfall(rainfall)
    average_monthly_rainfall = total_rainfall / len(rainfall)
    highest_monthly_rainfall = max(rainfall)
    lowest_monthly_rainfall = min(rainfall)
    print()
    print_details(total_rainfall,average_monthly_rainfall,\
                  highest_monthly_rainfall,lowest_monthly_rainfall)

def get_rainfall_data():
    #creating a list to hold rainfall data
    rainfall_list = [0] * MONTHS

    #adding data to rainfall list
    for index in range(len(rainfall_list)):
        print('Enter rainfall data for month',index+1,end='')
        rainfall_list[index] = float(input(': '))
    return rainfall_list

def calcualte_annual_total_rainfall(rainfall):
    total = 0 #iniating accumulator

    for values in rainfall:
        total += values
    return total

def print_details(total_rainfall,average_monthly_rainfall,\
                  highest_monthly_rainfall,lowest_monthly_rainfall):
    print('Total rainfall for the year is:',total_rainfall,'\nThe'\
          ' average monthly rainfall is:',average_monthly_rainfall,\
          '\nThe month with highest rainfall is:', highest_monthly_rainfall,\
          '\nThe month with lowest rainfall is:',lowest_monthly_rainfall)
main()
    
    
    
