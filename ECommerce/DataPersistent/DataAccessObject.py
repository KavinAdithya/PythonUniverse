import pymysql
from pymysql.connections import Connection
from pymysql.cursors import Cursor
# from PythonUniverse.ECommerce.UserInterface.Runner import Runner

class Data_Access_Object:
    connection : Connection = None
    cursor : Cursor = None
    # isFiles : bool = Runner.isFiles
    isFiles : bool = False

    @classmethod
    def load_connector(cls):
        connection : Connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'KavinDharani@3',
            database = 'eCommerceData'
        )
        cls.connection = connection
        cls.cursor = cls.connection.cursor()

    @classmethod
    def insert_data(cls, attributes : tuple, category : str):
        queries : list[str] = ['INSERT INTO laptop VALUES(%s, %s, %s, %s)',
                               'INSERT INTO bluetooth VALUES(%s, %s, %s)',
                               'INSERT INTO mouse VALUES(%s, %s, %s, %s)',
                               'INSERT INTO speaker VALUES(%s, %s, %s)',
                               'INSERT INTO keyboard VALUES(%s)']
        index : int = 0
        if category == 'bluetooth':
            index = 1
        elif category == 'mouse':
            index = 2
        elif category == 'speaker':
            index = 3
        elif category == 'keyboard':
            index = 4
        cls.cursor.execute(queries[index], attributes)
        cls.connection.commit()

    @classmethod
    def product_insert_data(cls, attributes : tuple) -> int:
        cls.cursor.execute('INSERT INTO product(product_name, quantity, price, brand) VALUES(%s, %s, %s, %s)', attributes)
        cls.cursor.execute('SELECT product_id FROM product Where product_name = "' + attributes[0] + '"')
        index : int = cls.cursor.fetchall()[0][0]
        cls.connection.commit()
        return index

    @classmethod
    def get_cursor(cls) -> Cursor:
        return cls.cursor

    @classmethod
    def insert_cart_data(cls, category : str, brand : str, count : int):
        isExists : str = 'SELECT EXISTS (SELECT 1 FROM cart WHERE product_name = %s)'
        cls.cursor.execute("SET SQL_SAFE_UPDATES = 0")
        cls.cursor.execute(isExists, (brand,))
        query: str

        if cls.cursor.fetchall()[0][0] == 1:
            query  = 'UPDATE cart SET count = count + %s WHERE product_name = %s'
        else:
            query = 'INSERT INTO cart(cart_id, count, product_name) VALUES(' + str(cls.__find_index(category)) + ', %s, %s)'

        cls.cursor.execute(query, (count, brand))
        cls.cursor.execute("DELETE FROM cart WHERE count = 0")
        cls.cursor.execute("SET SQL_SAFE_UPDATES = 1")
        cls.connection.commit()

    @classmethod
    def __find_index(cls, category : str) -> int:
        index : int = 1
        if category == 'bluetooth':
            index = 5
        elif category == 'speaker':
            index = 4
        elif category == 'mouse':
            index = 3
        elif category == 'keyboard':
            index = 2
        return index

    @classmethod
    def update_quantity(cls,  name : str, quantity : int):
        query : str = "update product SET quantity = quantity + %s WHERE product_name = %s"
        cls.cursor.execute("SET SQL_SAFE_UPDATES = 0")
        cls.cursor.execute(query, (quantity, name))
        cls.cursor.execute("SET SQL_SAFE_UPDATES = 1")
        cls.connection.commit()

    @classmethod
    def check_out(cls):
        cls.cursor.execute("TRUNCATE TABLE cart")
        cls.connection.commit()


Data_Access_Object.load_connector()
