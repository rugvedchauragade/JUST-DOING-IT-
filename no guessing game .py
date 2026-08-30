import random
low = 1
high = 100
answer = random.randint(low , high)
guesses = 0
is_running = True
print ("number guesing game")
print (f"select a no. between {low} and {high}")
while is_running:
   guess = input("enter your guess : ")

   if guess.isdigit():
       guess = int(guess)
       guesses += 1 
       if guess < low or guess > high :
          print("that no. is out of range")
          print(f"select anumber between {low} & {high}")

       elif guess < answer :
          print("too low ,try again")

       elif guess > answer :
          print("too high ,try again")

       else :
          print(f"correct answer ")
          print(f"no. of guesses : {guesses}")          
          is_running = False

          
   else :
      print("invalid guess")
      print(f"select anumber between {low} & {high}")

 
 