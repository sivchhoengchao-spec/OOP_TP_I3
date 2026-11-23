class EquationCalculator:   #Create class name "EquationCalculator"
    def __init__(self, y, z): #Constructor initializes the values of y and z
        self.y = y #store the input values
        self.z = z 

    def calculate_x(self): #Create the method to 'calculate x" by using the formula
        if self.y == 0 or self.z == 0: #Using condition to identify y, z > 0
             raise ValueError("y and z must not be zero.") #Manually trigger exception(error)
        if self.y + self.z == 0: #Identify y + z > 0
            raise ValueError("y + z must not be zero")
        x = (self.y * self.z)/(self.y + self.z) #Method of equation
        return x #sent the calculate result back to the caller 

    def display_result(self): #Create method to display x
        x = self.calculate_x() #Call function calculate_x
        print(f"y = {self.y}, z = {self.z}") #Display value of y and z
        print(f"x = {x}") #Display value of x
    
    
def main3(): #Create main function to run the program
    try: #Using try block lets you test a block of code errors
                #Get input from user 
                y = float(input("Enter a value of y: "))
                z = float(input("Enter a value of z: "))

                #Create  calculator object 
            
    except ValueError: #Using except block lets you handle the error
                print("Error: Please enter the valid number!")
    else:
        calculator = EquationCalculator(y, z)
                
        calculator.display_result() #Display the result
    
    
if __name__ == "__main__":

    print("EX3:")
    main3() #Call main function to run the program
        
