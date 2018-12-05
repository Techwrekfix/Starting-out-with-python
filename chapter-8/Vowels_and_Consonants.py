#This program displays the number of vowels and
#and consonants in a string

#ALGORITHM in pseudocode
#create a global constant:
#   VOWEL = 'a','e','i','o','u'
# 1.The is vowel function accepts a user string as argument:
#       for character in user_string:
#           if vowel is in character:
#               count equals + 1
#           return count
#
# 2.The is consonant function accepts a user_string as argumnent:
#       for characters in user_string:
#           if vowel not in character:
#               count equals +1
#            return count
#
# 3.The main function:
#       1.get user to enter a string
#       2.create the is vowel function passing user_string as argument
#       3.create the is consonant function passing user_string as argument

#CODE:

VOWEL= 'aeiou'     #the vowel constant

def is_vowel(user_string):
    count = 0   #initiate the vowel count variable
    for char in user_string:
        if char in VOWEL:
            count += 1
    print(user_string)
    print('The number of vowels in the sentence are:',count)

def is_consonant(user_string):
    user_string = user_string
    count = 0   #initiate the consonant count variable
    for char in user_string:
        if char not in VOWEL:
            count += 1
    print('The number of consonants in the sentence are:',count)

def main():
    string = input('Enter a sentence to count the number of'\
                   ' vowels and consonants: ').strip()
    
    is_vowel(string)
    is_consonant(string)
    
main()
    
