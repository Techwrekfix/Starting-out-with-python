#This program reads a series of integers and calculates the sum

def main():
    user_file = open('numbers.txt', 'r')
    total = 0.0 #setting accumulator to accumulate the total
    
    print('Here are the integers')
    for line in user_file:
        line = int(line)
        total += line
        print(line)
        
    user_file.close()
    print('And their total =',format(total,'.2f'))
main()
        

