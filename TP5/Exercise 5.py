class Temperature:

    """Create a class named Temperature."""
    @staticmethod
    def  celsius_to_fahrenheit(celsius):

        """Create a static method celsius_to_fahrenheit(celsius)."""
        F = (9/5)*celsius +32
        return F

    @staticmethod
    def  fahrenheit_to_celsius(fahrenheit):

        """ Create a static method fahrenheit_to_celsius(fahrenheit)"""
        C = (5/9)*(fahrenheit-32)
        return C

    @staticmethod
    def celsius_to_kelvin(celsius):

        """Create a static method celsius_to_kelvin(celsius)"""
        K = celsius + 273.15
        return K

"""Test the methods with different temperatures"""
Celsius = 25
Fahrenheit = 77


F = Temperature.celsius_to_fahrenheit(Celsius)
C = Temperature.fahrenheit_to_celsius(Fahrenheit)
K = Temperature.celsius_to_kelvin(Celsius)

"""Display all conversion results."""
print("Celsius:", C)
print("Fahrenheit:", F)
print("Kelvin:", round(K, 2))
