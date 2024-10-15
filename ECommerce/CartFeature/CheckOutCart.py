from PythonUniverse.ECommerce.CartFeature.CartArea import Cart
from PythonUniverse.ECommerce.Feature.ViewAvailabilty import Feature


class Checkout:
    def __init__(self, product, cart):
        self.product = product
        self.cart = cart

    def estimate_cost(self):
        total_cost = 0

        for category in self.cart:

            for product in self.cart[category]:

                count = self.cart[category][product]
                price = self.find_price(category, product)
                total_cost += price * count

        print('\n\n\t\tTotal Cost for Your Products in the cart is : ' , total_cost)

    def find_price(self, category, brand) -> int:
        products = self.product[category]

        for prod in products:
            if prod.brand.lower() == brand:
                return prod.price

        return 0

    def check_out(self):
        print('\n\n\t\t\t\tYou Have Made a Successfull purchase ? \n\t\t\t\t\t\t!^! Thank You !^!')
        del self.cart


cart = Cart()
cart.addProducts('laptop', 'Techno', 20)
# cart.increase_quantity('laptop', 'techno', 2)
# cart.addProducts('laptop', 'Techno', 18)
# cart.remove_product('laptop', 'Techno', 3)
cart.view_cart()
check = Checkout(Feature.dictionary, cart.cart_products)
check.estimate_cost()
check.check_out()