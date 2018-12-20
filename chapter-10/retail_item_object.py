#This program utilizes the RetailItem class

import retail_item_class

def main():

    create = create_object()
    display = display_objects(create)

def create_object():
    #Creating three ReatailItem objects
    items_list = []
    for count in range(3):
        print('Item #',count + 1,sep='')
        description = input('Enter Item description: ')
        inventory = input('Enter Units in Inventory: ')
        price = float(input('Enter Item price: '))
        print()

        item_details = retail_item_class.RetailItem(description,inventory,price)
        #append objects to list
        items_list.append(item_details)

    return items_list

def display_objects(objects):
    #displaying items in objects
    for items in objects:
        print('Item Description:',items.get_item_description())
        print('Units in Inventory:',items.get_units_in_inventory())
        print('Price:',items.get_price())
        print()

main()
    
    
    
