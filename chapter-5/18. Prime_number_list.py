#This program displays all the prime numbers from 1 to 100

#The is_prime function defines numbers that are prime
def is_prime(integer):
    prime_division = 0
    if integer <= 1:
        return False
    for current_integer in range(1,integer + 1):
        if integer % current_integer == 0:
            prime_division += 1
            if prime_division > 2:
                return False
    else:
         return True

def main():
    for numbers in range(1,101):
        if is_prime(numbers):
            print(numbers,end=' ') 
main()
