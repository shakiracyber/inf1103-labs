from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


supplier1 = Supplier(
    "S001",
    "ABC Electronics",
    "abc@gmail.com"
)

laptop = PhysicalProduct(
    "P001",
    "Laptop",
    1500.00,
    10,
    2.5,
    supplier1
)

antivirus = DigitalProduct(
    "D001",
    "Antivirus Software",
    59.90,
    100,
    250.0,
    supplier1
)


order1 = Order("ORD001")

print("Order created successfully!")
print("Order ID:", order1.order_id)

order1.add_order_line(laptop, 2)
order1.add_order_line(antivirus, 3)

print("Number of OrderLines:", len(order1.order_lines))
