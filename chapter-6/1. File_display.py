#This program displays all the numbers on a supposed
#existing file named 'numbers.txt'.

def main():
    #open the file
    number_file = open('numbers.txt','r')

    #read the first line in the file
    line = number_file.readline()

    #determing wether first line is not an empty string
    while line != '':
        print(line.rstrip('\n'))

        #read the next line
        line = number_file.readline()
    #close the file
    number_file.close()
main()
