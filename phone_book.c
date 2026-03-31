#include <stdio.h>

#define C_RESET "\x1b[0m"
#define C_CYAN "\x1b[36m"
#define C_GREEN "\x1b[32m"
#define C_RED "\x1b[31m"

typedef struct
{
    char name[50];
    int age;
    long long phone;
    char dob[20];
    char address[80];
} Contact;

static void print_contact(const Contact *c, int idx)
{
    printf(C_GREEN "\nContact #%d\n" C_RESET, idx + 1);
    printf("Name    : %s\n", c->name);
    printf("Age     : %d\n", c->age);
    printf("Phone   : %lld\n", c->phone);
    printf("DOB     : %s\n", c->dob);
    printf("Address : %s\n", c->address);
}

int main(void)
{
    Contact contacts[2];
    int count = 0;
    int i;

    printf(C_CYAN "========================================================\n" C_RESET);
    printf(C_CYAN "                   AESTHETIC PHONE BOOK\n" C_RESET);
    printf(C_CYAN "========================================================\n" C_RESET);

    printf("How many contacts to add (1-2): ");
    scanf("%d", &count);

    if (count < 1 || count > 2)
    {
        printf(C_RED "Only 1 or 2 contacts are supported in this mini project.\n" C_RESET);
        return 0;
    }

    for (i = 0; i < count; i++)
    {
        printf("\nEnter details for contact %d\n", i + 1);
        printf("Name (use underscore for spaces): ");
        scanf("%49s", contacts[i].name);
        printf("Age: ");
        scanf("%d", &contacts[i].age);
        printf("Phone number: ");
        scanf("%lld", &contacts[i].phone);
        printf("Date of birth (DD-MM-YYYY): ");
        scanf("%19s", contacts[i].dob);
        printf("Address (use underscore for spaces): ");
        scanf("%79s", contacts[i].address);
    }

    printf(C_CYAN "\n=================== SAVED CONTACTS ===================\n" C_RESET);
    for (i = 0; i < count; i++)
    {
        print_contact(&contacts[i], i);
    }

    printf(C_CYAN "\n======================================================\n" C_RESET);
    printf("Phone book session ended.\n");
    return 0;
}
