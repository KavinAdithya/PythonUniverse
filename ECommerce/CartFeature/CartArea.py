from PythonUniverse.ECommerce.Exceptions.ProductMissingException import ProductMissingException
from PythonUniverse.ECommerce.Feature.ViewAvailabilty import Feature

class Cart:
    def __init__(self):
        self.cart_products = {}
        self.products = Feature.dictionary

    def addProducts(self, category, brand, quantity):
        category = category.lower()
        brand = brand.lower()

        if Feature.isValidCategory(category):
            raise ProductMissingException('\n\t\t The Product Category Currently Unavailable...')

        if self.__isNotAvailableProduct(category, brand, quantity):
            raise ProductMissingException('\n\t\t Invalid Model/Brand Given...')

        if category in self.cart_products:
            brands = self.cart_products[category]

            if brand in brands:
                avail = brands[brand] + quantity
                brands[brand] = avail
            else:
                brands[brand] = quantity
        else:
            self.cart_products[category] = {}
            self.cart_products[category][brand] = quantity

        self.__quantity_change(category, brand, -quantity)
        print('\n\t\t Product Has been Successfully added to the cart...')

    def __isNotAvailableProduct(self, category, brand, quantity) -> bool:
        product = self.products[category]
        brand = brand.lower()

        for prod in product:
            if prod.brand.lower() == brand and prod.quantity >= quantity:
                return False
            if prod.brand.lower() == brand and not prod.quantity >= quantity:
                raise ProductMissingException('\n\t\t Product Quantity is too High compared to availability...')

        return True

    def view_cart(self):

        for category in self.cart_products:

            products = self.cart_products[category]
            print('\n\t\t Category : ' + category.upper())

            for brand in products:
                self.__print_object(brand, category)
                print ('\t\t | Cart Quantity : ' , products[brand])
                print('\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')

    def __quantity_change(self, category, brand, quantity):
        products = self.products[category]

        for product in products:
            if product.brand.lower() == brand:
                product.quantity += quantity
                break

    def remove_product(self, category, brand, quantity):
        category = category.lower()

        if not category in self.cart_products:
            raise ProductMissingException('\n\t\t The Product Category Unavailable in your cart...')

        products = self.cart_products[category]
        brand = brand.lower()

        if not brand in products:
            raise ProductMissingException('\n\t\t Product Currently Not Available in your cart ...')

        count = products[brand]

        if count < quantity:
            raise ProductMissingException('\n\t\t Selecting Extra products which is not present there...')

        products[brand] = count - quantity
        self.__quantity_change(category, brand, quantity)

        if count == 0:
            del products[brand]
        print('\n\t\t Product Has been Successfully Removed from the cart...')

    def __print_object(self, brand, category):
        objects = self.products[category]

        for obj in objects:
            if obj.brand.lower() == brand:
                print(obj)

Feature.default_load()