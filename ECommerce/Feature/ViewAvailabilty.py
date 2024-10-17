from PythonUniverse.ECommerce.Entity import Mouse, Laptop, KeyBoard, Bluetooth, Speaker
from PythonUniverse.ECommerce.Exceptions.ProductMissingException import ProductMissingException
from PythonUniverse.ECommerce.Exceptions.UnauthorizedAccess import UnauthorizedException

class Feature:
    dictionary = {}

    @classmethod
    def default_load(cls):
        cls.dictionary['laptop'] = [Laptop.Laptop('Mega Book', 20, 45000.00, 'Techno', 32, "Intel I5", 1024)]
        cls.dictionary['keyboard'] = [KeyBoard.KeyBoard('JackPot', 12, 1000.00, 'Dell')]
        cls.dictionary['bluetooth'] = [Bluetooth.Bluetooth('KaVin', 30, 2800.00, 'One Plus Nord Buds', 20, 'AAC')]
        cls.dictionary['speaker'] = [Speaker.Speaker('Smarter', 20, 10000.00, 'Samsung', 'tweeters, woofers', 'Bluetooth')]
        cls.dictionary['mouse'] = [Mouse.Mouse('Rat', 24, 1000.00, 'Dell', 'Heavy DOI', 1000, True)]

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