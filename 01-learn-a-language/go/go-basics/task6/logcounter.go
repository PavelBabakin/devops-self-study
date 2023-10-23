package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

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

func main() {
	filename := "sample.log"
	count, err := countErrors(filename)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Printf("Number of error messages in %s: %d\n", filename, count)
}
