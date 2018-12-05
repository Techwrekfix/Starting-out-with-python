#This program calculates the area of two rectangles
#and compare which of the two has greater area or
#if the two areas of the rectangle are the same.

#Collecting details of  Rectangle_1 from user
length_1 = float(input('Enter the length of rectangle_1: '))
width_1 = float(input('Enter the width of rectangle_1: '))
area_of_rectangle_1 = length_1 * width_1

#Collecting details of rectangle_2 from user
length_2 = float(input('Enter the length of rectangle_2: '))
width_2 = float(input('Enter the width of rectangle_2: '))
area_of_rectangle_2 = length_2 * width_2

#comparing the rectangles
if area_of_rectangle_1 > area_of_rectangle_2:
    print("\nArea of Rectangle 1 is greater")
elif area_of_rectangle_2 > area_of_rectangle_1:
    print("\nArea of Rectangle 2 is greater")
else:
    print("\nArea of both rectangles are the same")
