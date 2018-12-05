#This program displays user's name Initials

#ALGORITHM
#ask user to enter first, middle and last name
#a functions accepts the three names and returns
#a slice of the first character of the three names
#concatenate the three slices to generate the initials
#for the all the three names.

#CODE:

def generate_initials(first,middle,last):
    set1 = first[0:1] + '.'
    set2 = middle[0:1] + '.'
    set3 = last[0:1] + '.'

    initials = set1+ set2 +set3
    return initials

def main():
    first = input('Enter your first name: ')
    middle = input('Enter your middle name: ')
    last = input('Enter your last name: ')
    initials = generate_initials(first,middle,last)

    print('Here are the initials of your three names:',initials.upper())

main()
