C_RESET = "\x1b[0m"
C_TEAL = "\x1b[36m"
C_BLUE = "\x1b[34m"
C_GREEN = "\x1b[32m"
C_YELLOW = "\x1b[33m"
C_RED = "\x1b[31m"

ACCOUNTS = [
    {"card_code": "k", "name": "Ken Kaneki",
        "title": "Midnight Account", "pin": 1234, "balance": 50000},
    {"card_code": "s", "name": "Sasuke Uchiha",
        "title": "Storm Account", "pin": 5678, "balance": 100000},
    {"card_code": "i", "name": "Itachi Uchiha",
        "title": "Shadow Account", "pin": 9123, "balance": 60000},
    {"card_code": "l", "name": "Light Yagami",
        "title": "Nova Account", "pin": 8123, "balance": 40000},
]


def print_bar():
    print("+----------------------------------------------------------+")


def print_header():
    print_bar()
    print(f"{C_TEAL}|                     ANTEIKU ATM v2                       |{C_RESET}")
    print(f"{C_BLUE}|                Cool Neon Terminal Edition                |{C_RESET}")
    print_bar()
    print(" Card codes available: k / s / i / l\n")


def find_account_by_code(code):
    for account in ACCOUNTS:
        if account["card_code"] == code:
            return account
    return None


def validate_pin(expected_pin):
    for attempt in range(1, 4):
        try:
            pin = int(input(f" Enter 4-digit PIN (attempt {attempt}/3): "))
        except ValueError:
            return False

        if pin == expected_pin:
            return True

        print(f"{C_RED} PIN mismatch.{C_RESET}")

    return False


def print_receipt(account, withdrawn, remaining):
    print()
    print_bar()
    print(f"{C_GREEN}|                    TRANSACTION RECEIPT                   |{C_RESET}")
    print_bar()
    print(f" User        : {account['name']}")
    print(f" Profile     : {account['title']}")
    print(f" Withdrawn   : {withdrawn}")
    print(f" Remaining   : {remaining}")
    print_bar()


def run_session(account):
    print(f"{C_GREEN}\n Welcome, {account['name']}{C_RESET}")
    print(f" Profile: {account['title']}")
    print_bar()
    print(" 1) Withdraw Cash")
    print(" 2) Check Balance")
    print_bar()

    try:
        choice = int(input(" Choose action: "))
    except ValueError:
        print(f"{C_RED} Invalid action input.{C_RESET}")
        return

    if not validate_pin(account["pin"]):
        print(f"{C_RED} Access blocked for this session.{C_RESET}")
        return

    if choice == 1:
        try:
            amount = int(input(" Enter amount to withdraw: "))
        except ValueError:
            print(f"{C_RED} Invalid amount input.{C_RESET}")
            return

        if amount <= 0:
            print(f"{C_RED} Amount must be greater than zero.{C_RESET}")
            return

        if amount > account["balance"]:
            print(f"{C_RED} Insufficient funds.{C_RESET}")
            return

        print(f"{C_GREEN}\n Cash ready. Please collect: {amount}{C_RESET}")
        print_receipt(account, amount, account["balance"] - amount)
    elif choice == 2:
        print(f"{C_YELLOW}\n Current Balance: {account['balance']}{C_RESET}")
    else:
        print(f"{C_RED} Unknown menu action.{C_RESET}")


def main():
    print_header()
    card_code = input(" Insert card code: ").strip().lower()

    if not card_code:
        print(f"{C_RED} Failed to read card.{C_RESET}")
        return

    account = find_account_by_code(card_code[0])
    if account is None:
        print(f"{C_RED} Unknown card code. Access denied.{C_RESET}")
        print_bar()
        return

    run_session(account)

    print()
    print_bar()
    print(f"{C_TEAL} Session complete. Thanks for using ANTEIKU ATM.{C_RESET}")
    print_bar()


if __name__ == "__main__":
    main()
