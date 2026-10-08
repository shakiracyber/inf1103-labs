import json
from pathlib import Path

filename = Path("inventory.json")
#load inventory from file if it exists, otherwise create a new file
def load_inventory():
      if filename.exists():
            try:
                  with open(filename, "r") as file:
                        inventory = json.load(file)
                  print("inventory.json found and loaded successfully.")
                  return inventory
            except json.JSONDecodeError:
                  print("Unable to load inventory. Starting empty inventory.")
                  return []
      else:
            print("inventory.json not found. Starting empty inventory.")
            return []
#save inventory to json file
def save_inventory(inventory):
      with open(filename, "w") as file:
            json.dump(inventory, file, indent=4)
      print("Inventory saved succesfully!")

#display the products in the inventory
def display_all(inventory):
      print("\nCurrent inventory")
      print("-" * 45)

      if not inventory:
            print("No products in inventory.")
      else:
            for product in inventory:
                  print(
                        f"ID {product['id']} | "
                        f"Name: {product['name']} | "
                        f"Price: ${product['price']:.2f} | "
                        f"Stock: {product['stock']}"
                  )
            print("-" * 45)

#search
def search_product(inventory):
      print("\nSearch for a product")
      product_id = input("Enter the product ID: ").strip()

      for product in inventory:
            if product['id'] == product_id:
                  print(
                        f"ID: {product['id']} | "
                        f"Name: {product['name']} | "
                        f"Price: ${product['price']:.2f} | "
                        f"Stock: {product['stock']}"
                  )
                  return
      print("Product not found.")

#add a new product
def add_product(inventory):
      print ("\nAdd a new product")

      product_id = input("Enter the product ID: ").strip()

      for product in inventory:
            if product['id'] == product_id:
                  print("Product ID already exists. Cannot add product.")
                  return

      name = input("Enter the product name: ").strip()
      
      try:
            price = float(input("Enter the product price: "))
            stock = int(input("Enter the product stock quantity: "))

            if price < 0 or stock < 0:
                  print("Price and stock must be non-negative.")
                  return

            new_product = {
                  "id": product_id,
                  "name": name,
                  "price": price,
                  "stock": stock
            }
            inventory.append(new_product)
            print("Product added successfully.")
      except ValueError:
            print("Invalid input. Please enter valid numbers for price and stock.") 

def update_stock(inventory):
      print("\nUpdate product stock")
      product_id = input("Enter the product ID: ").strip()

      for product in inventory:
            if product['id'] == product_id:
                  try:
                        new_stock = int(input("Enter the new stock quantity: "))
                        if new_stock < 0:
                              print("Stock must be non-negative.")
                              return
                        product['stock'] = new_stock
                        print("Stock updated successfully.")
                        return
                  except ValueError:
                        print("Invalid input. Stock must be an integer.")
                        return
      print("Product not found.")

def main():
      print("="*50)
      print("Inventory management system")
      print("="*50)

      inventory = load_inventory()

      while True:
            print("\nMenu:")
            print("1. Display all products")
            print("2. Search for a product")
            print("3. Add a new product")
            print("4. Update product stock")
            print("5. Save and exit")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                  display_all(inventory)
            elif choice == "2":
                  search_product(inventory)
            elif choice == "3":
                  add_product(inventory)
            elif choice == "4":
                  update_stock(inventory)
            elif choice == "5":
                  save_inventory(inventory)
                  break
            else:
                  print("Invalid choice. Please try again.")

main()