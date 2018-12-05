#This program reads a series of integers and calculates the sum

def main():
    try:
        user_file = open('numbers.txt', 'r')
        total = 0.0 #setting accumulator to accumulate the total
        count = 0.0 #This counts the number of integers in the file
        print('Here are the integers in the file')
        for line in user_file:
            line = int(line)
            count += 1
            total += line
            print(line)
        average = total / count  
        user_file.close()
    except IOError as err:
        print('\nOpen function error: ',err)
    except ValueError as err:
        print('\n',err)
    except Exception as err:
        print('\n',err)
    else:
        print('The average of the integers =',format(average,'.2f'))
main()
        

