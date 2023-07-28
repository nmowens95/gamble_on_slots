import random

MAX_LINES = 3
MAX_BET = 500
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        '''by setting it up as symbol, symbol_count we can access the key and value, which the .items also allows us to access the key and value
        Our symbol is A, B, C and our symbol_count is 2, 4, 6, 8'''
        for _ in range(symbol_count):
            #we used an underscore when we don't care about the iteration or want an unused variable
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        for row in range(rows):
            value = random.choice(all_symbols)


def deposit():
    while True:
        amount = input("The minimum deposit is $50, how much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 50:
                print(f"Your starting balance is now {amount}")
                break
            else:
                print("Please enter a valid number amount of $50 or greater")
        else:
            print("Please enter a valid number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet? (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                print(f"{lines} it is!")
                break
            else:
                print("Please choose: 1-" + str(MAX_LINES) +"")
        else:
            print("Please enter a valid number")
    return lines

def get_bet():
    while True:
        amount = input(f"How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Sorry try a bet within {MIN_BET} and {MAX_BET} or within your current account balance.")
        else:
            print("Please enter a valid amount")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Sorry you don't have enough to be that amount, your current balance is: {balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} line(s). Your total bet is {total_bet}.")

main()