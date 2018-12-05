#This program displays the shipping
#charges of a company

#Asking user to enter weight of a package
package_weight = float(input('Enter the weight of the package in pounds: '))

#Determining the shipping charges

if package_weight <= 2:
    print('The package weight for',package_weight,'pounds is $1.50')
elif package_weight < 7:
    print('The package weight for',package_weight,'pounds is $3.00')
elif package_weight < 11:
    print('The package weight for',package_weight,'pounds is $4.00')
else:
    print('The package weight for',package_weight,'pounds is $4.75')
