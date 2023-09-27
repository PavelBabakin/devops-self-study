# Task 12: Create a basic web server using Go's net/http package that displays system information.

## **Building a Basic Web Server in Go to Display System Information**

In today's interconnected world, web servers play a crucial role in delivering content and services to users. Go, with its simplicity and efficiency, has become a popular choice for building web servers. In this article, we'll walk through creating a basic web server in Go that displays system information.

### **Why Go for Web Servers?**

Go, often referred to as Golang, offers several advantages for web development:

- **Concurrency**: Go's goroutines and channels make it easy to handle multiple tasks simultaneously.
- **Standard Library**: Go's standard library, especially the **`net/http`** package, provides robust tools for building web servers and clients.
- **Performance**: Go is a compiled language, which often results in faster execution times compared to interpreted languages.

### **Creating a Web Server in Go**

To demonstrate, we'll build a simple web server that displays the operating system, architecture, and hostname.

1. **Setting Up**:
    
    Start by creating a directory for your Go project:
    
    ```bash
    mkdir go-webserver-demo && cd go-webserver-demo
    ```
    
2. **The Code**:
    
    In the project directory, create a file named **`webserver.go`** and add the following code:
    
    ```go
    package main
    
    import (
        "fmt"
        "net/http"
        "os"
        "runtime"
    )
    
    func systemInfoHandler(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Operating System: %s\n", runtime.GOOS)
        fmt.Fprintf(w, "Architecture: %s\n", runtime.GOARCH)
        hostname, _ := os.Hostname()
        fmt.Fprintf(w, "Hostname: %s\n", hostname)
    }
    
    func main() {
        http.HandleFunc("/systeminfo", systemInfoHandler)
        http.ListenAndServe(":8080", nil)
    }
    ```
    
    This code sets up a basic web server that listens on port 8080. When a user navigates to **`/systeminfo`**, the server responds with details about the operating system, architecture, and hostname.
    
3. **Running the Server**:
    
    To run the server, navigate to the project directory in your terminal and execute:
    
    ```bash
    go run webserver.go
    ```
    
    Once the server is up, open a web browser and visit **`http://localhost:8080/systeminfo`** to view the system details.
    

### **Conclusion**

Building a web server in Go is straightforward, thanks to its powerful standard library and intuitive syntax. The example we explored is a basic demonstration, but Go is capable of powering complex web applications and services. As you delve deeper into Go web development, you'll discover its potential and the vast ecosystem of libraries and frameworks available to support your projects.