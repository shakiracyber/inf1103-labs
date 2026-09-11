inventory = 0
failed_enteries = 0

while True:
        stock = (input("Enter the stock quantity (or type 'quit'): "))
        if stock == 'quit':
               print("Exiting the program.")
               print ("Total Units Processed:" , inventory)
               print ("Number of Failed/Rejected Entries:" , failed_enteries)
               break
        elif stock.startswith("-") and stock[1:].isdigit():
              print("Invalid input. Please enter a positive integer.")
              failed_enteries +=1
        elif not stock.isdigit():
            print("Invalid input. Please enter a valid integer.")
            failed_enteries +=1
        else:
              stock = int(stock)
              inventory += stock
              if inventory > 500 :
                    print ("Inventory exceeds 500 units.")
                    failed_enteries +=1
                    break
