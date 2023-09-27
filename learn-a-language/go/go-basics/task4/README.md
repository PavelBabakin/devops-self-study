# Task 4: Implement a Go function to sort a slice of integers.

## **Sorting Integers in Go: A Simple Guide**

Go, affectionately known as Golang, is a statically typed, compiled language known for its simplicity and efficiency. In this tutorial, we'll delve into one of the foundational concepts in programming: sorting a list of numbers. Specifically, we'll be sorting a slice of integers using Go.

### **Creating a Simple Integer Sorter in Go**

1. **Setting Up the Project**:
    
    Start by creating a new directory for your Go project:
    
    ```bash
    mkdir go-sort && cd go-sort
    ```
    
    Within this directory, create a new Go file named **`sorter.go`**:
    
    ```bash
    touch sorter.go
    ```
    
2. **Crafting the Integer Sorter**:
    
    Open the **`sorter.go`** file in your preferred text editor and input the following code:
    
    ```go
    package main
    
    import (
        "fmt"
        "sort"
    )
    
    // sortIntegers sorts a slice of integers in ascending order without modifying the original slice.
    func sortIntegers(nums []int) []int {
        sortedNums := make([]int, len(nums))
        copy(sortedNums, nums)
        sort.Ints(sortedNums)
        return sortedNums
    }
    
    func main() {
        numbers := []int{42, 23, 16, 8, 15}
        sortedNumbers := sortIntegers(numbers)
    
        fmt.Println("Original Numbers:", numbers)
        fmt.Println("Sorted Numbers:", sortedNumbers)
    }
    ```
    
    This code defines a function, **`sortIntegers`**, which takes a slice of integers as input. It then creates a copy of this slice, sorts it in ascending order, and returns the sorted slice. The **`main`** function demonstrates the usage of this sorting function.
    
3. **Running the Integer Sorter**:
    
    In your terminal, navigate to the directory containing **`sorter.go`**. Execute the program with:
    
    ```bash
    go run sorter.go
    ```
    
    You should see the output displaying both the original and sorted slices of numbers.
    

### **Conclusion**

With just a few lines of Go code, you've built a basic integer sorter. This exercise introduces you to Go's built-in **`sort`** package and showcases how to define and use functions in Go. As you continue your journey with Go, you'll encounter more advanced topics and functionalities that will further enhance your programming skills. Whether you're a seasoned developer or just starting out, Go offers a plethora of opportunities to build efficient and scalable applications.