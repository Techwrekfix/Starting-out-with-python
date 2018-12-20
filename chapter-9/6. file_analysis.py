#This program performs analysis on two files

def main():
    #ask the user for the two files
    user_file_1 = input('Enter a text file 1 with its extension'
                      ' (example: file.txt): ')
    user_file_2 = input('Enter a text file 2 with its extension'
                      ' (example: file.txt): ')
    print()

    #Open the files for reading
    infile_1 = open(user_file_1,'r')
    infile_2 = open(user_file_2,'r')

    #create file analysis
    file_analysis(infile_1,infile_2)

    #Close the files
    infile_1.close()
    infile_2.close()

def file_analysis(file_1,file_2):
    #Reading contents of both files into sets
    set_1 = set()
    for item in file_1:
        item = item.strip('\n')
        set_1.add(item)
    
    set_2 = set()
    for item in file_2:
        item = item.strip('\n')
        set_2.add(item)

    #Display the contents of the two files
        
    #file 1
    print('Here are the contents of file 1:')
    for items in set_1:
        print(items)
    print()

    #file 2
    print('Here are the contents of file 2:')
    for items in set_2:
        print(items)

    #Displaying unigue words contained in both files
    print()
    print('The following are unique words in both files:')
    for words in set_1.intersection(set_2):
        print(words)

    #Displaying words contained in both files
    print()
    print('The following words appear in either file 1 or file 2:')
    for words in set_1.union(set_2):
        print(words)

    #Displaying words only in file_1 and not file_2
    print()
    print('The following words appear in file 1, but not in file 2:')
    for words in set_1.difference(set_2):
        print(words)

    #Displaying words only in file_2 and not in flie_1
    print()
    print('The following words appear in file 2, but not in file 1:')
    for words in set_2.difference(set_1):
        print(words)

    #Displaying words that appear in either
    #file_1 or file_2 but not both
    print()
    print('The following words apear in one file, but not both')
    for words in set_1.symmetric_difference(set_2):
        print(words)

main()

    
    
