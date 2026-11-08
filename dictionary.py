#dictionary = a collecion of {key: value } pairs 
#  ordered and changeable no duplicates 

# examples 
capitals = {"india" : "delhi" , "usa" : "washington"}

# for every method are use of dictionary we could use
# print(help(capitals))

# to get the value of the key 
# we use 
# print(capitals.get()) output error 
print(capitals.get("india"))# output delhi
print(capitals.get("usa"))# output washington
print(capitals.get("japan"))# output none 
# output is none caua=se there is no key as japan 

# we could aslo check if a key is there or not 
# using if else 
if capitals.get("japan") :
    print("the capital exists ")
else :
    print("the capital does not exists ")

# if we want to add or update a  key value pair we use 
capitals.update({"germany" : "berlin" }) # the will be added to capitals 

# we could also update existing one using 
capitals.update({"usa" : "washington dc"})

# we could also remove using 
capitals.pop("india")

##capitals.popitem() # will remove the latest key value pair

# to clear the dictionary we use .clear()
# capitals.clear()

print(capitals)

# to print the keys of a dictionary we use 
keys = capitals.keys()
print(keys)# output usa , germany

# or we could aslo use 
for key in keys :
    print(key)

# to print the values of a dictionary we use 
values = capitals.values()
print(values)

# we could also use 
for value in values :
    print(value)

# to print every item we use 
# items return an object that resembles an 2d list of tuples
# items = [(),(),()]
items = capitals.items()
for key , value in items :
    print(f"{key}:{value}")
