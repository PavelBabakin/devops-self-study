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
