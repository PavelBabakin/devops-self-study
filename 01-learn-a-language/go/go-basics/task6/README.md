# Task 6: Write a Go program to read a log file and count the number of error messages.

## **Counting Error Messages in Log Files with Go**

Logs are an integral part of any application. They provide insights into the application's behavior, help in debugging issues, and can be crucial for monitoring and alerting. In this tutorial, we'll explore how to use Go (or Golang) to read a log file and count the number of error messages.

### **Why Go for Log Processing?**

Go is known for its efficiency, concurrency support, and a rich standard library. Its simplicity in syntax and powerful file handling capabilities make it an excellent choice for tasks like log processing.

### **Building the Log Counter in Go**

1. **Setting the Stage**:
    
    Before diving into the code, ensure you have a sample log file. For this tutorial, we've used a file named **`sample.log`** with the following entries:
    
    ```makefile
    INFO: User logged in
    ERROR: Database connection failed
    INFO: User logged out
    ERROR: File not found
    INFO: User registered
    ```
    
2. **Crafting the Counter**:
    
    The core of our program is the **`countErrors`** function. This function opens the log file, reads it line by line, and counts lines that start with "ERROR".
    
    ```go
    func countErrors(filename string) (int, error) {
        file, err := os.Open(filename)
        if err != nil {
            return 0, err
        }
        defer file.Close()
    
        scanner := bufio.NewScanner(file)
        errorCount := 0
    
        for scanner.Scan() {
            line := scanner.Text()
            if strings.HasPrefix(line, "ERROR") {
                errorCount++
            }
        }
    
        if err := scanner.Err(); err != nil {
            return 0, err
        }
    
        return errorCount, nil
    }
    ```
    
3. **Demonstrating the Counter**:
    
    To showcase our log counter, the **`main`** function invokes **`countErrors`** and prints the result:
    
    ```go
    func main() {
        filename := "sample.log"
        count, err := countErrors(filename)
        if err != nil {
            fmt.Println("Error:", err)
            return
        }
    
        fmt.Printf("Number of error messages in %s: %d\n", filename, count)
    }
    ```
    
4. **Running the Program**:
    
    To see the log counter in action, navigate to the directory containing the Go file and execute:
    
    ```bash
    bashCopy code
    go run logcounter.go
    ```
    
    The output will display the number of error messages in the log file.
    

### **Conclusion**

With just a few lines of Go code, we've built a robust log counter. This exercise not only demonstrates Go's prowess in file handling but also highlights its string manipulation capabilities. As you delve deeper into Go, you'll discover its vast potential in various domains, from web development to data processing and beyond.