from abc import ABC

class Product(ABC):
    def __init__(self, name, quantity, price, brand):
        self.__name : str = name
        self.__quantity : int = quantity
        self.__price : float = price
        self.__brand  : str = brand

    '''POJO for name attribute'''
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('\t\tUndefined Name ...')
        self.name = name

    '''POJO for quantity Attribute'''
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity < 0:
            raise ValueError('\t\tUndefined Quantity.....')
        self.__quantity = quantity

    '''POJO for price Attribute'''
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError('\t\tUndefined Price.....')
        self.__price = price

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if not brand:
            raise ValueError('\t\tUndefined Brand...')
        self.__brand = brand

    def product_details(self) -> str:
        return (' Category !^!'
                + '\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n\t\t | Name : '
                + self.__name
                +  '\n\t\t | Price : ' + str( self.__price ))

    def __str__(self):
        return "\t\tProduct Category ->  No Products Available"
