#This program mix primary colors Red,
#Blue and Yellow.

#Getting primary color name from user
primary_color1 = input("Input the name of primary"\
                       " color 1: ")
primary_color2 = input("Input the name of primary"\
                       " color 2: ")
print()
#Assigning the primary colors the mixing results

if primary_color1 == 'red' and primary_color2 == 'blue' \
   or primary_color1 == 'blue' and primary_color2 == 'red':
    print(primary_color1, 'mixed with', primary_color2, \
          'is Purple')
elif (primary_color1 == 'red' and primary_color2 == 'yellow')\
     or (primary_color1 == 'yellow' and primary_color2 == 'red'):
    print(primary_color1, 'mixed with', primary_color2, \
          'is Orange')
elif (primary_color1 == 'yellow' and primary_color2 == 'blue')\
   or (primary_color1 == 'blue' and primary_color2 == 'yellow'):
    print(primary_color1, 'mixed with', primary_color2, \
          'is Green')
else:
    print("Error! either",primary_color1, "or", primary_color2, \
          "or Both is not a primary color")        
