from PythonUniverse.ECommerce.CartFeature.CheckOutCart import Checkout
from PythonUniverse.ECommerce.Data.ApplicationData.SettingCartData import SettingCartData
from PythonUniverse.ECommerce.Data.ApplicationData.SettingData import SettingData
from PythonUniverse.ECommerce.Entity.ObjectCreator import ObjectCreator
from PythonUniverse.ECommerce.Exceptions.UnauthorizedAccess import UnauthorizedException
from PythonUniverse.ECommerce.Feature.ViewAvailabilty import Feature
import sys

''' Its a User Interface to provide abstraction on operations'''

class Runner:
    cart = SettingCartData.load_cart()

    @classmethod
    def __title(cls):
        print('\n\n\t\t\t\t Welcome Techies !!!!')
        print('\t\t\t\t\t  ~ TechCrack')

    @classmethod
    def __choices(cls):
        print('\n\n\t\t ---------- Select Your Operation ----------')
        print('\n\t\t 1 -> \tView the Products               <- 1')
        print('\t\t 2 -> \tAdd Products to the Cart        <- 2')
        print('\t\t 3 -> \tView the Cart                   <- 3')
        print('\t\t 4 -> \tRemove Products from the Cart   <- 4')
        print('\t\t 5 -> \tEstimate Cost and Checkout      <- 5')
        print('\t\t 6 -> \tExit                            <- 6')

    @classmethod
    def __manage_operation(cls):
        n : int = 0
        try:
            n = int(input('\n\t\t What You like to proceed -   '))
            cls.__invoke_operation(n)
        except ValueError as e:
            print('\t\t Invalid Operation Selection...')
            cls.__end()
        except Exception as e:
            print(e)

    @classmethod
    def __invoke_operation(cls, n):
        if n == 1:
            Feature.view_availability()
        elif n == 2:
            data = cls.__get_product_data()
            cls.cart.addProducts(data[0], data[1], data[2])
        elif n == 3:
            cls.cart.view_cart()
        elif n == 4:
            data = cls.__get_product_data()
            cls.cart.remove_product(data[0], data[1], data[2])
        elif n == 5:
            cls.cart.view_cart()
            checkout = Checkout(cls.cart.products, cls.cart.cart_products)
            checkout.estimate_cost()
            if 'yes' == input('\t\t Are You want to checkout (Yes / No) ??  :   ').lower():
                checkout.check_out()
            cls.__end()
        elif n == 9360016740:
            print('\n\t\t !^! Admin Usage !^!')
            print('\t\t Welcome KaVin <%3>?/')
            cls.__control_admin()
        else:
            print('\n\t\t Invalid Operation...')
            cls.__end()

    @classmethod
    def __get_product_data(cls) -> list:
        product = []

        try:
            product.append(input('\n\t\t Enter Category : '))
            product.append(input('\t\t Enter Product model : '))
            product.append(int(input('\t\t Enter Quantity Which you needed : ')))
        except ValueError as e:
            print('\t\t Invalid Product Data Format...')
            cls.__end()

        return product

    @classmethod
    def __end(cls):
        print('\n\t\t\t\t\t\t!^! Thank You !^!')
        SettingData.store_data()
        SettingCartData.persist_cart(cls.cart)
        sys.exit()

    @classmethod
    def start_application(cls, isTitle):
        if isTitle:
            cls.__title()
        cls.__choices()
        cls.__manage_operation()
        if 'yes' == input('\n\t\t Are You Want to continue it (Yes / No) : ').lower():
            cls.start_application(False)
        else:
            cls.__end()

    @classmethod
    def __control_admin(cls):
        password = input('\n\t\t Secret Authentication : ')

        if not password == 'KavinDharani@3':
            raise UnauthorizedException('\t\t Invalid Codee.. Try Again...')

        if 'yes' == input('\n\t\t Are You Want increases the quantity of the products : ').lower():
            Feature.increases_product()
            return

        print('\n\t\t --- Select the Category ---')
        print('\n\t\t 1 -> \tLaptop        <- 1')
        print('\t\t 2 -> \tBluetooth     <- 2')
        print('\t\t 3 -> \tKeyBoard      <- 3')
        print('\t\t 4 -> \tMouse         <- 4')
        print('\t\t 5 -> \tSpeaker       <- 5')
        n : int = 0
        try:
            n = int(input('\n\t\t What Would You like to Proceed : '))
        except ValueError as e:
            raise e
        cls.__invoke_category(n, password)

    @classmethod
    def __invoke_category(cls, n, password):
        oc = ObjectCreator
        if n == 1:
            oc.laptop_creator(password)
        elif n == 2:
            oc.bluetooth_creator(password)
        elif n == 3:
            oc.keyboard_creator(password)
        elif n == 4:
            oc.mouse_creator(password)
        elif n == 5:
            oc.speaker_creator(password)
        else:
            print('Invalid Category...')