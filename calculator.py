print("Welcome to the simple calculator!")
print("Available operations: +, -, *, /")

while True:
    # Input validation for numbers
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
    except ValueError:
        print("Invalid number entered. Please enter numeric values.")
        continue

    # Input for operation
    operation = input("Enter operation (+, -, *, /): ")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose from +, -, *, /.")

    # Ask if user wants to continue
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        print("Thanks for using the calculator. Goodbye!")
        break