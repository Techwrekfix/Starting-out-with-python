#This program displays calories burned

cal_per_minute = 4.2
for minutes in range(10,31,5):
    calories_burned = cal_per_minute * minutes
    print('Number of Calories burned after',minutes, \
      'minutes =',calories_burned)
