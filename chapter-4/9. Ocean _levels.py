#This program display ocean leavel

print('Years\tOcean Level(millimeters)')
print('-----\t-----------------------')
for years in range(1, 26):
    mil_per_year = format(years * 1.6,'.1f')
    print(years,'\t\t',mil_per_year)
