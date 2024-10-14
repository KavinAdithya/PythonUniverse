from .Product import Product

class KeyBoard(Product):
    def __init__(self, name, quantity, price, brand):
        super().__init__(name, quantity, price, brand)

    def __str__(self) -> str:
        return ('\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~'
                + '\n | !^! KeyBoard ' +  self.product_details()
                + '\n | Brand : ' + self.brand
                + '\n | Quantity : ' + str(self.quantity)
                + '\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
