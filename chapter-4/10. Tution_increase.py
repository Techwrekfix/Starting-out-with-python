#This program displays a tuition increase

print('Year\tTuition Amount(per semester)')
print('----------------------------------')
tuition_amount = 8000
for years in range(1,6):
    tuition_amount += (0.03)* tuition_amount
    print(years, '\t\t',format(tuition_amount,',.2f'))
    
    
 
