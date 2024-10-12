

class Product:
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def product_details(self) -> str:
        return '  Category' + '\n Name : ' + self.name +  '\n Price : ' + self.price

    def __str__(self):
        return "Product Category ->  No Products Available"
