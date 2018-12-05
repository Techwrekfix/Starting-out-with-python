def main():
    
    #ask user for file name
    file_name = input('Enter the name of your file: ')

    #open the file
    user_file = open(file_name,'r')

    #read the first line in the file
    line = user_file.readline()
    line_numbers = 0

    #using a while loop to read the lines in the file
    while line != '':
        line_numbers += 1
        print(line_numbers,':',line.rstrip('\n'),sep='')
        line = user_file.readline()
        
    user_file.close()

main()
