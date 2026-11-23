# Keeps the entered number and calculates the following integer.
class LuckyNumberGame:
    """Return the integer immediately after a user's number."""

    def __init__(self, number: int) :
        self.number: int = number  # Save the number for this game.

    def get_next_number(self) :
        """Calculate and return the next integer."""
        return self.number + 1  # Add one to get the next integer.


def main5():
    """Run rounds of the game until the user chooses to stop."""
    while True:  # Start another round unless the user chooses to stop.
        try:
            # Convert the user's input from text to an integer.
            number = int(input("Please enter an integer: "))
        except ValueError:
            # Handle text or other input that cannot be converted to an integer.
            print("Please enter a valid integer.")
            continue  # Skip the rest of this round and ask for a number again.

        # Show the integer that comes after the user's number.
        game = LuckyNumberGame(number)
        print(f"The next number is: {game.get_next_number()}")

        # Repeat the prompt until the user enters "yes" or "no".
        while True:
            answer = input("Do you want to play again? (Yes/No): ").strip().lower()
            if answer in {"yes", "no"}:
                break
            print("Please enter Yes or No.")

        if answer == "no":
            break  # Exit the game loop when the user is finished.


# Run the game only when this file is started directly.
if __name__ == "__main__":
    print("EX5:")
    main5()
