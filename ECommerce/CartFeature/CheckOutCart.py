class Checkout:
    def __init__(self, product, cart):
        self.product = product
        self.cart = cart

    def estimate_cost(self):
        total_cost = 0

        for category in self.cart:

            for product in self.cart[category]:

                count = self.cart[category][product]
                price = self.__find_price(category, product)
                total_cost += price * count

        print('\n\n\t\t Total Cost for Your Products in the cart is : ' , total_cost)

    def __find_price(self, category, brand) -> int:
        products = self.product[category]

        for prod in products:
            if prod.brand.lower() == brand:
                return prod.price

        return 0

    def check_out(self):
        print('\n\n\t\t\t\t You Have Made a Successfully purchased ? \n\t\t\t\t\t\t!^! Thank You !^!')
        del self.cart