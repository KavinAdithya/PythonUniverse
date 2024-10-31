from pymysql.cursors import Cursor

from PythonUniverse.ECommerce.DataPersistent.DataAccessObject import Data_Access_Object
from PythonUniverse.ECommerce.Entity.Bluetooth import Bluetooth
from PythonUniverse.ECommerce.Entity.KeyBoard import KeyBoard
from PythonUniverse.ECommerce.Entity.Laptop import Laptop
from PythonUniverse.ECommerce.Entity.Mouse import Mouse
from PythonUniverse.ECommerce.Entity.Speaker import Speaker


class DataBaseInterface:
    __cart : dict = {}
    __application_product : dict = {}
    __admin : list = []
    __cursor : Cursor = Data_Access_Object.get_cursor()

    @classmethod
    def load_cart(cls):
        query : str = ('SELECT c.product_name, a.product_name, a.count FROM cart a '
                       'INNER JOIN category c '
                       'ON a.cart_id = c.category_id')
        cls.__cursor.execute(query)

        data : tuple = cls.__cursor.fetchall()

        for value in data:
            if value[0] in cls.__cart:
                cls.__cart[value[0]][value[2]] = value[1]
            else:
                cls.__cart[value[0]] = {value[1] :  value[2]}

    @classmethod
    def __load_laptop_product(cls):
        query : str = ('SELECT p.product_name, p.quantity, '
                       'p.price, p.brand, l.main_memory, '
                       'l.processor, l.secondary_storage '
                       'FROM laptop l INNER JOIN product p ON p.product_id = l.product_id')

        laptop : list = []
        cls.__cursor.execute(query)
        items : tuple = cls.__cursor.fetchall()

        for item in items:
            laptop.append(Laptop(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

        cls.__application_product['laptop'] = laptop

    @classmethod
    def __load_keyboard_product(cls):
        query: str = ('SELECT p.product_name, p.quantity, '
                      'p.price, p.brand '
                      'FROM keyboard k INNER JOIN product p ON p.product_id = k.product_id')

        keyboard : list = []
        cls.__cursor.execute(query)
        items: tuple = cls.__cursor.fetchall()

        for item in items:
            keyboard.append(KeyBoard(item[0], item[1], item[2], item[3]))

        cls.__application_product['keyboard'] = keyboard

    @classmethod
    def __load_mouse_product(cls):
        query: str = ('SELECT p.product_name, p.quantity, '
                      'p.price, p.brand, m.dot_per_inch, '
                      'm.polling_rate, m.isErgonomics '
                      'FROM mouse m INNER JOIN product p ON p.product_id = m.product_id')

        mouse : list = []
        cls.__cursor.execute(query)
        items: tuple = cls.__cursor.fetchall()

        for item in items:
            mouse.append(Mouse(item[0], item[1],item[2], item[3], item[4], item[5], item[6]))

        cls.__application_product['mouse'] = mouse

    @classmethod
    def __load_speaker_product(cls):
        query: str = ('SELECT p.product_name, p.quantity, '
                      'p.price, p.brand,'
                      's.driver, s.connectivity'
                      ' FROM speaker s INNER JOIN product p ON p.product_id = s.product_id')

        speaker : list = []
        cls.__cursor.execute(query)
        items: tuple = cls.__cursor.fetchall()

        for item in items:
            speaker.append(Speaker(item[0], item[1], item[2], item[3], item[4], item[5]))

        cls.__application_product['speaker'] = speaker

    @classmethod
    def __load_bluetooth_product(cls):
        query: str = ('SELECT p.product_name, p.quantity, ' +
                      'p.price, p.brand, b.scope, ' +
                      'b.codec_support' +
                      ' FROM bluetooth b INNER JOIN product p ON p.product_id = b.product_id')

        bluetooth : list = []
        cls.__cursor.execute(query)
        items: tuple = cls.__cursor.fetchall()

        for item in items:
            bluetooth.append(Bluetooth(item[0], item[1], item[2], item[3], item[4], item[5]))

        cls.__application_product['bluetooth'] = bluetooth

    @classmethod
    def load_product(cls):
         cls.__load_laptop_product()
         cls.__load_mouse_product()
         cls.__load_speaker_product()
         cls.__load_bluetooth_product()
         cls.__load_keyboard_product()

    @classmethod
    def load_admin(cls):
        query : str = 'SELECT * FROM admin WHERE admin_id = 1'
        cls.__cursor.execute(query)
        data : tuple = cls.__cursor.fetchall()

        cls.__admin.append(data[0][1])
        cls.__admin.append(data[0][2])

    @classmethod
    def get_admin(cls) -> list:
        return cls.__admin

    @classmethod
    def get_cart(cls) -> dict:
        return cls.__cart

    @classmethod
    def get_products(cls) -> dict:
        return cls.__application_product

DataBaseInterface.load_cart()
DataBaseInterface.load_product()
DataBaseInterface.load_admin()