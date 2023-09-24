# Task 3: Create a Python script that takes user input and performs basic arithmetic operations.

Python, renowned for its simplicity and readability, is a versatile tool in a developer's arsenal. Whether you're a seasoned programmer or just starting out, building a basic calculator is a fantastic way to get acquainted with Python's capabilities. In this guide, we'll walk you through creating a simple calculator that can perform basic arithmetic operations using Python on macOS.

### **Why a Calculator?**

A calculator might seem rudimentary, but it's a perfect project for beginners. It introduces essential programming concepts like taking user input, performing arithmetic operations, and using conditional statements. Plus, it's functional – everyone needs a calculator!

### **Creating the Calculator Script**

### **1. Setting Up Your Workspace**

Open your terminal and create a new Python file:

```
nano arithmetic_operations.py
```

This command opens a blank file named **`arithmetic_operations.py`**.

### **2. Writing the Script**

Our calculator will take two numbers as input from the user and then ask the user to choose an arithmetic operation (addition, subtraction, multiplication, or division). Here's the code:

```python
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
```

### **3. Running the Script**

After saving the script, navigate to its directory in the terminal and run:

```
python3 arithmetic_operations.py
```

Follow the on-screen prompts, and voilà! You have a working calculator.

### **Expanding Your Horizons**

This basic calculator is just the tip of the iceberg. As you delve deeper into Python, consider enhancing this calculator. Maybe introduce complex operations, error handling, or even develop a graphical interface for it. The sky's the limit!

### **Conclusion**

Building a basic calculator is a rewarding experience. It's a testament to Python's ease of use and versatility. As you continue your journey in the world of programming and DevOps, remember that even the most complex applications often start with simple building blocks. Keep experimenting, keep learning, and most importantly, have fun!