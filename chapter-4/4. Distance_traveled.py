#This program displays distance travelled in miles

speed = int(input('Enter the speed of the vehicle in mph: '))
time = int(input('Enter the hours traveled by the vehicle: '))

#Creating a table
print('Hour \t Distance Traveled')
print('--------------------------')
#Using a loop to display the table
for hours in range(time):
    distance = speed *(hours+1) 
    print(hours+1,'\t',distance)


