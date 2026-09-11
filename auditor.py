inventory = 0
failed_enteries = 0

while True:
        stock = str(input("Enter the stock quantity (or type 'quit'): "))
        if stock.isdigit():
                stock = int(stock)
                inventory += stock
        elif stock < 0:
            print("Invalid input. Please enter a positive integer.")
            failed_enteries +=1
        elif stock > 500:
            print("Stock quantity exceeds maximum 500 units. Please enter a valid quantity number")
            failed_enteries +=1
        else:
                print("Exiting the program.")
                print ("Total Units Processed:" , inventory)
                print ("Number of Failed/Rejected Entries:" , failed_enteries)