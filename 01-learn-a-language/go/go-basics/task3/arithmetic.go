package main

import (
	"fmt"
)

func main() {
	var num1, num2 float64
	var operation string

	fmt.Print("Enter first number: ")
	fmt.Scan(&num1)

	fmt.Print("Enter second number: ")
	fmt.Scan(&num2)

	fmt.Print("Enter operation (+, -, *, /): ")
	fmt.Scan(&operation)

	switch operation {
	case "+":
		fmt.Printf("Result: %f\n", num1+num2)
	case "-":
		fmt.Printf("Result: %f\n", num1-num2)
	case "*":
		fmt.Printf("Result: %f\n", num1*num2)
	case "/":
		if num2 != 0 {
			fmt.Printf("Result: %f\n", num1/num2)
		} else {
			fmt.Println("Error: Division by zero.")
		}
	default:
		fmt.Println("Invalid operation.")
	}
}
