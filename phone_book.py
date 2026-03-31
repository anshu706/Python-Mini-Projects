C_RESET = "\x1b[0m"
C_CYAN = "\x1b[36m"
C_GREEN = "\x1b[32m"
C_RED = "\x1b[31m"


def print_contact(contact, idx):
    print(f"{C_GREEN}\nContact #{idx + 1}{C_RESET}")
    print(f"Name    : {contact['name']}")
    print(f"Age     : {contact['age']}")
    print(f"Phone   : {contact['phone']}")
    print(f"DOB     : {contact['dob']}")
    print(f"Address : {contact['address']}")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{C_RED}Please enter a valid number.{C_RESET}")


def main():
    print(f"{C_CYAN}========================================================{C_RESET}")
    print(f"{C_CYAN}                   AESTHETIC PHONE BOOK{C_RESET}")
    print(f"{C_CYAN}========================================================{C_RESET}")

    count = read_int("How many contacts to add (1-2): ")

    if count < 1 or count > 2:
        print(
            f"{C_RED}Only 1 or 2 contacts are supported in this mini project.{C_RESET}")
        return

    contacts = []
    for i in range(count):
        print(f"\nEnter details for contact {i + 1}")
        contact = {
            "name": input("Name (use underscore for spaces): ").strip(),
            "age": read_int("Age: "),
            "phone": input("Phone number: ").strip(),
            "dob": input("Date of birth (DD-MM-YYYY): ").strip(),
            "address": input("Address (use underscore for spaces): ").strip(),
        }
        contacts.append(contact)

    print(f"{C_CYAN}\n=================== SAVED CONTACTS ==================={C_RESET}")
    for i, contact in enumerate(contacts):
        print_contact(contact, i)

    print(f"{C_CYAN}\n======================================================{C_RESET}")
    print("Phone book session ended.")


if __name__ == "__main__":
    main()
