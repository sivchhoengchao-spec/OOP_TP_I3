class Product:

    """ Create a class named Product."""

    """Define a class attribute store_name = "ITC Online Store"."""
    store_name = "ITC Online Store"

    """ Define a class attribute product_count = 0"""
    product_count = 0

    def __init__(self, name, price, quantity):

        """Define a constructor with  name, price, quantitly"""
        if self.is_valid_price(price) == False:
            raise ValueError ("Price must be positive!")
        self.name = name
        self.price = price
        self.quantity = quantity

        """ Increase the product count when a new object is created"""
        Product.product_count +=1


    def display_product(self):

        """ Create an instance method display_product()"""
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def total_value(self):

        """Create an instance method total_value() to calculate price multiplied by quantity"""
        return self.price * self.quantity

    @classmethod
    def get_product_count(cls):

        """Create a class method get_product_count()"""
        return cls.product_count

    @staticmethod
    def is_valid_price(price):

        """ Create a static method is_valid_price(price) to check whether the price is pos
itive."""
        return price > 0

"""Create at least three Product objects."""
product1 = Product("Laptop", 800, 5)
product2 = Product("Mouse", 15, 20)
product3 = Product("Keyboard", 30, 10)

products = [product1, product2, product3]
total_inventory = 0

print(f"============  {Product.store_name}  =================")
for i, product in enumerate(products, start=1):

    """Display all product information and the total inventory value."""
    print("\nProduct:", i)

    product.display_product()

    print("Total Value:", product.total_value())

    total_inventory += product.total_value()

    print("------------------------")



print("Total Products:", Product.get_product_count())
print("Total Inventory Value:", total_inventory)
