#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define C_RESET "\x1b[0m"
#define C_MAGENTA "\x1b[35m"
#define C_GREEN "\x1b[32m"
#define C_RED "\x1b[31m"
#define C_YELLOW "\x1b[33m"

static void print_rules(void)
{
    printf(C_MAGENTA "========================================================\n" C_RESET);
    printf(C_MAGENTA "                     LUCKY CASINO\n" C_RESET);
    printf(C_MAGENTA "========================================================\n" C_RESET);
    printf("1. Guess a number from 1 to 10.\n");
    printf("2. Correct guess wins 10x of your bet.\n");
    printf("3. Wrong guess loses your bet amount.\n");
    printf("========================================================\n\n");
}

int main(void)
{
    char name[50];
    int balance;
    int again = 1;

    srand((unsigned int)time(NULL));
    print_rules();

    printf("Player name: ");
    scanf("%49s", name);
    printf("Deposit amount: $");
    scanf("%d", &balance);

    while (again == 1 && balance > 0)
    {
        int bet;
        int guess;
        int lucky_number;

        printf("\n" C_YELLOW "Current Balance: $%d\n" C_RESET, balance);
        printf("Enter bet amount: $");
        scanf("%d", &bet);

        if (bet <= 0 || bet > balance)
        {
            printf(C_RED "Invalid bet. Try again.\n" C_RESET);
            continue;
        }

        printf("Guess a number (1-10): ");
        scanf("%d", &guess);

        if (guess < 1 || guess > 10)
        {
            printf(C_RED "Guess must be between 1 and 10.\n" C_RESET);
            continue;
        }

        lucky_number = (rand() % 10) + 1;

        if (guess == lucky_number)
        {
            int win = bet * 10;
            balance += win;
            printf(C_GREEN "Amazing %s! Lucky number was %d. You won $%d\n" C_RESET, name, lucky_number, win);
        }
        else
        {
            balance -= bet;
            printf(C_RED "No luck this time. Lucky number was %d. You lost $%d\n" C_RESET, lucky_number, bet);
        }

        if (balance <= 0)
        {
            printf(C_RED "\nBalance reached $0. Game over.\n" C_RESET);
            break;
        }

        printf("Play another round? (1 = Yes, 0 = No): ");
        scanf("%d", &again);
    }

    printf(C_MAGENTA "\nThanks for playing, %s. Final balance: $%d\n" C_RESET, name, balance);
    return 0;
}
