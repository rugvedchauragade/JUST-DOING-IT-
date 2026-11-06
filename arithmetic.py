import math
# ARITHMETIC OPERATORS
print ("ARITHMETIC OPERATORS")
gf = 0 
gf = gf + 1 # or gf +=1 (same thing )
print(gf) # output 1 

balance = 10
balance = balance - 2 # or balance -= 2 (same thing )
print(balance) # output 8

love = 10 
love *= 10 # or love = love * 10 (same thing )
print(love) # output 100

life = 100
life /= 2 # or life = life / 2 (same thing )
print(life) # output 50.0

problem = 10
problem = problem ** 2 # or problem **= 2 (same thing )
print(problem) # output 100

remainder = 10
remainder = remainder % 3 # or remainder %= 3 (same thing )
print(remainder) # output 1

#BUILT-IN MATH FUNCTIONS
print ("BUILT-IN MATH FUNCTIONS")
x = 3.14 
y = -9.81 
z = 2.71 

result = round(x) # rounds to the nearest integer
print(result) # output 3

abs_value = abs(y) # returns the absolute value
print(abs_value) # output 9.81

power = pow(z, 2) # returns z raised to the power of 2
print(power) # output 7.3441 

maximum = max(x, y, z) # returns the maximum value
print(maximum) # output 3.14

minimum = min(x, y, z) # returns the minimum value
print(minimum) # output -9.81

#MATH MODULE FUNCTIONS ( import math at the top of the file )
print ("MATH MODULE FUNCTIONS")
print(math.pi) # output 3.141592653589793
print(math.e) # output 2.718281828459045

a = 19 
print(math.sqrt(a)) # output 4.358898943540674
# or we could also do 
#square_root = math.sqrt(a)
#print(square_root)

b = 14.6
print(math.ceil(b)) # output 15
#ceil returns the smallest integer greater than or equal to b

c = 15.8 
print(math.floor(c))# output 15
#floor returns the largest integer less than or equal to c