from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if quantity >= 0:
            self.stock = quantity
            print(f"Stock updated successfully")
        else:
            print("Stock must be non-negative.")
       
    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.name} | "
            f"Price: ${self.price:.2f} | "
            f"Stock: {self.stock}"
        )
    def get_product_id(self):
            return self.__product_id

    def to_dict(self):
         return {
            "id": self.__product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
         }

    @abstractmethod
    def get_fulfillment_info(self):
        pass