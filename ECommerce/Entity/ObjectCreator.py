from PythonUniverse.ECommerce.Entity.Bluetooth import Bluetooth
from PythonUniverse.ECommerce.Entity.KeyBoard import KeyBoard
from PythonUniverse.ECommerce.Entity.Laptop import Laptop
from PythonUniverse.ECommerce.Entity.Speaker import Speaker
from PythonUniverse.ECommerce.Feature.ViewAvailabilty import Feature

class ObjectCreator:

    @classmethod
    def __product_creator(cls, category) -> list:
        attribute = []
        try:
            name : str = input('\n\t\t Enter the name of the device : ')
            quantity : int = int(input('\t\t Enter the Default Quantity of the ' + category + ' : '))
            price : float = float(input('\t\t Enter the price of the '+ category + ' : '))
            brand : str = input('\t\t Enter the model / Brand : ')

            attribute.append(name)
            attribute.append(quantity)
            attribute.append(price)
            attribute.append(brand)
        except ValueError as e:
            raise ValueError(e)

        return attribute

    @classmethod
    def laptop_creator(cls, password):
        attribute = cls.__product_creator('Laptop')
        try:
            main_memory : int = int(input('\t\t Enter the size of Main Memory (MB) : '))
            processor : str = input('\t\t Enter the name of the Processor : ')
            secondary_memory : int = int(input('\t\t Enter the name of the Secondary Memory (MB) : '))
        except ValueError as e:
            raise ValueError(e)

        laptop = Laptop(attribute[0], attribute[1], attribute[2], attribute[3], main_memory, processor, secondary_memory)
        Feature.admin_addProducts(password, 'laptop', laptop)

    @classmethod
    def bluetooth_creator(cls, password):
        attribute = cls.__product_creator('Bluetooth')
        try:
            scope : int = int(input('\t\t Enter the scope of the device : '))
            codec_support : str = input('\t\t Enter the codec support : ')
        except ValueError as e:
            raise ValueError(e)

        bluetooth = Bluetooth(attribute[0], attribute[1], attribute[2], attribute[3], scope, codec_support)
        Feature.admin_addProducts(password, 'bluetooth', bluetooth)

    @classmethod
    def keyboard_creator(cls, password):
        attribute = cls.__product_creator('Key Board')

        keyboard = KeyBoard(attribute[0], attribute[1], attribute[2], attribute[3])
        Feature.admin_addProducts(password, 'Keyboard', keyboard)

    @classmethod
    def mouse_creator(cls, password):
        attribute = cls.__product_creator('Mouse')
        try:
            DOI : str = input('\t\t Enter the DOI (Dot Per Inch): ')
            polling_rate : int = int(input('\t\t Enter the Polling Rate : '))
            isErgonomics : bool = bool(input('\t\t Is it supports Ergonomics '))
        except ValueError as e:
            raise ValueError(e)

        mouse = Laptop(attribute[0], attribute[1], attribute[2], attribute[3], DOI, polling_rate, isErgonomics)
        Feature.admin_addProducts(password, 'mouse', mouse)

    @classmethod
    def speaker_creator(cls, password):
        attribute = cls.__product_creator('Speaker')
        try:
            driver : str = input('\t\t Enter the driver : ')
            connectivity : str = input('\t\t Enter the Connectivity: ')
        except ValueError as e:
            raise ValueError(e)

        speaker = Speaker(attribute[0], attribute[1], attribute[2], attribute[3], driver, connectivity)
        Feature.admin_addProducts(password, 'speaker', speaker)

# 93 12 54 47 39 60 38 98 34 6 60 133 -> 674