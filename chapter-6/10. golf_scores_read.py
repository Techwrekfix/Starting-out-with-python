#This program reads data from the golf.txt record

def main():
    try:
        #open the file
        user_file = open('golf.txt', 'r')

        #read first field in the record
        print('Here are the details of the players')
        print('\nName\t\t\tScore')
        print('-------\t\t\t----')
        name = user_file.readline()
        

        while name != '':
            #reading the next field in the record
            score = user_file.readline()
            
            #stripping the newline character
            name = name.rstrip('\n')
            score = score.rstrip('\n')

            #print the details
            print(name,'\t\t',score)
            
            #start reading the record again
            name = user_file.readline()
            name = name.rstrip('\n')
        #close the file
        user_file.close()
    except Exception as err:
        print(err)        
main()
    
        
        
