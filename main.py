import random

MAX_LINES = 3
MAX_BET = 2500
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# below is for the multiplier
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# set up so if we bet on 1 line it will only bet on the top, 2 lines: 1st and 2nd, 3rd line is all three
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            # added the 1 because it's indexed and we want to return 1, 2, 3
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        '''By setting it up as symbol, symbol_count we can access the key and value, which the .items also allows us to access the key and value
        Our symbol is A, B, C and our symbol_count is 2, 4, 6, 8'''
        for _ in range(symbol_count):
            # we used an underscore when we don't care about the index nor using an extra variable
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        ''' we added the : within the [] to make a copy of a list instead of only making a reference
        We want to make a copy so that as we take away simbles from our slot, it doesn't delete indefinitely after a turn'''
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
            # We will run through each column and will delete a symbol from the current_symbols list so it is not picked again
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row], end="")
            
        print()

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


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Sorry you don't have enough to be that amount, your current balance is: {balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} line(s). Your total bet is {total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", *winning_lines)
    # * is a splat variable which will allow us to say which lines we won on
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        else:
            balance += spin(balance)
        
    print(f"You left with ${balance}")

main()