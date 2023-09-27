# Task 8: Use the os package to gather system information like OS type, disk usage, and environment variables.

## **Gathering System Information with Go**

In the realm of DevOps and system administration, having the ability to quickly gather system information is invaluable. Whether it's for troubleshooting, monitoring, or auditing, understanding the state of your system is crucial. While there are many tools available for this purpose, creating a custom utility tailored to your needs can be beneficial. In this tutorial, we'll explore how to use Go (or Golang) to gather essential system information.

### **Why Go for System Information?**

Go offers a comprehensive standard library that provides native support for many system-related tasks. Its efficient runtime, combined with its straightforward syntax, makes it an excellent choice for building utilities and CLI tools.

### **Building the System Information Utility in Go**

1. **Fetching the OS Type**:
    
    Go's **`runtime`** package allows us to determine the type of operating system on which our program is running. With a simple call to **`runtime.GOOS`**, we can fetch the OS type.
    
    ```go
    osType := runtime.GOOS
    fmt.Println("Operating System:", osType)
    ```
    
2. **Determining Disk Usage**:
    
    To get the disk usage, we use the **`syscall`** package. Specifically, the **`Statfs`** function provides details about the file system, including total and free space.
    
    ```go
    fs := syscall.Statfs_t{}
    err := syscall.Statfs("/", &fs)
    // ... (code to handle error and display disk usage)
    ```
    
3. **Listing Environment Variables**:
    
    The **`os`** package in Go provides the **`Environ`** function, which returns a slice of strings representing the environment, in the form "key=value".
    
    ```go
    envVars := os.Environ()
    for _, env := range envVars {
        fmt.Println(env)
    }
    ```
    
4. **Running the Utility**:
    
    After writing the utility, you can execute it using the **`go run`** command. This will display the gathered system information in the terminal.
    
    ```bash
    go run sysinfo.go
    ```
    

### **Conclusion**

With Go's rich standard library, creating a system information utility is a breeze. This exercise not only showcases Go's capabilities in system interactions but also demonstrates its potential as a go-to language for building utilities and tools. As you continue your journey with Go, you'll discover its vast potential in various domains, from system utilities to web applications and beyond.