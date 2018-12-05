#This program generate and display seven-digit
#lottery number in the range of 0 through 9

import random

def main():
    lottery = []
    for count in range(7):
        numbers = random.randrange(0,10)
        lottery.append(numbers)

    #display lottery numbers
    for item in lottery:
        print(item)
main()
