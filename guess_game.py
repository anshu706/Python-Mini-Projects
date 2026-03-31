C_RESET = "\x1b[0m"
C_CYAN = "\x1b[36m"
C_GREEN = "\x1b[32m"
C_RED = "\x1b[31m"


def main():
    secret_number = 5
    guess_number = 0
    guess_limit = 3

    print(f"{C_CYAN}======================================{C_RESET}")
    print(f"{C_CYAN}         GUESS THE NUMBER GAME{C_RESET}")
    print(f"{C_CYAN}======================================{C_RESET}")
    print(f"You have {guess_limit} attempts.\n")

    for i in range(1, guess_limit + 1):
        try:
            guess_number = int(
                input(f"Attempt {i}/{guess_limit} -> Enter guess: "))
        except ValueError:
            guess_number = None

        if guess_number == secret_number:
            print(f"{C_GREEN}\nPerfect guess. You won!{C_RESET}")
            break
        else:
            print(f"{C_RED}Not this one.{C_RESET}")

    if guess_number != secret_number:
        print(f"{C_RED}\nYou lost. Secret number was {secret_number}.{C_RESET}")


if __name__ == "__main__":
    main()
