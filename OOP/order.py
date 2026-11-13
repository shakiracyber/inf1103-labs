from order_line import OrderLine
from product2 import Product


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine (product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total

  
    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self.order_lines:
            print("Checking:", repr(order_line.product.get_product_id()))
            print("Looking for:", repr(product_id))

            if order_line.product.get_product_id() == product_id:
                print("Match found!")
                self.order_lines.remove(order_line)
                return True

        return False

