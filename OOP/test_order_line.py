from supplier import Supplier
from physical_product import PhysicalProduct
from order_line import OrderLine

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

order_line1 = OrderLine(laptop, 2)
subtotal = order_line1.calculate_subtotal()
print("Subtotal:", subtotal)

