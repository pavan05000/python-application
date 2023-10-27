# Sample Python Application

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def main():
    print("Welcome to the Simple Calculator App!")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            result = add_numbers(num1, num2)
        elif choice == '2':
            result = subtract_numbers(num1, num2)
        elif choice == '3':
            result = multiply_numbers(num1, num2)
        elif choice == '4':
            result = divide_numbers(num1, num2)
        else:
            result = "Invalid choice. Please choose a valid operation."

        print(f"Result: {result}")

if __name__ == "__main__":
    main()

