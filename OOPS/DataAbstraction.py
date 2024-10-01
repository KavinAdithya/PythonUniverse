from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def speedoMeter(self):
        print('50 km/hr')

class BMW(Car):
    def speedoMeter(self):
        print('100 km/hr')

car = Car()
car.speedoMeter()