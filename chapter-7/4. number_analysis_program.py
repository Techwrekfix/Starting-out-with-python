#Number analysis program

NUMBER_SERIES = 20

def main():
    #here is the mathematical algorithm/code
    numbers = get_numbers()
    total = calculate_total(numbers)
    average = total / len(numbers)
    highest_number = max(numbers)
    lowest_number = min(numbers)
    print()
    print_details(numbers,total,average,highest_number,lowest_number)

def get_numbers():
    number_list = [0] * NUMBER_SERIES

    print('Enter a series of numbers.')
    print()
    for index in range(len(number_list)):
        number_list[index] = float(input('Enter a number: '))
    return number_list

def calculate_total(numbers):
    total = 0  #intiating accumulator

    for values in numbers:
        total += values
    return total

def print_details(numbers,total,average,highest_number,lowest_number):
    print(numbers,'\nThe total =',total,'\nThe average =',average,\
          '\nThe highest number =',highest_number,'\nThe lowest number'\
          ' =',lowest_number)
main()
    
    
