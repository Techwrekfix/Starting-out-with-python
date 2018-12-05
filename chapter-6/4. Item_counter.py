#This program is an item counter

def main():
    #open the file
    user_file = open('filename.txt', 'r')

    count = 0 #This counts the number of items in the file

    for line in user_file:
        count += 1

    user_file.close()
    print('The total number of items in the file =',count)
main()
    
