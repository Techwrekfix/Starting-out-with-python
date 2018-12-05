#This program displays Average rainfall over a period
total_months = 0
total_inches = 0
years = int(input('Enter number of years: '))

for no_of_years in range(1,years+1):
    for months in range(1,13):
        print('Enter the inches of rainfall for month',months,\
               ',year',no_of_years,end='')
        inches = float(input(': '))
        #total inches of rainfall
        total_inches += inches
        #toal month
        total_months += 1

#average rainfall
average_rainfall = (total_inches/total_months)
#display results
print('\nNumber of months = '+format(total_months,'.1f'),\
      'Total inches = '+format(total_inches,'.1f'),\
      'Average rainfall = '+format(average_rainfall,'.1f'),sep='\n')
    
        



