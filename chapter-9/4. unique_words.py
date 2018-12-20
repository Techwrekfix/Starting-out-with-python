#This program displays list of all unique
#words found in a text file

def main():
    #ask the user for a file
    user_file = input('Enter a text file with its extension'
                      ' (example: file.txt): ')

    #Open the file for reading
    infile = open(user_file,'r')

    #create unigue words
    create_unique_words(infile)

    #Close file
    infile.close()

def create_unique_words(file):
    #create an empty set
    unique_words = set()

    #use a loop to to read the content
    #of the file and add it to the unique_words

    for word in file:
        word = word.strip('\n')
        if word not in unique_words:
            unique_words.add(word)

    print(unique_words)

main()
