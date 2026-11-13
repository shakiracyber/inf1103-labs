from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.supplier: Supplier = supplier

    def update_stock(self, quantity) -> None:
        if quantity >= 0:
            self.stock = quantity
            print(f"Stock updated successfully")
        else:
            print("Stock must be non-negative.")
       
    def display_information(self) -> None:
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.name} | "
            f"Price: ${self.price:.2f} | "
            f"Stock: {self.stock}"
        )
    def get_product_id(self) -> str:
            return self.__product_id

    def to_dict(self)-> dict[str, str | float | int]:
         return {
            "id": self.__product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
         }

    @abstractmethod
    def get_fulfillment_info(self) -> str:
        pass