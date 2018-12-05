#This program represents an ingredient adjuster

#creating variables
cups_of_sugar = 1.5
cups_of_butter = 1.0
cups_of_flour = 2.75
fixed_number_of_cookies = 48

#asking the user to enter prefered number of cookies
number_of_cookies = float(input('Enter the preferred number of cookies: '))

#calculating expected number of ingredients
expected_cups_of_sugar = (number_of_cookies / fixed_number_of_cookies) \
                         *cups_of_sugar
expected_cups_of_butter =(number_of_cookies / fixed_number_of_cookies) \
                         *cups_of_butter
expected_cups_of_flour =(number_of_cookies / fixed_number_of_cookies) \
                         *cups_of_flour
#displaying results
print('For every',number_of_cookies,'cookies, you will need the '\
      'following amount of ingredients')
print('Sugar = ',format(expected_cups_of_sugar,'.2f'),' cups, Butter = '\
              ,format(expected_cups_of_butter,'.2f'),' cups, Flour = '\
              ,format(expected_cups_of_flour,'.2f'),' cups',sep='')
