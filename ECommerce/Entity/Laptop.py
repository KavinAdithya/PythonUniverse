from .Product import Product

class Laptop(Product):

    def __init__(self, name,  quantity, price , brand, main_memory, processor, secondary_storage):
        super().__init__(name, quantity, price, brand)
        self.__main_memory : int = main_memory
        self.__processor : str = processor
        self.__secondary_storage : int = secondary_storage

    @property
    def main_memory(self) -> int:
        return self.__main_memory

    @main_memory.setter
    def main_memory(self, main_memory):
        if main_memory < 0:
            raise ValueError('\t\tUndefined main_memory...')
        self.__main_memory = main_memory

    @property
    def processor(self) -> str:
        return self.__processor

    @processor.setter
    def processor(self, processor):
        if processor < 0:
            raise ValueError('\t\tUndefined Processor.....')
        self.__processor = processor

    @property
    def secondary_storage(self) -> int:
        return self.__secondary_storage

    @secondary_storage.setter
    def secondary_storage(self, secondary_storage):
        if secondary_storage < 0:
            raise ValueError('\t\tUndefined Secondary Storage.....')
        self.__secondary_storage = secondary_storage

    def process_details(self) -> str:
        return ('\n\t\t | Brand : ' + self.brand
                + '\n\t\t | Processor : ' + self.processor
                + '\n\t\t | Main Memory : ' + str(self.main_memory)
                + 'GB\n\t\t | Secondary Memory : ' + str(self.secondary_storage)
                + 'GB\n\t\t | Available Quantity : ' + str(self.quantity)
                + '\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')

    def __str__(self) -> str:
        return  ('\n\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~'
                 +'\n\t\t |  !^! Laptop'
                 + self.product_details()
                 + ' ' +self.process_details())