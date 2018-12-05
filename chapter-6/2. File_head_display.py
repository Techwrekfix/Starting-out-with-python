#File head display program

def main():
    #creating variables for max lines and number of line in the file
    max_line = 5
    count_lines = 0
    #ask user for file name
    file_name = input('Enter the name of your file: ')

    #open the file
    user_file = open(file_name,'r')

    #read the first line in the file
    line = user_file.readline()
    count_lines += 1
    #using a while loop to read the lines in the file
    while line != '' and count_lines <= max_line:
        count_lines += 1
        print(line.rstrip('\n'))
        line = user_file.readline()
        
    user_file.close()

main()
    
