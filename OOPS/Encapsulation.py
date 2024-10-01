class Car:
    def __init__(self, brand, price):
        self._brand = brand
        self.__price = price

    @property
    def brand(self):
        return self._brand

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float):
            self.__price = new_price


car = Car('BMW', 100000.0)
car.price = 200000.00
# print(car._Car__price) Name Mangling
print(car.price)