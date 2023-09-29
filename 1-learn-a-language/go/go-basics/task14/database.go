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
