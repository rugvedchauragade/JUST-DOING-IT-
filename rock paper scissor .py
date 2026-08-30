import random 
options = ("rock" , "paper" , "scissor")

while True :

    player = None
    computer = random.choice(options) # to choice a random option 


    while player not in options : # while loop to so that user inputs the given option only 
        player = input("enter a choice :  ").lower()


    print(f"player : {player}")
    print(f"computer : {computer}") 

    if player == computer :
        print("its a tie ")
    elif player == "rock" and computer == "scissor"  :
        print("you win")
    elif player == "paper" and computer == "rock" :
        print("you win")
    elif player == "scissor" and computer == "paper" :
        print("you win")
    else :
        print("you loose")
    if not input("play again ?(y/n) : ").lower() == "y":
         break
print("thanks for playing")