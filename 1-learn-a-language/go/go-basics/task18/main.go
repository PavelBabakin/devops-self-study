package main

import (
	"fmt"
)

func main() {
	result, err := divide(10, 0)
	if err != nil {
		if appErr, ok := err.(*AppError); ok {
			fmt.Printf("Custom error occurred: %s\n", appErr.Error())
		} else {
			fmt.Println(err)
		}
	} else {
		fmt.Printf("Result: %d\n", result)
	}
}
