#This program is a time calculator

#Asking user to enter number of seconds
user_seconds = int(input('Please enter the number of seconds: '))

#Calculating days, hours, minutes and seconds
days = user_seconds // 86400
hours = (user_seconds % 86400) // 3600
minutes = ((user_seconds % 86400) % 3600) // 60
seconds = ((user_seconds % 86400) % 3600) % 60

#Displaying the results
print('\nThere are ',days,'day(s), ',hours,'hour(s), ',minutes,\
      'minute(s) and ',seconds,'second(s) in ',user_seconds,'seconds',sep='')
