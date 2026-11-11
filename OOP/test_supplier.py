from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

supplier1 = Supplier(
    "S001",
    "ABC Electronics",
    "abc@gmail.com"
)

physical1 = PhysicalProduct(
    "P001",
    "Laptop",
    1500.00,
    10,
    2.5,
    supplier1
)

digital1 = DigitalProduct(
    "D001",
    "Antivirus Software",
    59.90,
    100,
    250.0,
    supplier1
)

print("\nDeleting supplier1...")
del supplier1

print("\nPhysical Product Supplier after deletion:")
physical1.supplier.display_information()

print("\nDigital Product Supplier after deletion:")
digital1.supplier.display_information()