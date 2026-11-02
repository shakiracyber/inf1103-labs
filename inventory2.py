from product2 import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        product_id = product.get_product_id()

        if self.search_product(product_id) is not None:
            return False
        
        self.products.append(product)
        return True

    def display_inventory(self):
        print("\nCurrent Inventory:")
        print("-" *45)

        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products:
                product.display_information()
        print("-" *45)

    def search_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def get_all_products(self):
        return self.products.copy()