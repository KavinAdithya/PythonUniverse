from PythonUniverse.ECommerce.Feature.ViewAvailabilty import Feature



class Cart:

    def __init__(self):
        self.cart_products = {}
        self.products = Feature.dictionary

    def addProducts(self, category, brand, quantity):
        category = category.lower()
        brand = brand.lower()

        if Feature.isValidCategory(category):
            raise ValueError('\t\tThe Product Category Currently Unavailable...')

        if self.isNotAvailableProduct(category, brand, quantity):
            raise ValueError('\t\tProduct Currently Not Available...')

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

        self.quantity_change(category, brand, -quantity)

    def isNotAvailableProduct(self, category, brand, quantity) -> bool:
        product = self.products[category]
        brand = brand.lower()

        for prod in product:
            if prod.brand.lower() == brand and prod.quantity >= quantity:
                return False

        return True

    def view_cart(self):

        for category in self.cart_products:

            products = self.cart_products[category]
            print('\t\tCategory : ' + category)

            for brand in products:
                self.print_object(brand, category)
                print ('\t\t | Cart Quantity : ' , products[brand])
                print('\t\t ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~')

    def quantity_change(self, category, brand, quantity):
        products = self.products[category]

        for product in products:
            if product.brand.lower() == brand:
                product.quantity += quantity
                break

    def remove_product(self, category, brand, quantity):
        category = category.lower()

        if not category in self.cart_products:
            raise ValueError('\t\tThe Product Category Unavailable in your cart...')

        products = self.cart_products[category]
        brand = brand.lower()

        if not brand in products:
            raise ValueError('\t\tProduct Currently Not Available...')

        count = products[brand]

        if count < quantity:
            raise ValueError('\t\tSelecting Extra products which is not present there...')

        products[brand] = count - quantity
        self.quantity_change(category, brand, quantity)

        if count == 0:
            del products[brand]

    def print_object(self, brand, category):
        objects = self.products[category]

        for obj in objects:
            if obj.brand.lower() == brand:
                print(obj)

Feature.default_load()