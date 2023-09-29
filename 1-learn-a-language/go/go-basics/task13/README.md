# Task 13: Extend your web server to include an API endpoint that returns system information in JSON format.

### **Building a Go Web Server to Display System Information**

Go, also known as Golang, is a statically typed, compiled language designed for simplicity and efficiency. One of its strengths is building web servers and APIs. In this article, we'll create a basic web server using Go that displays system information in both plain text and JSON format.

### **Prerequisites**:

- Go installed on your machine.
- Basic understanding of Go syntax.

### **Step-by-Step Guide**:

1. **Setting Up the Web Server**:
    
    Start by creating a new file named **`webserver.go`**. This file will contain all the code for our web server.
    
2. **Displaying System Information in Plain Text**:
    
    We'll first create a handler function that displays system information in plain text:
    
    ```go
    func systemInfoHandler(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Operating System: %s\n", runtime.GOOS)
        fmt.Fprintf(w, "Architecture: %s\n", runtime.GOARCH)
        hostname, _ := os.Hostname()
        fmt.Fprintf(w, "Hostname: %s\n", hostname)
    }
    ```
    
3. **Displaying System Information in JSON Format**:
    
    Next, we'll create another handler function that returns the system information in JSON format:
    
    ```go
    func systemInfoJSONHandler(w http.ResponseWriter, r *http.Request) {
        hostname, _ := os.Hostname()
        info := map[string]string{
            "Operating System": runtime.GOOS,
            "Architecture":    runtime.GOARCH,
            "Hostname":        hostname,
        }
    
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(info)
    }
    ```
    
4. **Starting the Web Server**:
    
    In the **`main()`** function, define the routes for the handlers and start the web server:
    
    ```go
    func main() {
        http.HandleFunc("/systeminfo", systemInfoHandler)
        http.HandleFunc("/api/systeminfo", systemInfoJSONHandler)
        http.ListenAndServe(":8080", nil)
    }
    ```
    
5. **Running the Web Server**:
    
    Navigate to the directory containing **`webserver.go`** and run:
    
    ```bash
    bashCopy code
    go run webserver.go
    
    ```
    
    Once the server is running, you can access the plain text system information at **`http://localhost:8080/systeminfo`** and the JSON formatted information at **`http://localhost:8080/api/systeminfo`**.
    

### **Conclusion**:

Building web servers in Go is straightforward and efficient. With just a few lines of code, we've created a web server that displays system information in two different formats. As you delve deeper into Go, you'll discover its power and versatility in building web applications and services.