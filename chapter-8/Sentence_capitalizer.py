#This program is a sentence capitlizer. It capitalizes
#the first character each sentence.

#ALGORITHM in pseudocode
# 1.The sentence capitalizer accepts a user string:
# 2.using the split method, the user string is converted
#   to a list with the dot character removed.
# 3. for character in user string:
#       strip all leading and trailing characters from
#       user string and assign it to a variable
#       use the capitalze method to capitalize the first
#       character in the user_string- the capitalize method converts
#       the frist character of a string to capital letter
# 4. display results
# 5. The main function:
#       get a string from the user
#       pass the user string to the sentence_capitalizer function

#CODE:

def sentence_capitalizer(user_string):
    user_list = user_string.split('.')
    for char in user_list:
        capitalizer = char.strip().capitalize() + '. '
        print(capitalizer,end='')

def main():
    string = input('Enter a sentence: ')
    sentence_capitalizer(string)

main()
        
