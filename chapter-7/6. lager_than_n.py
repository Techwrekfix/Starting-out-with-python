#This program compares a list and a number, n

def compare(number_list, n):
    for values in number_list:
        if values > n:
            print(values)
compare(number_list, n)
