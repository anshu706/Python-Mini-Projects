C_RESET = "\x1b[0m"
C_BLUE = "\x1b[34m"
C_GREEN = "\x1b[32m"
C_RED = "\x1b[31m"
C_YELLOW = "\x1b[33m"


QUIZ = [
    {
        "question": "Which one is the first search engine on the internet?",
        "o1": "Google",
        "o2": "Archie",
        "o3": "Wais",
        "o4": "Altavista",
        "answer": 2,
    },
    {
        "question": "Which browser was invented in 1990?",
        "o1": "Internet Explorer",
        "o2": "Mosaic",
        "o3": "Mozilla",
        "o4": "Nexus",
        "answer": 4,
    },
    {
        "question": "First computer virus is known as?",
        "o1": "Rabbit",
        "o2": "Creeper virus",
        "o3": "Elk Cloner",
        "o4": "SCA virus",
        "answer": 2,
    },
    {
        "question": "Firewall in computer is used for?",
        "o1": "Security",
        "o2": "Data Transmission",
        "o3": "Monitoring",
        "o4": "Authentication",
        "answer": 1,
    },
    {
        "question": "Which one is not a database software?",
        "o1": "MySQL",
        "o2": "Oracle",
        "o3": "COBOL",
        "o4": "Sybase",
        "answer": 3,
    },
]


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{C_RED}Please enter a valid number.{C_RESET}")


def main():
    score = 0

    print(f"{C_BLUE}========================================================{C_RESET}")
    print(f"{C_BLUE}                    QUIZ ARENA 5X{C_RESET}")
    print(f"{C_BLUE}========================================================{C_RESET}")
    start = read_int("Press 7 to start, 0 to quit: ")

    if start == 0:
        print("Quiz closed.")
        return

    if start != 7:
        print(f"{C_RED}Invalid input. Restart and press 7.{C_RESET}")
        return

    for i, q in enumerate(QUIZ, start=1):
        ans = read_int(
            f"{C_YELLOW}\nQ{i}. {q['question']}\n{C_RESET}"
            f"1) {q['o1']}\n"
            f"2) {q['o2']}\n"
            f"3) {q['o3']}\n"
            f"4) {q['o4']}\n"
            "Your answer: "
        )

        if ans == q["answer"]:
            score += 5
            print(f"{C_GREEN}Correct! +5{C_RESET}")
        else:
            print(f"{C_RED}Wrong! Correct option was {q['answer']}{C_RESET}")

    print(f"{C_BLUE}\n=================== RESULT ==================={C_RESET}")
    print(f"Final Score: {score} / 25")

    if score >= 20:
        print(f"{C_GREEN}Outstanding performance.{C_RESET}")
    elif score >= 10:
        print(f"{C_YELLOW}Good attempt. Keep practicing.{C_RESET}")
    else:
        print(f"{C_RED}Needs improvement. Try again.{C_RESET}")


if __name__ == "__main__":
    main()
