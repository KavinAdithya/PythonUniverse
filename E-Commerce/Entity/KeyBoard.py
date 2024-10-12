import Product

class KeyBoard(Product):
    def __init__(self, name, quantity, price, brand):
        super().__init__(name, quantity, price)
        self.__brand = brand


    def __str__(self) -> str:
        return 'KeyBoard ' +  self.product_details() + '\n Brand ' + self.brand + '\n Quantity : ' + self.quantity
