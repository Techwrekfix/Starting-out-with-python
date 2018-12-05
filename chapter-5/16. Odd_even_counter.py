#This program keeps a count of odd numbers and even numbers
import random

def main():
    even = 0
    odd = 0
    for numbers in range(1, 101):
        random_number = generate_random_number()
        print(random_number)
        if is_even_odd(random_number):
            even += 1
        else:
            odd += 1
    print('Even numbers =',even,'\nOdd numbers =',odd)
    
def generate_random_number():
    random_number =  random.randint(1,100)
    return random_number

def is_even_odd(random_number):
   
    if random_number % 2 == 0:
      return True
    
    else:
        return False
    
main()
 
