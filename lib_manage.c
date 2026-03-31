#include <stdio.h>
#include <string.h>

#define C_RESET "\x1b[0m"
#define C_CYAN "\x1b[36m"
#define C_GREEN "\x1b[32m"
#define C_YELLOW "\x1b[33m"
#define C_RED "\x1b[31m"

typedef struct
{
    char title[80];
    char author[60];
    int pages;
    int price;
    int code;
    int stock;
} Book;

static void header(void)
{
    printf(C_CYAN "========================================================\n" C_RESET);
    printf(C_CYAN "                 NEO LIBRARY MANAGER\n" C_RESET);
    printf(C_CYAN "========================================================\n" C_RESET);
}

static void show_book(const Book *b)
{
    printf(C_GREEN "\nBook Profile\n" C_RESET);
    printf("Title  : %s\n", b->title);
    printf("Author : %s\n", b->author);
    printf("Pages  : %d\n", b->pages);
    printf("Price  : Rs %d\n", b->price);
    printf("Code   : %d\n", b->code);
    printf("Stock  : %d copies\n", b->stock);
}

int main(void)
{
    Book books[3] = {
        {"Introduction_to_C", "Dennis_Ritchie", 280, 350, 123, 2},
        {"Introduction_to_Python", "Guido_Rossum", 320, 420, 456, 3},
        {"Fundamentals_of_Thermodynamics", "Moran", 510, 670, 153, 13}};

    int choice;
    int code;

    header();
    printf("1. Display catalog\n");
    printf("2. Search by code\n");
    printf("3. Add custom book\n");
    printf("4. Exit\n");
    printf("Select option: ");
    scanf("%d", &choice);

    if (choice == 1)
    {
        int i;
        printf(C_YELLOW "\nCatalog Snapshot\n" C_RESET);
        for (i = 0; i < 3; i++)
        {
            printf("%d) %s (code %d, stock %d)\n", i + 1, books[i].title, books[i].code, books[i].stock);
        }
    }
    else if (choice == 2)
    {
        int i;
        int found = 0;

        printf("Enter code: ");
        scanf("%d", &code);

        for (i = 0; i < 3; i++)
        {
            if (books[i].code == code)
            {
                show_book(&books[i]);
                found = 1;
                break;
            }
        }

        if (!found)
        {
            printf(C_RED "No book found for code %d\n" C_RESET, code);
        }
    }
    else if (choice == 3)
    {
        Book custom;

        printf("\nEnter title (use underscore for spaces): ");
        scanf("%79s", custom.title);
        printf("Enter author (use underscore for spaces): ");
        scanf("%59s", custom.author);
        printf("Enter pages: ");
        scanf("%d", &custom.pages);
        printf("Enter price: ");
        scanf("%d", &custom.price);
        printf("Enter code: ");
        scanf("%d", &custom.code);
        printf("Enter stock count: ");
        scanf("%d", &custom.stock);

        printf(C_GREEN "\nCustom entry saved for this session.\n" C_RESET);
        show_book(&custom);
    }
    else
    {
        printf("Library closed. Have a nice day.\n");
    }

    return 0;
}
