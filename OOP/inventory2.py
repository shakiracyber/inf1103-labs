from product2 import Product

class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        product_id = product.get_product_id()

        if self.search_product(product_id) is not None:
            return False
        
        self.products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        for product in self.products:
            if product.get_product_id() == product_id:
                self.products.remove(product)
                return True
        return False

    def display_inventory(self):
        print("\nCurrent Inventory:")
        print("-" *45)

        if not self.products:
            print("No products in inventory.")
        else:
            for product in self.products:
                product.display_information()
        print("-" *45)

    def search_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def find_product(self, product_id: str) -> Product | None:
        return self.search_product(product_id)

    def get_all_products(self):
        return self.products.copy()