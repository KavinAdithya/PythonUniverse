from .Product import Product

class KeyBoard(Product):
    def __init__(self, name, quantity, price, brand):
        super().__init__(name, quantity, price, brand)

    def __str__(self) -> str:
        return ('\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~'
                + '\n\t\t | !^! KeyBoard ' +  self.product_details()
                + '\n\t\t | Brand : ' + self.brand
                + '\n\t\t | Available Quantity : ' + str(self.quantity)
                + '\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
