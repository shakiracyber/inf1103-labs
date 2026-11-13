from product2 import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.weight = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight} kg")

    def get_fulfillment_info(self) -> str:
        return " This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.weight * 5

    def to_dict(self) -> dict[str, str | float | int]:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.weight
        return data