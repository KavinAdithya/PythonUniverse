from .Product import Product

class Bluetooth(Product):
    def __init__(self, name, quantity, price, brand, scope, codec_support):
        super().__init__(name, quantity, price, brand)
        self.__range : int = scope
        self.__codec_support : str = codec_support

    @property
    def range(self) -> int:
        return self.range

    @range.setter
    def range(self, scope):
        if scope < 0:
            raise ValueError('Undefined Range...')
        self.__range = scope

    @property
    def codec_support(self) -> str:
        return self.__codec_support

    @codec_support.setter
    def codec_support(self, codec_support):
        if not codec_support:
            raise ValueError('Undefined codec Support...')
        self.__codec_support = codec_support

    def __str__(self) -> str:
        return ('\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~'
                + '\n\t\t | !^! Bluetooth '
                + self.product_details()
                + '\n\t\t | Brand : ' + self.brand
                + '\n\t\t | Bluetooth Range : '
                + str(self.__range)
                + '\n\t\t | Codec Support : '
                + self.__codec_support
                + '\n\t\t | Available Quantity : ' + str(self.quantity)
                + '\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')
