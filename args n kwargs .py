#*args = allows you to pass multiple non key arguments 
#**kwargs = aloows u to pass multiple non - key word arguments 
#     * unpacking operator 


#def add(a,b):
    #
#printadd(1,2 ,3))# the add takes two positional argument but we gave it three 
# so the code will give error 

def addition(*args): # adds the argument given into a tuple 
    for arg in args :
        total = 0
        total += arg 
    return total 

print(addition(1,2))

# we can change the name of *args to anything but with * in start

# name display program 
def display_name(*args):
    for arg in args:
        print( arg , end = " ")

display_name("Mr", "rugved", "shrikant", "chauragade" ) # pass any amount of arguments 
print()
## now moving too **kwargs 
# lets understand using an example 
def print_address (**kwargs): # adds tese arguments into dictionar (key value pair )
    for key , value  in kwargs.items() :
        print(f"{key} : {value}")   

print_address(street = "katol rd" , area = "gittikhadan" , city ="nagpur")
print()

# using both *args and **kwargs in a function
def shipping_label(*args , **kwargs): # args first then kwargs always 
    for arg in args :
        print(arg , end = " ")
    print()

    print(f"{kwargs.get('street')}" ) 
    print(f"{kwargs.get('area')} , {kwargs.get('city')} , {kwargs.get('zip')}")


shipping_label("Mr" , "rugved" , "chauragade" , street = "katol rd" , area = "gittikhadan" , city ="nagpur " , zip = 440013)