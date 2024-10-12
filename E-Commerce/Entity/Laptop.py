import  Product
class Laptop(Product):

    def __init__(self, name, price , quantity,  brand, main_memory, processor, secondary_storage):
        super().__init__(name, quantity, price)
        self.__brand = brand
        self.__main_memory = main_memory
        self.__processor = processor
        self.__secondary_storage = secondary_storage

    def process_details(self) -> str:
        return '\n Brand : ' + self.brand + '\n Processor : ' + self.processor + '\n Main Memory : ' + self.main_memory + 'GB\n Secondary Memory : ' + self.secondary_storage + 'GB\n Quantity : ' + self.quantity

    def __str__(self) -> str:
        return ' Laptop ' + self.product_details() + ' ' +self.process_details()