# Task 15: Write a Go utility to query the database and fetch logs for a specific date range.

## **Fetching Logs from a Database Based on Date Range using Go**

In the realm of DevOps, logs are crucial. They provide insights into system behavior, help diagnose issues, and can be used for analytics. As systems grow and logs accumulate, it becomes essential to query logs based on specific criteria, such as date ranges. In this article, we'll explore how to use Go (Golang) to fetch logs from a MySQL database for a specific date range.

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

Create a new file named **`query_logs.go`**. This file will contain our utility program.

```go
package main

import (
    "database/sql"
    "fmt"
    "log"
    _ "github.com/go-sql-driver/mysql"
)

func fetchLogsByDateRange(db *sql.DB, startDate, endDate string) {
    rows, err := db.Query("SELECT log_message, log_time FROM server_logs WHERE log_time BETWEEN ? AND ?", startDate, endDate)
    if err != nil {
        log.Fatal(err)
    }
    defer rows.Close()

    fmt.Println("Logs between", startDate, "and", endDate, ":")
    for rows.Next() {
        var logMessage string
        var logTime string
        if err := rows.Scan(&logMessage, &logTime); err != nil {
            log.Fatal(err)
        }
        fmt.Printf("Time: %s, Message: %s\n", logTime, logMessage)
    }
}

func main() {
    // Connect to the database
    db, err := sql.Open("mysql", "username:password@tcp(127.0.0.1:3306)/dbname")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    // Fetch logs for a specific date range
    fetchLogsByDateRange(db, "2022-01-01", "2022-12-31")
}
```

Replace **`username`**, **`password`**, and **`dbname`** with your MySQL credentials and the desired database name.

### **Step 3: Running the Go Code**

Navigate to the directory containing **`query_logs.go`** and execute:

```bash
go run query_logs.go
```

Upon successful execution, you should see the logs within the specified date range printed to the console.

### **Step 4: Customizing the Date Range**

To fetch logs for a different date range, simply modify the **`fetchLogsByDateRange`** function call in the **`main`** function with the desired start and end dates.

### **Conclusion**

Using Go to query logs based on date ranges is efficient and straightforward. This utility can be a valuable tool for system administrators, DevOps engineers, and anyone who needs to analyze logs based on specific criteria. Whether you're troubleshooting an issue or analyzing system behavior over time, this Go utility can help streamline the process.