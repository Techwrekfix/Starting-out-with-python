#This program reads random numbers from a file

def main():
    #opening the file
    user_file = open('random_numbers.txt', 'r')

    total = 0.0 #This will accumulates the total of
                #random numbers in the file
    count = 0 #This will count the number of
                #random numbers in the file

    #using a loop to read numbers from the file
    print('Here are the random numbers')
    for line in user_file:
        count += 1
        line = int(line)
        total += line
        print(line)
        
    #closing the file
    user_file.close()
    print('\nThe total of the random numbers =',format(total,'.1f'))
    print('The number of random numbers =',count)
main()
        
