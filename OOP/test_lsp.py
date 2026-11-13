from product2 import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfillment_info())


supplier1 = Supplier(
    supplier_id="S001",
    name="Tech Supplier",
    contact_email="tech@example.com"
)

laptop = PhysicalProduct(
    product_id="P001",
    name="Laptop",
    price=1500.0,
    stock=10,
    weight=2.5,
    supplier=supplier1
)

antivirus = DigitalProduct(
    product_id= "D001",
    name ="Antivirus Software",
    price=59.90,
    stock=50,
    download_size=500.0,
    supplier=supplier1
)
print("=== Physical Product ===")
show_product_details(laptop)

print("\n=== Digital Product ===")
show_product_details(antivirus)