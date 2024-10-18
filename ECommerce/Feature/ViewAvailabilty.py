from PythonUniverse.ECommerce.Entity import Mouse, Laptop, KeyBoard, Bluetooth, Speaker
from PythonUniverse.ECommerce.Exceptions.ProductMissingException import ProductMissingException
from PythonUniverse.ECommerce.Exceptions.UnauthorizedAccess import UnauthorizedException

from ECommerce.BootData.FetchObjectCreation import Entity_Data


class Feature:
    dictionary = {}

    @classmethod
    def default_load(cls):
        cls.dictionary['laptop'] = Entity_Data.get_laptop('')
        cls.dictionary['keyboard'] = Entity_Data.get_keyboard('')
        cls.dictionary['bluetooth'] = Entity_Data.get_bluetooth('')
        cls.dictionary['speaker'] = Entity_Data.get_speaker('')
        cls.dictionary['mouse'] = Entity_Data.get_mouse('')

    @classmethod
    def __add_product(cls, category, item):
        category = category.lower()
        if  cls.isValidCategory(category):
            raise ProductMissingException('\t\tUndefined Category...')
        if cls.__isObjectAvailable(category, item):
            return
        cls.dictionary[category].append(item)

    @classmethod
    def __isObjectAvailable(cls, category, item) -> bool:
        if category not in cls.dictionary:
            return False

        items = cls.dictionary[category]

        for l in items:
            if item.brand == l.brand:
                return True

        return False

    @classmethod
    def isValidCategory(cls, category):
        return category not in cls.dictionary

    @classmethod
    def view_availability(cls):
         print()
         for category in cls.dictionary:

            print('\t\t ', category.upper())
            products = cls.dictionary[category]

            for product in products:
                print(product)
            print()

    @classmethod
    def admin_addProducts(cls, password, category, item):
        if password == 'KavinDharani@3':
            cls.__add_product(category, item)
            print('\n\t\t KaVin Product has been added to our Application.... !^!')
        else:
            raise UnauthorizedException('\t\tAccess Denied...')