#This program measure the weight of objects

#Getting the mass of an object from user
mass_of_object = float(input("Enter the mass of the" \
                             " mass of the object: "))
#Calculating the weight:
weight = mass_of_object * 9.8
print("\nThe weight of the object is N", format(weight,'.2f'),sep='')

if weight > 500:
    print("\nThis object is too heavy")
elif weight < 100:
    print("\nThis object is too light")
        
