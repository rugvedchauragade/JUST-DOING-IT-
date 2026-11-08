# duck typing = another way of achieving polymorphism besides inheritance 
# object must be have the minimum necsessaryattributes / methods 
# "if it looks like a duck and quack like a duck , it must be a duck ."

class Animal :
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Car :
    alive = False
    def speak(self):
        print("beep")



animals  = [ Dog(), Cat()  ,Car() ]
for animal in animals:
    animal.speak() 
    print(animal.alive)