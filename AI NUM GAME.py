def ai_number_prediction():
    print("=" * 40)
    print("      AI Number Prediction Game")
    print("=" * 40)
    print("Think of a number between 1 and 100")

    low = 1
    high = 100
    attempts = 0

    input("\nPress Enter when you are ready...")

    while low <= high:
        attempts += 1
        guess = (low + high) // 2

        print(f"\nAI Guess #{attempts}: {guess}")

        response = input(
            "Enter response - "
            "[h] Too High  "
            "[l] Too Low  "
            "[c] Correct : "
        ).strip().lower()

        if response == 'c':
            print("\n===================================")
            print(f"AI successfully guessed your number!")
            print(f"Total Attempts: {attempts}")
            print("===================================")
            break

        elif response == 'h':
            high = guess - 1

        elif response == 'l':
            low = guess + 1

        else:
            print("Invalid input! Please enter h, l, or c.")

    else:
        print("\nInconsistent responses detected.")


if __name__ == "__main__":
    ai_number_prediction()