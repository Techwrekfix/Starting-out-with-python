#This module is a RetailItem class

class RetailItem:

    #Initializing the data attributes
    def __init__(self,item_description,units_in_inventory,price):
        self.__item_description = item_description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def set_item_description(self,item_description):
        self.__item_description = item_description

    def set_units_in_inventory(self,units_in_inventory):
        self.__units_in_inventory = units_in_inventory

    def set_price(self,price):
        self.__price = price

    def get_item_description(self):
        return self.__item_description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price
    
        
