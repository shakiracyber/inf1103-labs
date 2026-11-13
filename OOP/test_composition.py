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


print("\nOrder Details:")

for order_line in order1.order_lines:
    print("Product:", order_line.product.name)
    print("Quantity:", order_line.quantity)
    print("Subtotal:", order_line.calculate_subtotal())
    print("--------------------")

print("Order Total:", order1.calculate_total())

print("\nCreating Order 2..")

order2 = Order("ORD002")
order2.add_order_line(laptop, 1)

print("Order 2 created successfully")
print("Order 2 orderlines:", len(order2.order_lines))


print("\nChecking OrderLine identity...")

print(
    "Same OrderLine?",
    order1.order_lines[0] is order2.order_lines[0]
)

print("\nChecking Product identity...")

print(
    "Same Product?",
    order1.order_lines[0].product is order2.order_lines[0].product
)

print("\nChecking Product IDs in Order 1:")

for order_line in order1.order_lines:
    print(
        "Product:",
        order_line.product.name,
        "ID:",
        repr(order_line.product.get_product_id())
    )

print("\n Removing laptop from order 1...")

result = order1.remove_order_line("P001")

print("orderline removed successfully:", result)
print("remaining orderlines:", len(order1.order_lines))
print("updated order 1 total:", order1.calculate_total())

print("\nChecking if Laptop still exists...")
laptop.display_information()

print("\nChecking Order 2...")
print("Order 2 OrderLines:", len(order2.order_lines))
print("Order 2 Total:", order2.calculate_total())
