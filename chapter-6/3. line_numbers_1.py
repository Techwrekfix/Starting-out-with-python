def main():
    
    #ask user for file name
    file_name = input('Enter the name of your file: ')

    #open the file
    user_file = open(file_name,'r')
    count = 0

    for line in user_file:
        count += 1
        print(count,':',line.rstrip('\n'),sep='')
    user_file.close()
    
main()
