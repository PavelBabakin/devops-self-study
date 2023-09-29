# Task 19: Use Go's defer statement to ensure resources (like files or database connections) are properly closed after usage.

### **Resource Management in Go with the `defer` Statement**

In the world of programming, managing resources efficiently is crucial. Whether it's file handling, database connections, or network sockets, ensuring that resources are allocated and deallocated properly can prevent potential issues like memory leaks or system crashes. Go, with its simplicity and efficiency, provides a powerful tool for this: the **`defer`** statement.

### **Understanding the `defer` Mechanism**

The **`defer`** keyword in Go allows developers to schedule functions to be executed after the surrounding function completes. This can be either after a normal return or in the event of a panic. The primary use case for **`defer`** is to perform cleanup actions, ensuring resources are released properly.

### **Ensuring Files Are Closed Properly**

One of the most common scenarios where **`defer`** proves invaluable is file handling. When reading or writing to files, it's essential to close them afterward. With **`defer`**, this becomes straightforward:

```go
file, err := os.Open("sample.txt")
if err != nil {
    log.Fatal(err)
}
defer file.Close()

// ... file operations ...

// File will be closed automatically when the function exits.
```

By placing the **`defer file.Close()`** statement immediately after opening the file, we ensure the file will be closed, regardless of how the function exits.

### **Database Connections and `defer`**

Another typical use case is with database operations. After performing database tasks, connections should be closed to free up resources:

```go
db, err := hypothetical_db_package.Connect("your_connection_string")
if err != nil {
    log.Fatal(err)
}
defer db.Close()

// ... database operations ...

// Database connection will be closed automatically when the function exits.
```

The **`defer db.Close()`** statement guarantees the database connection's closure, ensuring efficient resource management.

### **The Order of Execution**

It's worth noting that if multiple **`defer`** statements exist in a function, they are executed in a LIFO (Last In, First Out) manner. This stacking behavior can be useful in scenarios where the order of cleanup is essential.

### **Conclusion**

The **`defer`** statement in Go is more than just a convenience; it's a powerful tool for writing clean, efficient, and error-resistant code. By ensuring resources are properly closed or deallocated, developers can prevent many common issues and ensure their applications run smoothly. As you delve deeper into Go, make **`defer`** your ally in crafting robust and efficient software.