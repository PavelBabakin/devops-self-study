# Task 3: Create a Go program that takes user input and performs basic arithmetic operations.

## **Building a Basic Arithmetic Calculator with Go**

Go, often referred to as Golang, is renowned for its simplicity and efficiency. While it's commonly used for web services and DevOps tools, it's also a great language for building basic applications, especially when you're just getting started. In this tutorial, we'll walk you through creating a simple Go program that takes user input to perform basic arithmetic operations.

### **Creating a Simple Arithmetic Calculator**

1. **Setting Up the Project**:
    
    Begin by creating a new directory for your Go project:
    
    ```bash
    mkdir go-arithmetic && cd go-arithmetic
    ```
    
    Within this directory, create a new Go file named **`arithmetic.go`**:
    
    ```bash
    touch arithmetic.go
    ```
    
2. **Crafting the Calculator**:
    
    Open the **`arithmetic.go`** file in your preferred text editor and paste the following code:
    
    ```go
    package main
    
    import (
        "fmt"
    )
    
    func main() {
        var num1, num2 float64
        var operation string
    
        fmt.Print("Enter first number: ")
        fmt.Scan(&num1)
    
        fmt.Print("Enter second number: ")
        fmt.Scan(&num2)
    
        fmt.Print("Enter operation (+, -, *, /): ")
        fmt.Scan(&operation)
    
        switch operation {
        case "+":
            fmt.Printf("Result: %f\n", num1+num2)
        case "-":
            fmt.Printf("Result: %f\n", num1-num2)
        case "*":
            fmt.Printf("Result: %f\n", num1*num2)
        case "/":
            if num2 != 0 {
                fmt.Printf("Result: %f\n", num1/num2)
            } else {
                fmt.Println("Error: Division by zero.")
            }
        default:
            fmt.Println("Invalid operation.")
        }
    }
    ```
    
    This code sets up a basic calculator. It prompts the user to input two numbers and an arithmetic operation. The program then performs the chosen operation and displays the result.
    
3. **Running the Calculator**:
    
    In your terminal, navigate to the directory containing **`arithmetic.go`**. Execute the program with:
    
    ```bash
    go run arithmetic.go
    ```
    
    Follow the on-screen prompts to input your numbers and desired arithmetic operation. The program will then display the result of the operation.
    

### **Conclusion**

With just a few lines of Go code, you've built a basic arithmetic calculator. This exercise introduces you to user input handling, conditional logic, and basic arithmetic in Go. It's a foundational step that paves the way for more intricate Go projects in the future. Whether you're a seasoned developer or just starting out, Go offers a plethora of opportunities to build efficient and scalable applications.