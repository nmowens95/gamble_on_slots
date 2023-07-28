MAX_LINES = 3

def deposit():
    while True:
        amount = input("The minimum buy is $50, how much would you like to deposit? $")
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

def main():
    balance = deposit()
    number_of_lines = get_number_of_lines()

main()