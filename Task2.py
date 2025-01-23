def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            operation = input("\nEnter your choice (1/2/3/4/5): ")
            
            if operation == "5":
                print("Exiting the calculator. Goodbye!")
                break
            
            if operation not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please choose a valid operation.")
                continue
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if operation == "1":
                result = num1 + num2
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == "2":
                result = num1 - num2
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == "3":
                result = num1 * num2
                print(f"The result of {num1} * {num2} is: {result}")
            elif operation == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is: {result}")
        except ValueError:
            print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    calculator()
