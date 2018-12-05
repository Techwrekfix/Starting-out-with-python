#This program calculates a hotdog cookout
#Assigning variables
hot_dog_package = 10
hotdog_bun_package = 8

#Asking the user for the number of attendance and
#number of hotdogs nedded
number_of_people = int(input('Enter the number of people attending ' \
                             'the hot dog cookout: '))
number_hotdog_per_person = int(input('Enter the number of hot ' \
                               'dogs each of the '+ \
                                     str(number_of_people) + ' people needs: '))
print()
#Making necessary calculations
hotdogs_needed = number_of_people * number_hotdog_per_person
hotdogs_buns_needed = hotdogs_needed

exact_hotdogs_packages = hotdogs_needed / hot_dog_package
exact_hotdogs_bun_packages = hotdogs_buns_needed / hotdog_bun_package

hotdogs_package_remainder = hotdogs_needed % hot_dog_package
hotdogs_bun_package_remainder =  hotdogs_buns_needed % hotdog_bun_package

if hotdogs_package_remainder > 0:
    mimimunm_hotdog_package_required = int(exact_hotdogs_packages + 1)
else:
    mimimunm_hotdog_package_required = int(exact_hotdogs_packages)

if hotdogs_bun_package_remainder > 0:
    mimimunm_hotdogs_bun_package_required = int(exact_hotdogs_bun_packages + 1)
else:mimimunm_hotdogs_bun_package_required = int(exact_hotdogs_bun_packages)

hotdogs_leftover = int(float(format(mimimunm_hotdog_package_required - \
                                exact_hotdogs_packages,'.2f'))* hot_dog_package)
hotdogs_buns_leftover = int(float(mimimunm_hotdogs_bun_package_required - \
                                  exact_hotdogs_bun_packages)* hotdog_bun_package)


#Displaying the output

print('The minimum number of hot dogs packages required is: ',mimimunm_hotdog_package_required, \
      '\nThe minimum number of hot dogs bun packages required is: '\
      ,mimimunm_hotdogs_bun_package_required,'\nThe number of hot dogs left over is: ' \
      ,hotdogs_leftover, '\nThe number of hot dogs bun left over is: ' \
      ,hotdogs_buns_leftover)

      
