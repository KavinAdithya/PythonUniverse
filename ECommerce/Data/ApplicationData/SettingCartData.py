from PythonUniverse.ECommerce.CartFeature.CartArea import Cart
import os

class SettingCartData:
    __cart : dict = {}

    @classmethod
    def persist_cart(cls, cart : Cart):
        cls.__cart = cart.cart_products
        cls.__persist_data()

    @classmethod
    def __persist_data(cls):
        for category in cls.__cart:

            file = open("A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/CartData/" + category + ".txt", "w")
            items : dict = cls.__cart[category]

            for item in items:
                file.write(item + " " + str(items[item]) + "\n")
            file.close()

    @classmethod
    def load_cart(cls) -> Cart:

        category : dict  = {'laptop.txt' : 'laptop',
                            'speaker.txt' : 'speaker',
                            'bluetooth.txt' : 'bluetooth',
                            'mouse.txt' : 'mouse'
                            ,'keyboard.txt' : 'keyboard'}
        cart_products : dict = {}

        for cat in category:
            path : str = "A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/CartData/" + cat

            if not os.path.exists(path):
                continue

            file = open(path, "r")
            items = file.readlines()
            cart_products[category[cat]] = {}

            for item in items:
                detail : list = item.split(" ")
                cart_products[category[cat]][detail[0]] = int(detail[1])

        return Cart(cart_products, True)

    @classmethod
    def remove(cls):
        category: list = ['laptop','speaker','bluetooth','mouse','keyboard']

        for cat in category:
            path: str = "A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/CartData/" + cat + '.txt'
            if  os.path.exists(path):
                os.remove(path)

    @classmethod
    def admin_data(cls) -> list:

        path : str = 'A:/Python/PycharmProjects/PythonUniverse/ECommerce/Data/CartData/admin.txt'
        file = open(path, 'r')

        return file.readline().split(' ')

# SettingCartData.load_cart()