#include <stdio.h>

#define C_RESET "\x1b[0m"
#define C_TEAL "\x1b[36m"
#define C_BLUE "\x1b[34m"
#define C_GREEN "\x1b[32m"
#define C_YELLOW "\x1b[33m"
#define C_RED "\x1b[31m"

typedef struct
{
    char card_code;
    const char *name;
    const char *title;
    int pin;
    int balance;
} Account;

static const Account accounts[] = {
    {'k', "Ken Kaneki", "Midnight Account", 1234, 50000},
    {'s', "Sasuke Uchiha", "Storm Account", 5678, 100000},
    {'i', "Itachi Uchiha", "Shadow Account", 9123, 60000},
    {'l', "Light Yagami", "Nova Account", 8123, 40000}};

static const int account_count = (int)(sizeof(accounts) / sizeof(accounts[0]));

static void print_bar(void)
{
    printf("+----------------------------------------------------------+\n");
}

static void print_header(void)
{
    print_bar();
    printf(C_TEAL "|                     ANTEIKU ATM v2                       |\n" C_RESET);
    printf(C_BLUE "|                Cool Neon Terminal Edition                |\n" C_RESET);
    print_bar();
    printf(" Card codes available: k / s / i / l\n\n");
}

static const Account *find_account_by_code(char code)
{
    int i;

    for (i = 0; i < account_count; i++)
    {
        if (accounts[i].card_code == code)
        {
            return &accounts[i];
        }
    }

    return NULL;
}

static int validate_pin(int expected_pin)
{
    int pin;
    int attempt;

    for (attempt = 1; attempt <= 3; attempt++)
    {
        printf(" Enter 4-digit PIN (attempt %d/3): ", attempt);
        if (scanf("%d", &pin) != 1)
        {
            return 0;
        }

        if (pin == expected_pin)
        {
            return 1;
        }

        printf(C_RED " PIN mismatch.\n" C_RESET);
    }

    return 0;
}

static void print_receipt(const Account *account, int withdrawn, int remaining)
{
    printf("\n");
    print_bar();
    printf(C_GREEN "|                    TRANSACTION RECEIPT                   |\n" C_RESET);
    print_bar();
    printf(" User        : %s\n", account->name);
    printf(" Profile     : %s\n", account->title);
    printf(" Withdrawn   : %d\n", withdrawn);
    printf(" Remaining   : %d\n", remaining);
    print_bar();
}

static void run_session(const Account *account)
{
    int choice;
    int amount;

    printf(C_GREEN "\n Welcome, %s\n" C_RESET, account->name);
    printf(" Profile: %s\n", account->title);
    print_bar();
    printf(" 1) Withdraw Cash\n");
    printf(" 2) Check Balance\n");
    print_bar();
    printf(" Choose action: ");

    if (scanf("%d", &choice) != 1)
    {
        printf(C_RED " Invalid action input.\n" C_RESET);
        return;
    }

    if (!validate_pin(account->pin))
    {
        printf(C_RED " Access blocked for this session.\n" C_RESET);
        return;
    }

    if (choice == 1)
    {
        printf(" Enter amount to withdraw: ");
        if (scanf("%d", &amount) != 1)
        {
            printf(C_RED " Invalid amount input.\n" C_RESET);
            return;
        }

        if (amount <= 0)
        {
            printf(C_RED " Amount must be greater than zero.\n" C_RESET);
            return;
        }

        if (amount > account->balance)
        {
            printf(C_RED " Insufficient funds.\n" C_RESET);
            return;
        }

        printf(C_GREEN "\n Cash ready. Please collect: %d\n" C_RESET, amount);
        print_receipt(account, amount, account->balance - amount);
    }
    else if (choice == 2)
    {
        printf(C_YELLOW "\n Current Balance: %d\n" C_RESET, account->balance);
    }
    else
    {
        printf(C_RED " Unknown menu action.\n" C_RESET);
    }
}

int main(void)
{
    char card_code;
    const Account *account;

    print_header();
    printf(" Insert card code: ");
    if (scanf(" %c", &card_code) != 1)
    {
        printf(C_RED " Failed to read card.\n" C_RESET);
        return 0;
    }

    account = find_account_by_code(card_code);
    if (account == NULL)
    {
        printf(C_RED " Unknown card code. Access denied.\n" C_RESET);
        print_bar();
        return 0;
    }

    run_session(account);

    printf("\n");
    print_bar();
    printf(C_TEAL " Session complete. Thanks for using ANTEIKU ATM.\n" C_RESET);
    print_bar();
    return 0;
}
