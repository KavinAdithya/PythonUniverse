from .Product import Product

class Mouse(Product):
    ''' DOI -> Dot Per Inch '''
    def __init__(self, name, quantity, price, brand, DOI, polling_rate, isErgonomics):
        super().__init__(name, quantity, price, brand)
        self.__DOI : str = DOI
        self.__polling_rate : int  = polling_rate
        self.__isErgonomics : bool = isErgonomics

    @property
    def DOI(self) -> str:
        return self.DOI

    @DOI.setter
    def DOI(self, DOI):
        if not DOI:
            raise ValueError('\t\tUndefined DOI (Dot Per Inch) ...')
        self.DOI = DOI
    
    @property
    def polling_rate(self) -> str:
        return self.polling_rate

    @polling_rate.setter
    def polling_rate(self, polling_rate):
        if not polling_rate:
            raise ValueError('\t\tUndefined Polling Rate ...')
        self.polling_rate = polling_rate

    @property
    def isErgonomics(self) -> str:
        return self.isErgonomics

    @isErgonomics.setter
    def isErgonomics(self, isErgonomics):
        self.isErgonomics = isErgonomics

    def __str__(self) -> str:
        return ( '\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~'
                 + '\n\t\t |  !^! Mouse'
                 + self.product_details()
                 + '\n\t\t | Dot Per Inch (DOI) : ' + self.__DOI
                 + '\n\t\t | Polling Rate : ' + str(self.__polling_rate)
                 + '\n\t\t | Is Ergonomice : ' + str(self.__isErgonomics)
                 + '\n\t\t | Available Quantity : ' + str(self.quantity)
                 + '\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~' )