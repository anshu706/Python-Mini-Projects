import random

C_RESET = "\x1b[0m"
C_MAGENTA = "\x1b[35m"
C_GREEN = "\x1b[32m"
C_RED = "\x1b[31m"
C_YELLOW = "\x1b[33m"


def print_rules():
    print(f"{C_MAGENTA}========================================================{C_RESET}")
    print(f"{C_MAGENTA}                     LUCKY CASINO{C_RESET}")
    print(f"{C_MAGENTA}========================================================{C_RESET}")
    print("1. Guess a number from 1 to 10.")
    print("2. Correct guess wins 10x of your bet.")
    print("3. Wrong guess loses your bet amount.")
    print("========================================================\n")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{C_RED}Please enter a valid number.{C_RESET}")


def main():
    again = 1

    print_rules()

    name = input("Player name: ").strip()
    balance = read_int("Deposit amount: $")

    while again == 1 and balance > 0:
        print(f"\n{C_YELLOW}Current Balance: ${balance}{C_RESET}")
        bet = read_int("Enter bet amount: $")

        if bet <= 0 or bet > balance:
            print(f"{C_RED}Invalid bet. Try again.{C_RESET}")
            continue

        guess = read_int("Guess a number (1-10): ")
        if guess < 1 or guess > 10:
            print(f"{C_RED}Guess must be between 1 and 10.{C_RESET}")
            continue

        lucky_number = random.randint(1, 10)

        if guess == lucky_number:
            win = bet * 10
            balance += win
            print(
                f"{C_GREEN}Amazing {name}! Lucky number was {lucky_number}. You won ${win}{C_RESET}")
        else:
            balance -= bet
            print(
                f"{C_RED}No luck this time. Lucky number was {lucky_number}. You lost ${bet}{C_RESET}")

        if balance <= 0:
            print(f"{C_RED}\nBalance reached $0. Game over.{C_RESET}")
            break

        again = read_int("Play another round? (1 = Yes, 0 = No): ")

    print(f"{C_MAGENTA}\nThanks for playing, {name}. Final balance: ${balance}{C_RESET}")


if __name__ == "__main__":
    main()
