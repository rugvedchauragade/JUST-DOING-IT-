  # concession stand program

menu = {"pizza" : 5.00 ,
        "chips" : 1.00 ,
        "popcorn" : 4.00 ,
        "hotdog" : 3.00 ,
        "soda" : 2.00 ,
        "fries" : 4.00 ,
        "sandwich" : 5.00}
cart = []
total = 0
print("------------ menu -------------")
for key , value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("------------------------------")

while True :
    food = input("enter the food you want to buy (Q to quit): ").lower()# parenthesis are important
    if food == "q" :
        break
    elif menu.get(food) is not None :
        cart.append(food)

for food in cart :
    total = total + menu.get(food)
    print(food , end = " ")

print(f"total is : ${total:.2f}")