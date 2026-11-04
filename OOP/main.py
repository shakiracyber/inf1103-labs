from pathlib import Path
import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory2 import Inventory

filename = Path("inventory.json")
#load inventory from file if it exists, otherwise create a new file
def load_inventory():
    inventory = Inventory()

    if filename.exists():
        try:
            with open(filename, "r") as file:
                inventory_data = json.load(file)

            for product_data in inventory_data:
              product_type = product_data.get("type")
              if product_type == "physical":
                    product = PhysicalProduct(
                          product_data["id"],
                          product_data["name"],
                          product_data["price"],
                          product_data["stock"],
                          product_data["weight"]
                          )
              elif product_type == "digital":
                    product = DigitalProduct(
                          product_data["id"],
                          product_data["name"],
                          product_data["price"],
                          product_data["stock"],
                          product_data["download_size"]
                          )
              else:
                    print("Unknown product type. Skipping record.")
                    continue
              inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Unable to load inventory.")

    else:
        print("inventory.json not found.")

    return inventory
#save inventory to json file
def save_inventory(inventory):
      products = inventory.get_all_products()
      inventory_data = []

      for product in products:
            inventory_data.append(product.to_dict())
      with open(filename, "w") as file:
            json.dump(inventory_data, file, indent=4)

      print("Inventory saved successfully!")
    
#add a new product
def add_product(inventory):
      print ("\nAdd a new product")
      print("\nSelect product type:")
      print("1. Physical Product")
      print("2. Digital Product")

      product_type = input("Enter your choice (1 or 2): ").strip()
      if product_type not in ("1","2"):
            print("Invalid choice. Please select 1 or 2.")
            return

      product_id = input("Enter the product ID: ").strip()

      if not product_id:
            print("Product ID cannot be empty.")
            return
      

      name = input("Enter the product name: ").strip()

      if not name:
            print("Product name cannot be empty.")
            return
      
      try:
            price = float(input("Enter the product price: "))
            stock = int(input("Enter the product stock quantity: "))

            if price < 0 or stock < 0:
                  print("Price and stock must be non-negative.")
                  return

            if product_type == "1":
                 weight = float(input("Enter weight (kg):"))
                 
                 if weight < 0:
                  print("Weight cannot be negative.")
                  return
                 
                 new_product = PhysicalProduct( product_id, name, price, stock, weight)
            elif product_type == "2":
                 download_size = float(input("Enter download size (MB): "))

                 if download_size < 0:
                      print("Download size cannot be negative.")
                      return
                 
                 new_product = DigitalProduct( product_id, name, price, stock, download_size)
                 
      
            if inventory.add_product(new_product):
                  print("Product added successfully.")  
            else:
                    print("Product ID already exists. Cannot add product.")
      except ValueError:
            print("Invalid input. Please enter valid numbers for price and stock.") 

def update_product_stock(inventory):
      print("\nUpdate product stock")
      product_id = input("Enter the product ID: ").strip()
      product = inventory.search_product(product_id)
      if product is not None:
        try:
          new_stock = int(input("Enter the new stock quantity: "))
          product.update_stock(new_stock)
        except ValueError:
          print("Invalid input. Stock must be an integer.")
      else:
           print(f"Product with ID {product_id} not found.")

def main():
    inventory = load_inventory()
    while True:
            print("\nMenu:")
            print("1. Display all products")
            print("2. Search for a product")
            print("3. Add a new product")
            print("4. Update product stock")
            print("5. Save inventory")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                  inventory.display_inventory()
            elif choice == "2":
                  print("\nSearch for a product")
                  product_id = input("Enter the product ID: ").strip()

                  product = inventory.search_product(product_id)

                  if product is not None:
                        product.display_information()
                  else:
                        print(f"Product with ID {product_id} not found.")
            elif choice == "3":
                  add_product(inventory)
            elif choice == "4":
                  update_product_stock(inventory)
            elif choice == "5":
                  save_inventory(inventory)
            elif choice == "6":
                    print("Exiting the program.")
                    break
            else:
                  print("Invalid choice. Please try again.")

if __name__ == "__main__":
     main()