from physical_product import PhysicalProduct
from digital_product import DigitalProduct

laptop = PhysicalProduct ("P001", "Laptop", 1200, 5, 2.5)
game = DigitalProduct ("D001", "Minecraft",35, 10, 500)

laptop.display_information()
print(laptop.get_fulfillment_info())
print(f"Shipping Cost: ${laptop.calculate_shipping_cost():.2f}")
print(game.get_fulfillment_info())