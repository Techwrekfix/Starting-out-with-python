#This program displays book club points

#Asking user to enter detail
number_of_books_purchased = int(input('Enter the number of books'\
                                      'purchased: '))
print()
#Determining the points
if number_of_books_purchased < 2:
    print('You have 0 points')
elif number_of_books_purchased < 4:
    print('You have 5 points')
elif number_of_books_purchased < 6:
    print('You have 15 points')
elif number_of_books_purchased < 8:
    print('You have 30 points')
else:
    print('You have 60 points')
