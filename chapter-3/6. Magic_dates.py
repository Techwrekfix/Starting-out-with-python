#This program displays a very unique magic date

#Getting user date details and assigning them
#a variable
month = int(input("Enter a month in numeric form: "))
day = int(input("Enter a day in numeric form: "))
year = int(input("Enter a two digit year: "))
print()

#creating the magic date
if month * day == year:
    print("The date ",month,"/",day,"/",year," is magic.",sep='')
else:
    print("The date ",month,"/",day,"/",year," is not magic.",sep='')
