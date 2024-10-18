from .Product import Product

class Speaker(Product):

    def __init__(self, name, quantity, price, brand, driver, connectivity):
        super().__init__(name, quantity, price, brand)
        self.__driver : str = driver
        self.__connectivity : str = connectivity

    @property
    def driver(self) -> str:
        return self.__driver

    @driver.setter
    def driver(self, driver):
        if not driver:
            raise ValueError('\t\tUndefined Driver ...')
        self.driver = driver

    @property
    def connectivity(self) -> str:
        return self.__connectivity

    @connectivity.setter
    def connectivity(self, connectivity):
        if not connectivity:
            raise ValueError('\t\tUndefined Driver ...')
        self.connectivity = connectivity

    def __str__(self) -> str:
        return ('\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~'
                + '\n\t\t |  !^! Speaker'
                + self.product_details()
                + '\n\t\t | Brand : ' + self.brand
                + '\n\t\t | Driver : ' + self.__driver
                + '\n\t\t | Connectivity : ' + self.__connectivity
                + '\n\t\t | Available Quantity : ' + str(self.quantity)
                + '\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')