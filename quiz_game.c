#include <stdio.h>

#define C_RESET "\x1b[0m"
#define C_BLUE "\x1b[34m"
#define C_GREEN "\x1b[32m"
#define C_RED "\x1b[31m"
#define C_YELLOW "\x1b[33m"

typedef struct
{
    const char *question;
    const char *o1;
    const char *o2;
    const char *o3;
    const char *o4;
    int answer;
} Quiz;

int main(void)
{
    Quiz quiz[] = {
        {"Which one is the first search engine on the internet?", "Google", "Archie", "Wais", "Altavista", 2},
        {"Which browser was invented in 1990?", "Internet Explorer", "Mosaic", "Mozilla", "Nexus", 4},
        {"First computer virus is known as?", "Rabbit", "Creeper virus", "Elk Cloner", "SCA virus", 2},
        {"Firewall in computer is used for?", "Security", "Data Transmission", "Monitoring", "Authentication", 1},
        {"Which one is not a database software?", "MySQL", "Oracle", "COBOL", "Sybase", 3}};

    int i;
    int start;
    int score = 0;

    printf(C_BLUE "========================================================\n" C_RESET);
    printf(C_BLUE "                    QUIZ ARENA 5X\n" C_RESET);
    printf(C_BLUE "========================================================\n" C_RESET);
    printf("Press 7 to start, 0 to quit: ");
    scanf("%d", &start);

    if (start == 0)
    {
        printf("Quiz closed.\n");
        return 0;
    }

    if (start != 7)
    {
        printf(C_RED "Invalid input. Restart and press 7.\n" C_RESET);
        return 0;
    }

    for (i = 0; i < 5; i++)
    {
        int ans;

        printf(C_YELLOW "\nQ%d. %s\n" C_RESET, i + 1, quiz[i].question);
        printf("1) %s\n", quiz[i].o1);
        printf("2) %s\n", quiz[i].o2);
        printf("3) %s\n", quiz[i].o3);
        printf("4) %s\n", quiz[i].o4);
        printf("Your answer: ");
        scanf("%d", &ans);

        if (ans == quiz[i].answer)
        {
            score += 5;
            printf(C_GREEN "Correct! +5\n" C_RESET);
        }
        else
        {
            printf(C_RED "Wrong! Correct option was %d\n" C_RESET, quiz[i].answer);
        }
    }

    printf(C_BLUE "\n=================== RESULT ===================\n" C_RESET);
    printf("Final Score: %d / 25\n", score);

    if (score >= 20)
    {
        printf(C_GREEN "Outstanding performance.\n" C_RESET);
    }
    else if (score >= 10)
    {
        printf(C_YELLOW "Good attempt. Keep practicing.\n" C_RESET);
    }
    else
    {
        printf(C_RED "Needs improvement. Try again.\n" C_RESET);
    }

    return 0;
}
