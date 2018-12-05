#This program calculates calories from a fat

def main():
    fat_grams = float(input('Enter the number of fat grams: '))
    carb_grams = float(input('Etner the number of carb_grams: '))
    fat_calories = calculate_fat_calories(fat_grams)
    carb_calories = calculate_carb_calories(carb_grams)

    #Displaying fats calories from fat and carbohydrates
    print('\nThe calories from fat is: ',fat_calories,'calories \nThe '\
          'calories from carbohydrate is: ',carb_calories,'calories')

def calculate_fat_calories(fat_grams):
    calories_from_fat = fat_grams * 9
    return calories_from_fat
def calculate_carb_calories(carb_grams):
    calories_from_carb = carb_grams * 4
    return calories_from_carb
main()

