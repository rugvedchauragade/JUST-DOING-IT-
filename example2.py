#example 2 shopping cart program 
item = input("Enter the item name: ")
price = input("Enter the item price: ")
quantity = input("Enter the item quantity: ")
price = float(price) # convert string to float
quantity = int(quantity) # convert string to integer
total = price * quantity # calculate total cost
print(f"The total cost of {quantity} {item}(s) is: ${total:.2f}") 