#include <stdio.h>

#define C_RESET "\x1b[0m"
#define C_BLUE "\x1b[34m"
#define C_GREEN "\x1b[32m"
#define C_YELLOW "\x1b[33m"

int main(void)
{
    char name[50];
    long long phone_number;
    int customer_id;

    int body_soap;
    int hair_cream;
    int hair_spray;
    int body_spray;

    int sugar;
    int tea;
    int coffee;
    int rice;
    int wheat;

    int pepsi;
    int sprite;
    int coke;
    int mojitos;
    int thumbs_up;

    int cosmetics_total;
    int grocery_total;
    int beverage_total;
    int total;

    printf(C_BLUE "============================================================\n" C_RESET);
    printf(C_BLUE "                  ANTEIKU SMART BILLING DESK\n" C_RESET);
    printf(C_BLUE "============================================================\n\n" C_RESET);

    printf("Customer name: ");
    scanf("%49s", name);
    printf("Phone number: ");
    scanf("%lld", &phone_number);
    printf("Customer ID : ");
    scanf("%d", &customer_id);

    printf("\n" C_YELLOW "[COSMETICS]\n" C_RESET);
    printf("Body Soap   (Rs 10): "); scanf("%d", &body_soap);
    printf("Hair Cream  (Rs 25): "); scanf("%d", &hair_cream);
    printf("Hair Spray  (Rs 50): "); scanf("%d", &hair_spray);
    printf("Body Spray  (Rs 50): "); scanf("%d", &body_spray);

    printf("\n" C_YELLOW "[GROCERY]\n" C_RESET);
    printf("Sugar       (Rs 100): "); scanf("%d", &sugar);
    printf("Tea         (Rs 15): "); scanf("%d", &tea);
    printf("Coffee      (Rs 50): "); scanf("%d", &coffee);
    printf("Rice        (Rs 150): "); scanf("%d", &rice);
    printf("Wheat       (Rs 160): "); scanf("%d", &wheat);

    printf("\n" C_YELLOW "[BEVERAGES]\n" C_RESET);
    printf("Pepsi       (Rs 30): "); scanf("%d", &pepsi);
    printf("Sprite      (Rs 35): "); scanf("%d", &sprite);
    printf("Coke        (Rs 30): "); scanf("%d", &coke);
    printf("Mojitos     (Rs 25): "); scanf("%d", &mojitos);
    printf("Thumbs Up   (Rs 35): "); scanf("%d", &thumbs_up);

    cosmetics_total = (10 * body_soap) + (25 * hair_cream) + (50 * hair_spray) + (50 * body_spray);
    grocery_total = (100 * sugar) + (15 * tea) + (50 * coffee) + (150 * rice) + (160 * wheat);
    beverage_total = (30 * pepsi) + (35 * sprite) + (30 * coke) + (25 * mojitos) + (35 * thumbs_up);
    total = cosmetics_total + grocery_total + beverage_total;

    printf("\n" C_BLUE "========================== INVOICE ==========================\n" C_RESET);
    printf("Customer: %s | Phone: %lld | ID: %d\n", name, phone_number, customer_id);
    printf("------------------------------------------------------------\n");
    printf("Cosmetics total : Rs %d\n", cosmetics_total);
    printf("Grocery total   : Rs %d\n", grocery_total);
    printf("Beverage total  : Rs %d\n", beverage_total);
    printf("------------------------------------------------------------\n");
    printf(C_GREEN "Grand Total      : Rs %d\n" C_RESET, total);
    printf(C_BLUE "============================================================\n" C_RESET);

    return 0;
}
