# Task 14: Use a Go SQL package (like database/sql with an appropriate driver) to connect to a local database, add a table for storing server logs, and insert logs into the database.

## **Using Go to Connect to a Database and Insert Logs**

In the world of DevOps, automation is key. Whether it's automating deployment pipelines or infrastructure provisioning, the ability to automate tasks can greatly enhance productivity. One such task that often needs automation is logging. In this article, we'll explore how to use Go (Golang) to connect to a MySQL database and insert logs.

### **Prerequisites:**

- Go installed on your machine.
- MySQL installed and running.
- Basic understanding of Go syntax and SQL.

### **Step 1: Setting Up the Go Environment**

Before diving into the code, ensure you have the necessary Go package to interact with MySQL:

```bash
go get -u github.com/go-sql-driver/mysql
```

This command fetches the MySQL driver for Go, allowing our program to communicate with MySQL databases.

### **Step 2: Writing the Go Code**

Create a new file named **`database.go`**. This file will contain our main program.

```go
package main

import (
    "database/sql"
    "fmt"
    "log"
    _ "github.com/go-sql-driver/mysql"
)

func main() {
    // Connect to the database
    db, err := sql.Open("mysql", "username:password@tcp(127.0.0.1:3306)/dbname")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // Create a table for storing server logs
    _, err = db.Exec(`CREATE TABLE IF NOT EXISTS server_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        log_message TEXT NOT NULL,
        log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )`)
    if err != nil {
        log.Fatal(err)
    }

    // Insert a log into the database
    _, err = db.Exec("INSERT INTO server_logs (log_message) VALUES (?)", "This is a test log message.")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("Log inserted successfully!")
}
```

Replace **`username`**, **`password`**, and **`dbname`** with your MySQL credentials and the desired database name.

### **Step 3: Running the Go Code**

Navigate to the directory containing **`database.go`** and execute:

```bash
go run database.go
```

Upon successful execution, you should see the message "Log inserted successfully!" This indicates that a log message has been inserted into the **`server_logs`** table in your MySQL database.

### **Step 4: Verifying the Insertion**

To confirm that the log has been inserted, access your MySQL database and execute:

```sql
SELECT * FROM server_logs;
```

You should see the log message "This is a test log message." along with its timestamp.

### **Conclusion**

Using Go to interact with databases is straightforward and efficient. With just a few lines of code, we've established a connection to a MySQL database, created a table, and inserted a log message. This approach can be expanded to handle more complex logging requirements, making Go a valuable tool in the DevOps toolkit.