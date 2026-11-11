from product2 import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size, supplier: Supplier):
        super().__init__(product_id, name, price, stock,supplier)
        self.download_size = download_size
    
    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.download_size} MB")

    def get_fulfillment_info(self):
        return " This product is available for digital download."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.download_size
        return data