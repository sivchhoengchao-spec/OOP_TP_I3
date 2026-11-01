class Greeting:
    """A class for greeting a user."""

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        """Print a greeting message."""
        print(f"Hello, {self.name}!")


def main1():
    """Get the user's name and display a greeting."""
   
    name = input("Enter your name: ").strip()

    greeting = Greeting(name)
    greeting.say_hello()


if __name__ == "__main__":
    print("EX1:")
    main1()