from product2 import Product
from inventory2 import Inventory

from pathlib import Path
import json

filename = Path("inventory.json")
#add a new product
def add_product(inventory):
      print ("\nAdd a new product")

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

            new_product = Product(product_id, name, price, stock)

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
    inventory = Inventory()

    inventory.add_product(Product("P001", "Laptop", 1200.0, 45))

    inventory.add_product(Product("P002", "Smartphone", 800.0, 30))

    while True:
            print("\nMenu:")
            print("1. Display all products")
            print("2. Search for a product")
            print("3. Add a new product")
            print("4. Update product stock")
            print("5. Save and exit")

            choice = input("Enter your choice (1-5): ").strip()

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
                  inventory.save_to_file("inventory.json")
                  break
            else:
                  print("Invalid choice. Please try again.")

if __name__ == "__main__":
     main()