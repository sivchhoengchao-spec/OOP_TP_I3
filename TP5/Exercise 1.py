class Student:

    """ Create a class named Student"""
    def __init__(self, name, age, student_id):

        """Define a constructor with name, age, and student_id."""
        self.name = name;
        self.age = age
        self.student_id = student_id

    def details(self):

        """ Create an instance method named details()"""
        return (f"Stuent Name : {self.name}"
                f"\nAge : {self.age}"
                f"\nStudent ID : {self.student_id}"
                f"\nAdult : {self.is_adult()}")
    
    def is_adult(self):

        """Create an instance method named is_adult()"""
        return "Yes" if self.age>=18 else "No"

"""Create three student objects."""
student1 = Student("chhoeng", 19, "ST001")
student2 = Student("makara", 18, "ST002")
student3 = Student("chhing", 17, "ST003")
i=1


for student in student1, student2, student3:
    
    """ Display the information of each student"""
    print("==================================")
    print("Student ",i)
    student.is_adult()
    print(student.details())
    i=i+1


print("===========================================")
print("Question")
print("1. We use a constructor (__init__()) to initialize an object when it is created. It assigns initial values to the object's attributes, such as name, age, and student_id.")
print("2.Instance methods are functions defined inside a class that perform actions using an object's data. They use self to access and work with the attributes of a specific object.")