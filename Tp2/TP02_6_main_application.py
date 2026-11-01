import TP02_1_greeting as greeting
import TP02_2_rectangle as rectangle
import TP02_3_equation as EquationCalculator
import TP02_4_hundreds_counter as hundreds_counter
import TP02_5_lucky_number as LuckyNumberGame 

def main():
    while True:
        print("\n========== TP02 Python OOP ==========\n")
        print(" 1. Greeting")
        print(" 2. Rectangle")
        print(" 3. Equation Calculator")
        print(" 4. Hundreds Counter")
        print(" 5. Cheater Game")
        print(" 0. Exit")
        print("\n=====================================\n")

        choice = input("Please, Enter your choice (0-5): ").strip()

        if choice == "1":
            greeting.main1()
        elif choice == "2":
            rectangle.main2()
        elif choice == "3":
            EquationCalculator.main3()
        elif choice == "4":
            hundreds_counter.main4()
        elif choice == "5":
            LuckyNumberGame.main5()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

        
if __name__ == "__main__":
    print("Welcome to the TP02 Python OOP Application!")
    main()

