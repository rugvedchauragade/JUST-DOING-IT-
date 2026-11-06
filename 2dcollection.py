# 2D COLLECTIONS
# 2D LISTS IS JUST LIST MADE UP OF LISTS 
# 2dlist = [list1 , list2 , list3]

fruits = ["apple" , "orange" , "banana", "coconut"]
vegetables = ["potato" , "onion" , "tomato"]
meat = [ "chicken" , "fish" , "turkey"]

groceries = [fruits , vegetables , meat ]

print(groceries)
print(groceries[0])# output ['apple', 'orange', 'banana', 'coconut']
# it will take fruitsas zero index and print all the elements of it 

print(groceries[0][0]) # this means row zero coloumn zero
# output = apple 

print(groceries[0][2])# output = banana 

print (groceries [1][2]) # output = tomato

for collection in groceries :
    
    for food in collection :
        print (food , end =" ")

print()# will print every list vertically
