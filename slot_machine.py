# python slot machine 
import random 


def spin_row ():
    symbols = ['🍒', '🍉', '🍋','🔔','⭐']
    results = []
    for symbol in range (3):
        results.append(random.choice(symbols))
    return results


def print_row(row):
    print("|".join(row)) # adds a bar between each character
    

def get_payout(row, bet):
    if row[0] == row[1] == row[2]: # to check if all three are same 
        if row[0] == '🍒' :
            return bet * 3
        elif row[0] == '🍉' :
            return bet * 4
        elif row[0]== '🍋' :
            return bet * 5 
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

    

def main():
    balance = 100
    print("welcome to slot machine")
    print("symbols : 🍒 🍉 🍋 🔔 ⭐")
    print("**************************")

    while balance > 0 :
        print(f"current balance : ${balance}")
        bet = input("place your bet amount : ")
        if not bet.isdigit():
            print("please enter a vaild no.")
            continue 
        bet = int(bet)
        if bet > balance :
            print("insufficient funds")

        if bet <= 0 :
            print("bet must be greater than 0")
            continue 
        balance -= bet

        row = spin_row()
        print("spinning...")
        print_row(row)

        payout = get_payout(row ,bet)
        if payout > 0 :
            print(f"you won ${payout}")
        else:
            print("sorry u lost the bet ")

        balance += payout

        play_again = input ("do uwanna spin again ?(Y/N) :  ").upper()

        if play_again != 'Y':
            break

    print(f"game over! your final balance is ${balance}")



if __name__ == '__main__':
    main()