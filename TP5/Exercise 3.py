class Rectangle:

    """Create a class named Rectangle."""
    def __init__(self, width, length):

        """Define a constructor with width and length."""
        if Rectangle.is_valid(width, length) == False:
            raise ValueError("Width and length must be positive!")
        
        self.width = width
        self.length = length

    def area(self):

        """ Create an instance method area()."""
        A = self.width * self.length
        return A

    def perimeter(self):

        """Create an instance method perimeter()"""
        P = 2 *( self.width + self.length )
        return P
    @staticmethod

    def is_valid(width, length):

        """ Create a static method is_valid(width, length)"""
        """The rectangle must have positive dimensions"""
        return width>0 and length>0
        
"""Create at least three Rectangle objects."""
rect1 = Rectangle(5, 10)
rect2 = Rectangle(4, 6)
rect3 = Rectangle(3, 8)
rect4 = Rectangle(1, 3)

rectangles = [rect1, rect2, rect3, rect4]

for i , rect in enumerate(rectangles, start = 1):

    """Display their areas and perimeters."""

    print("Rectangle : ", i)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())
    print("-------------------")

