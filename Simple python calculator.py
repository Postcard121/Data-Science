
def menu():
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Choose an operation: "))

    return choice


def calculator():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    choice = menu()

    if choice == 1:
        print("Answer:", number1 + number2)

    elif choice == 2:
        print("Answer:", number1 - number2)

    elif choice == 3:
        print("Answer:", number1 * number2)

    elif choice == 4:
        print("Answer:", number1 / number2)

    else:
        print("Invalid choice")


calculator()
