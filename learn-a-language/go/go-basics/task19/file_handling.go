package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	// Open a file for reading
	file, err := os.Open("sample.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}

	// Schedule the file to be closed after the surrounding function completes
	defer file.Close()

	// Read the file content
	content, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println(string(content))
}
