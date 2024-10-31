from PythonUniverse.ECommerce.Exceptions.ProductMissingException import ProductMissingException
from PythonUniverse.ECommerce.Feature.ViewAvailabilty import Feature

class Cart:
    def __init__(self, cart : dict):
        self.cart_products : dict = cart
        self.products : dict  = Feature.dictionary

    def addProducts(self, category, model, quantity):
        category = category.lower()
        model = model.lower()

        if Feature.isValidCategory(category):
            raise ProductMissingException('\n\t\t The Product Category Currently Unavailable...')

        if self.__isNotAvailableProduct(category, model, quantity):
            raise ProductMissingException('\n\t\t Invalid Model/Brand Given...')

        if category in self.cart_products:
            brands = self.cart_products[category]

            if model in brands:
                avail = brands[model] + quantity
                brands[model] = avail
            else:
                brands[model] = quantity
        else:
            self.cart_products[category] = {}
            self.cart_products[category][model] = quantity

        self.__quantity_change(category, model, -quantity)
        print('\n\t\t Product Has been Successfully added to the cart...')

    def __isNotAvailableProduct(self, category, model, quantity) -> bool:
        product = self.products[category]
        model = model.lower()

        for prod in product:
            if prod.name.lower() == model and prod.quantity >= quantity:
                return False
            if prod.name.lower() == model and not prod.quantity >= quantity:
                raise ProductMissingException('\n\t\t Product Quantity is too High compared to availability...')

        return True

    def view_cart(self):

        if len(self.cart_products) == 0:
            print('\n\t\t No products Available in your Cart..')
            return

        for category in self.cart_products:

            products = self.cart_products[category]
            print('\n\t\t Category : ' + category.upper())

            for model in products:
                self.__print_object(model, category)
                print ('\t\t | Cart Quantity : ' , products[model])
                print('\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')

    def __quantity_change(self, category, model, quantity):
        products = self.products[category]

        for product in products:
            if product.name.lower() == model:
                product.quantity += quantity
                break

    def remove_product(self, category, model, quantity):
        category = category.lower()

        if not category in self.cart_products:
            raise ProductMissingException('\n\t\t The Product Category Unavailable in your cart...')

        products = self.cart_products[category]
        model = model.lower()

        if not model in products:
            raise ProductMissingException('\n\t\t Product Currently Not Available in your cart ...')

        count = products[model]

        if count < quantity:
            raise ProductMissingException('\n\t\t Selecting Extra products which is not present there...')

        products[model] = count - quantity
        self.__quantity_change(category, model, quantity)

        if count == 0:
            del products[model]
        print('\n\t\t Product Has been Successfully Removed from the cart...')

    def __print_object(self, model, category):
        objects = self.products[category]
        for obj in objects:
            if obj.name.lower() == model.lower():
                print(obj)