# Task 2: Write a Go program to print "Hello, DevOps!".

## **Getting Started with Go: Your First Program**

Go, colloquially known as Golang, is a statically typed, compiled language developed by Google. Its simplicity, efficiency, and strong standard library make it a popular choice for various applications, including web services, DevOps tools, and more. In this article, we'll guide you through writing your very first Go program: a simple application that prints "Hello, DevOps!".

### **Step-by-Step Guide to Your First Go Program**

1. **Creating the Go File**:
    
    Start by creating a new directory for your Go project:
    
    ```bash
    mkdir hello-devops && cd hello-devops
    ```
    
    Within this directory, create a new Go file named **`main.go`**:
    
    ```bash
    touch main.go
    ```
    
2. **Writing the Go Program**:
    
    Open the **`main.go`** file in your preferred text editor. Insert the following code:
    
    ```go
    package main
    
    import "fmt"
    
    func main() {
        fmt.Println("Hello, DevOps!")
    }
    ```
    
    Here's a quick breakdown of the code:
    
    - **`package main`**: This defines the package name. Every Go executable program starts with the main package.
    - **`import "fmt"`**: This imports the **`fmt`** package, which contains functions for formatted I/O.
    - **`func main()`**: The main function is the entry point of our Go program.
    - **`fmt.Println("Hello, DevOps!")`**: This line prints the string "Hello, DevOps!" to the console.
3. **Running the Go Program**:
    
    With the code in place, it's time to run our program. In the terminal, ensure you're in the directory containing **`main.go`**. Execute the following command:
    
    ```bash
    go run main.go
    ```
    
    You should see the output:
    
    ```
    Hello, DevOps!
    ```
    

### **Wrapping Up**

Congratulations! You've just written and executed your first Go program. While this is a simple introduction, the world of Go offers vast possibilities. As you continue your journey, you'll encounter a wide range of functionalities and libraries that will empower you to build robust applications, be it for web services, DevOps automation, or any other domain.

Stay tuned for more articles as we delve deeper into the world of Go and its applications in the realm of DevOps!