from product2 import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock,supplier)
        self.download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.download_size} MB")

    def get_fulfillment_info(self) -> str:
        return " This product is available for digital download."

    def to_dict(self) -> dict[str, str | float | int]:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.download_size
        return data