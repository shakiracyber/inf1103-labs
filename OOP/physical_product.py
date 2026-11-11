from product2 import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight} kg")

    def get_fulfillment_info(self):
        return " This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.weight * 5

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.weight
        return data