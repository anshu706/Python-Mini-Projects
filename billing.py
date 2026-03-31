C_RESET = "\x1b[0m"
C_BLUE = "\x1b[34m"
C_GREEN = "\x1b[32m"
C_YELLOW = "\x1b[33m"


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print(f"{C_BLUE}============================================================{C_RESET}")
    print(f"{C_BLUE}                  ANTEIKU SMART BILLING DESK{C_RESET}")
    print(f"{C_BLUE}============================================================\n{C_RESET}")

    name = input("Customer name: ").strip()
    phone_number = input("Phone number: ").strip()
    customer_id = read_int("Customer ID : ")

    print(f"\n{C_YELLOW}[COSMETICS]{C_RESET}")
    body_soap = read_int("Body Soap   (Rs 10): ")
    hair_cream = read_int("Hair Cream  (Rs 25): ")
    hair_spray = read_int("Hair Spray  (Rs 50): ")
    body_spray = read_int("Body Spray  (Rs 50): ")

    print(f"\n{C_YELLOW}[GROCERY]{C_RESET}")
    sugar = read_int("Sugar       (Rs 100): ")
    tea = read_int("Tea         (Rs 15): ")
    coffee = read_int("Coffee      (Rs 50): ")
    rice = read_int("Rice        (Rs 150): ")
    wheat = read_int("Wheat       (Rs 160): ")

    print(f"\n{C_YELLOW}[BEVERAGES]{C_RESET}")
    pepsi = read_int("Pepsi       (Rs 30): ")
    sprite = read_int("Sprite      (Rs 35): ")
    coke = read_int("Coke        (Rs 30): ")
    mojitos = read_int("Mojitos     (Rs 25): ")
    thumbs_up = read_int("Thumbs Up   (Rs 35): ")

    cosmetics_total = (10 * body_soap) + (25 * hair_cream) + \
        (50 * hair_spray) + (50 * body_spray)
    grocery_total = (100 * sugar) + (15 * tea) + \
        (50 * coffee) + (150 * rice) + (160 * wheat)
    beverage_total = (30 * pepsi) + (35 * sprite) + \
        (30 * coke) + (25 * mojitos) + (35 * thumbs_up)
    total = cosmetics_total + grocery_total + beverage_total

    print(
        f"\n{C_BLUE}========================== INVOICE =========================={C_RESET}")
    print(f"Customer: {name} | Phone: {phone_number} | ID: {customer_id}")
    print("------------------------------------------------------------")
    print(f"Cosmetics total : Rs {cosmetics_total}")
    print(f"Grocery total   : Rs {grocery_total}")
    print(f"Beverage total  : Rs {beverage_total}")
    print("------------------------------------------------------------")
    print(f"{C_GREEN}Grand Total      : Rs {total}{C_RESET}")
    print(f"{C_BLUE}============================================================{C_RESET}")


if __name__ == "__main__":
    main()
