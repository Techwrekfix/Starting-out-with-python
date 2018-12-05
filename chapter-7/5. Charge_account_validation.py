#This program reads the content of a file into a list
#and search for some contents

def main():
    #open the file for reading
    infile = open('charge_accounts.txt','r')
    #read the content of the file

    accounts = infile.readlines()

    infile.close()

    index = 0
    while index < len(accounts):
        accounts[index] = accounts[index].rstrip('\n')
        index += 1
    print(accounts)
    print()

    #asking user for charge account number
    search = input('Enter a charge account number: ')

    #searching for the account number
    if search in accounts:
        print(search,'is valid.')
    else:
        print(search,'is invalid.')
main()

    
