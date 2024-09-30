class Laptop:
    name = 'Techno'

    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram


    def show_configuration(self) -> bool:
        print('Name : ', self.name)
        print('Processor : ', self.processor)
        print(f"Ram : {self.ram}GB")
        return True

    @classmethod
    def update_name(cls):
        Laptop.name = 'Tech-crack'

    @staticmethod
    def addNumber(a : int , b : int) -> int:
        return a + b


z : int = Laptop.addNumber(2, 2)
print(z)
print(Laptop.name)
Laptop.update_name()
Laptop.update_name()
print(Laptop.name)
Laptop('intel i5', 16).show_configuration()