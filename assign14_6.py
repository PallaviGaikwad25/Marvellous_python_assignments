class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b > 0:
            return a / b
        else:
            return "Error: Division by zero"


def main():
    print("Enter two numbers:")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    calc = Calculator()

    if choice == '1':
        result = calc.add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = calc.subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        result = calc.multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        result = calc.divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
