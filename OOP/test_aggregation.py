from inventory2 import Inventory
from supplier import Supplier
from physical_product import PhysicalProduct

inventory_a = Inventory()
inventory_b = Inventory()

supplier1 = Supplier(
    "S001",
    "ABC Electronics",
    "abc@gmail.com"
)

laptop= PhysicalProduct(
    "P001",
    "Laptop",
    1500.00,
    10,
    2.5,
    supplier1
)

print ("\nProduct created successfully")
laptop.display_information()

print("\nAdding laptop to Inventory A")

result = inventory_a.add_product(laptop)

print("Product added successfully:", result)

inventory_a.display_inventory()

print("\nRemoving laptop from Inventory A")

result = inventory_a.remove_product("P001")

print("Product removed successfully:", result)

inventory_a.display_inventory()

print("\nChecking if laptop still exists...")

laptop.display_information()

print("\nTransferring laptop to Inventory B")

result = inventory_b.add_product(laptop)

print("Product added to Inventory B:", result)

inventory_b.display_inventory()
