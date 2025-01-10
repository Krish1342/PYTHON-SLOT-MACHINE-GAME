import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_values = {"A": 5, "B": 4, "C": 3, "D": 2}


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

    return winnings,winning_lines


def get_slot_machine_spint(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        curr_symobols = all_symbols[
            :
        ]  # : - slice operator to copy all_symbols into curr_symbols
        for _ in range(rows):
            value = random.choice(curr_symobols)
            curr_symobols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid Number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(
                f"Insufficient funds. Please deposit more money.Your current balance is ${balance}."
            )
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines.Total bet is equal to: ${total_bet}"
    )

    slots = get_slot_machine_spint(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"Your winnings are: ${winnings}.")
    print(f"You won on lines", *winning_lines) 
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Please enter to spin (q to quit)")
        if answer == "q":
            print("Thank you for playing!")
            break
        balance += spin(balance)
        
    print(f"Current Balance ${balance}")
            
        
    
    

main()