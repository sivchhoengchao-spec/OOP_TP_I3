class Employee:

    """ Create a class named Employee"""

    """ Define a class attribute company = "ITC"."""
    company =  "ITC"

    """Define a class attribute employee_count = 0."""
    employee_count = 0

    def __init__(self, name, position, salary):

        """Define a constructor with name, position, and salary"""
        self.name = name
        self.position = position
        self.salary = salary

        """Increase the employee count whenever an object is created."""
        Employee.employee_count +=1

    def display_info(self):
       
        """Create an instance method display_info()"""
        print("Name:", self.name)
        print("Position:", self.position)
        print("Salary:", self.salary)

    @classmethod
    def get_employee_count(cls):

        """ Create a class method get_employee_count()"""
        return cls.employee_count

"""Create at least four employees"""
employee1 = Employee("chhoeng", "Manager", 1000)
employee2 = Employee("makara", "Developer", 900)
employee3 = Employee("chhing", "Designer", 800)
employee4 = Employee("vath", "Accountant", 700)
    
    
employees = [employee1, employee2, employee3, employee4]

for i, emp in enumerate(employees, start=1):

    """ Display all employee information and the total number of employees"""
    print("Employee:", i)
    emp.display_info()
    print("--------------------")
print("Total Employees:", Employee.get_employee_count())