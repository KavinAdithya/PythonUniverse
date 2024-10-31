from PythonUniverse.ECommerce.BootData.FetchObjectCreation import Entity_Data
from PythonUniverse.ECommerce.DataPersistent.DataBaseInterface import DataBaseInterface
from PythonUniverse.ECommerce.Exceptions.ProductMissingException import ProductMissingException
from PythonUniverse.ECommerce.Exceptions.UnauthorizedAccess import UnauthorizedException

class Feature:
    isFiles : bool = False
    dictionary : dict = {}
    @classmethod
    def load_products(cls, isFiles):
        cls.isFiles = isFiles
        if isFiles:
            cls.__default_load()
            return
        cls.dictionary =  DataBaseInterface.get_products()

    @classmethod
    def __default_load(cls):
        cls.dictionary['laptop'] = Entity_Data.get_laptop(
            'A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/AppData/')
        cls.dictionary['keyboard'] = Entity_Data.get_keyboard(
            'A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/AppData/')
        cls.dictionary['bluetooth'] = Entity_Data.get_bluetooth(
            'A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/AppData/')
        cls.dictionary['speaker'] = Entity_Data.get_speaker(
            'A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/AppData/')
        cls.dictionary['mouse'] = Entity_Data.get_mouse(
            'A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/AppData/')

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
         isEmpty : bool = True
         for category in cls.dictionary:
            isEmpty = False
            print('\n\t\t ', category.upper())
            products = cls.dictionary[category]

            for product in products:
                if product.quantity < 1:
                    continue
                print(product)
            print()

         if isEmpty:
             print('No Products Available Right Now...')
    @classmethod
    def admin_addProducts(cls, password, category, item):
        if password == 'KavinDharani@3':
            cls.__add_product(category, item)
            print('\n\t\t KaVin Product has been added to our Application.... !^!')
        else:
            raise UnauthorizedException('\n\t\t Access Denied...')

    @classmethod
    def increases_product(cls):
        category : str = input("\t\t Enter The Category : ").lower()
        name : str = input("\t\t Enter Name  : ").lower()
        quantity : int = int(input('\t\t Enter The Quantity : '))

        if  cls.isValidCategory(category):
            raise ProductMissingException('\n\t\t Undefined Category...')

        items : list = cls.dictionary[category]

        isSuccess = False
        for item in items:

            if item.name.lower() == name:
                item.quantity = item.quantity + quantity
                isSuccess = True
        if not isSuccess:
            raise ProductMissingException('\n\t\t Brand You Have Provided Does not Exists!!!')
        else:
            print('\n\t\t Product Quantity Has Been Added Successfully... !^!')