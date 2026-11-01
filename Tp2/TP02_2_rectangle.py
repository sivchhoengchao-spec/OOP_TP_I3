class Rectangle:
    """A rectangle with a length and a width."""

    def __init__ (self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("length and width must be greater than 0")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print(f"Length    : {self.length}")
        print(f"Width     : {self.width}")
        print(f"Area      : {self.area()}")
        print(f"Perimeter : {self.perimeter()}")


def read_number(message):
    """Ask until the user types a valid number."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a number, for example 5 or 3.5")


def main2():
    length = read_number("Enter the length of the rectangle: ")
    width = read_number("Enter the width of the rectangle: ")
    try:
        rect = Rectangle(length, width)
    except ValueError as error:
        print("Error:", error)
    else:
        rect.display()


if __name__ == "__main__":
    print("EX2:")
    main2()
