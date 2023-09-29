def main():
    # Get user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display the available operations
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for the operation
    choice = input("\nEnter your choice (1/2/3/4): ")

    # Perform the selected operation
    if choice == '1':
        print(f"\nResult: {num1 + num2}")
    elif choice == '2':
        print(f"\nResult: {num1 - num2}")
    elif choice == '3':
        print(f"\nResult: {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("\nError: Division by zero is not allowed!")
        else:
            print(f"\nResult: {num1 / num2}")
    else:
        print("\nInvalid choice!")

if __name__ == "__main__":
    main()
