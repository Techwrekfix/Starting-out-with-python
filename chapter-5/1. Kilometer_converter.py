#This program converts distance from Kilometers to miiles

multiplier = 0.6214     #creating a variable multiplier

def main():
    intro()
    kilometer = float(input('\nEnter a distance in Kilometer(s): '))
    miles = get_miles(kilometer)
    
    #Displaying the distance in miles
    print('The converted distance is',format(miles,'.1f'),'miles')


#Defining the intro function
def intro():
    print('This program converts in kilometers to miles')

#Defining the get miles function
def get_miles(kilometer):
    Miles = kilometer * multiplier
    return Miles
main()
