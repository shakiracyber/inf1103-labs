
def get_valid_input():
      failed_attempts = 0
      while True:
            stock = (input("Enter the stock quantity (or type 'quit'): "))
            if stock == 'quit':
                 return "quit", failed_attempts
            elif stock.startswith("-") and stock[1:].isdigit():
                  print("Invalid input. Please enter a positive integer.")
                  failed_attempts +=1
            elif not stock.isdigit():
                  print("Invalid input. Please enter a valid integer.")
                  failed_attempts +=1
            else:
                  return int(stock) , failed_attempts

def process_delivery(current_total, new_value):
        new_total = current_total + new_value
        return new_total

def calculate_tax(amount):
      tax = amount * 0.10
      return tax
def generate_report(new_value, failed_entries):
      print("Total deliveries processed:", new_value)
      print ("Number of failed/rejected entries:", failed_entries)

inventory = 0
deliveries_processed = 0
failed_enteries = 0

while True:
      stock, failed_attempts = get_valid_input()
      failed_enteries += failed_attempts
      if stock == "quit":
            generate_report(deliveries_processed, failed_enteries)
            break
      else:
            inventory = process_delivery(inventory,stock)
            tax =calculate_tax(stock)
            print ("Tax:", tax)
            deliveries_processed += 1
