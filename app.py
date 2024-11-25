import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Power (^)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log)")

    choice = input("Enter choice (1-10): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {num1 + num2}")
        elif choice == '2':
            print(f"The result is: {num1 - num2}")
        elif choice == '3':
            print(f"The result is: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")

    elif choice == '5':
        num = float(input("Enter the number: "))
        if num >= 0:
            print(f"The result is: {math.sqrt(num)}")
        else:
            print("Error: Cannot calculate the square root of a negative number.")

    elif choice == '6':
        base = float(input("Enter the base: "))
        exp = float(input("Enter the exponent: "))
        print(f"The result is: {math.pow(base, exp)}")

    elif choice in ['7', '8', '9', '10']:
        num = float(input("Enter the number (in degrees): "))
        rad = math.radians(num)

        if choice == '7':
            print(f"The result is: {math.sin(rad)}")
        elif choice == '8':
            print(f"The result is: {math.cos(rad)}")
        elif choice == '9':
            print(f"The result is: {math.tan(rad)}")
        elif choice == '10':
            if num > 0:
                print(f"The result is: {math.log(num)}")
            else:
                print("Error: Logarithm undefined for non-positive numbers.")

    else:
        print("Invalid input. Please select a valid operation.")

# Run the scientific calculator
scientific_calculator()


