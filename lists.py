#collection = single " variable " to store multiple values 
# list = [] ordered and chageable . duplicate ok
# set = {} unordered and immutable . but add / remove ok . no duplicate 
# tuple = () orderd and unchangeable . duplicate ok . faster 

fruit = ["apple" , "orange" , "banana" , "coconut"]
# list is ordered and we changabele 
print (fruit[0])# output apple
print (fruit[1])# output orange 
# print ( fruit[4])# output error 
print(fruit [0:3])
print(fruit [::-1]) 

for x in fruit :
    print(x)
# if we need a list and help of methods of addition ,replace 
# we can use 
# print(help(fruit))
print (len(fruit))# output 4
fruit[0] = "pineapple" # pinaplle will replace apple 
print(fruit[0])
print(fruit) # list [] can be change after once created 

# for addition
fruit.append("apple")# adds apple to the end of the list 
print (fruit)

# to remove 
fruit.remove("orange")
print(fruit)

# to insert at some specific location
fruit.insert(0 , "grapes")# adds grape to 1st position
print(fruit)

# to sort we use sort()
fruit.sort()
print(fruit)# will sort it in alphabetical order 

# for reverse we use 
fruit.reverse()
print(fruit)

# to clear every single element we use .clear()
# fruit.clear() 
# this will return []

# to find the index of an element we use .index()
print(fruit.index("apple"))

# u can count how many values there are in a list 
# cause duplicate are ok in list 
print(fruit.count("apple"))

# to find something if something is in the list or nots  we can use 
print("pineapple" in fruit  ) # output true 



#########
