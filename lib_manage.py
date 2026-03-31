C_RESET = "\x1b[0m"
C_CYAN = "\x1b[36m"
C_GREEN = "\x1b[32m"
C_YELLOW = "\x1b[33m"
C_RED = "\x1b[31m"


def header():
    print(f"{C_CYAN}========================================================{C_RESET}")
    print(f"{C_CYAN}                 NEO LIBRARY MANAGER{C_RESET}")
    print(f"{C_CYAN}========================================================{C_RESET}")


def show_book(book):
    print(f"{C_GREEN}\nBook Profile{C_RESET}")
    print(f"Title  : {book['title']}")
    print(f"Author : {book['author']}")
    print(f"Pages  : {book['pages']}")
    print(f"Price  : Rs {book['price']}")
    print(f"Code   : {book['code']}")
    print(f"Stock  : {book['stock']} copies")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{C_RED}Please enter a valid number.{C_RESET}")


def main():
    books = [
        {
            "title": "Introduction_to_C",
            "author": "Dennis_Ritchie",
            "pages": 280,
            "price": 350,
            "code": 123,
            "stock": 2,
        },
        {
            "title": "Introduction_to_Python",
            "author": "Guido_Rossum",
            "pages": 320,
            "price": 420,
            "code": 456,
            "stock": 3,
        },
        {
            "title": "Fundamentals_of_Thermodynamics",
            "author": "Moran",
            "pages": 510,
            "price": 670,
            "code": 153,
            "stock": 13,
        },
    ]

    header()
    print("1. Display catalog")
    print("2. Search by code")
    print("3. Add custom book")
    print("4. Exit")

    choice = read_int("Select option: ")

    if choice == 1:
        print(f"{C_YELLOW}\nCatalog Snapshot{C_RESET}")
        for i, book in enumerate(books, start=1):
            print(
                f"{i}) {book['title']} (code {book['code']}, stock {book['stock']})")
    elif choice == 2:
        code = read_int("Enter code: ")
        found = None

        for book in books:
            if book["code"] == code:
                found = book
                break

        if found is None:
            print(f"{C_RED}No book found for code {code}{C_RESET}")
        else:
            show_book(found)
    elif choice == 3:
        custom = {
            "title": input("\nEnter title (use underscore for spaces): ").strip(),
            "author": input("Enter author (use underscore for spaces): ").strip(),
            "pages": read_int("Enter pages: "),
            "price": read_int("Enter price: "),
            "code": read_int("Enter code: "),
            "stock": read_int("Enter stock count: "),
        }

        print(f"{C_GREEN}\nCustom entry saved for this session.{C_RESET}")
        show_book(custom)
    else:
        print("Library closed. Have a nice day.")


if __name__ == "__main__":
    main()
