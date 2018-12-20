#This program is about word frequency

def main():
    #ask the user for a file
    user_file = input('Enter a text file with its extension'
                      ' (example: file.txt): ')

    #Open the file for reading
    infile = open(user_file,'r')

    #create word frequency
    frequency = create_word_frequency(infile)

    #Close file
    infile.close()

def create_word_frequency(file):
    #Create an empty dictionary
    word_frequency = {}
    count = 1   #To count the number of times a word appers in the file

    for word in file:
        word = word.strip('\n')
        if word not in word_frequency:
            word_frequency[word] = count
        else:
            word_frequency[word] += 1
    
    print(word_frequency)
        
main()
