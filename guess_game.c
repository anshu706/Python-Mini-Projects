#include <stdio.h>

#define C_RESET "\x1b[0m"
#define C_CYAN "\x1b[36m"
#define C_GREEN "\x1b[32m"
#define C_RED "\x1b[31m"

int main(void)
{
    int secret_number = 5;
    int guess_number = 0;
    int guess_limit = 3;
    int i;

    printf(C_CYAN "======================================\n" C_RESET);
    printf(C_CYAN "         GUESS THE NUMBER GAME\n" C_RESET);
    printf(C_CYAN "======================================\n" C_RESET);
    printf("You have %d attempts.\n\n", guess_limit);

    for (i = 1; i <= guess_limit; i++)
    {
        printf("Attempt %d/%d -> Enter guess: ", i, guess_limit);
        scanf("%d", &guess_number);

        if (guess_number == secret_number)
        {
            printf(C_GREEN "\nPerfect guess. You won!\n" C_RESET);
            break;
        }
        else
        {
            printf(C_RED "Not this one.\n" C_RESET);
        }
    }

    if (guess_number != secret_number)
    {
        printf(C_RED "\nYou lost. Secret number was %d.\n" C_RESET, secret_number);
    }

    return 0;
}
