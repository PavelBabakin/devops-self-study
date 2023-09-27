# Task 5: Use Go's map data structure to count the frequency of words in a text.

## **Counting Word Frequencies in Go: A Dive into Maps**

Go, often referred to as Golang, is a statically typed, compiled language known for its simplicity, efficiency, and powerful standard library. One of the versatile data structures provided by Go is the map, which can be likened to dictionaries in Python or objects in JavaScript. In this tutorial, we'll harness the power of maps to count the frequency of words in a given text.

### **Harnessing Go's Map for Word Counting**

Maps in Go are a collection of key-value pairs. They're incredibly efficient for tasks like counting occurrences, as we can use the unique word as the key and its frequency as the value.

1. **Crafting the Word Counter**:
    
    Start by creating a new Go file, say **`wordcount.go`**. In this file, we'll define a function, **`wordFrequency`**, which will take a string as input and return a map with words as keys and their frequencies as values.
    
    ```go
    package main
    
    import (
        "fmt"
        "strings"
    )
    
    func wordFrequency(text string) map[string]int {
        wordCounts := make(map[string]int)
        words := strings.Fields(text)
    
        for _, word := range words {
            word = strings.ToLower(word)
            word = strings.Trim(word, ".,!?()[]{}\"")
            wordCounts[word]++
        }
    
        return wordCounts
    }
    ```
    
    The function begins by initializing an empty map. It then splits the input text into words and iterates over each word. For each word, it converts it to lowercase and trims any punctuation. It then increments the word's count in the map.
    
2. **Demonstrating the Word Counter**:
    
    To see our word counter in action, we'll add a **`main`** function:
    
    ```go
    func main() {
        text := "This is a sample text. This text contains some sample words. Words like sample, text, and this."
        frequencies := wordFrequency(text)
    
        fmt.Println("Word Frequencies:")
        for word, count := range frequencies {
            fmt.Printf("%s: %d\n", word, count)
        }
    }
    ```
    
    This function sets a sample text, calls our **`wordFrequency`** function, and then prints out the word frequencies.
    
3. **Running the Word Counter**:
    
    With the program ready, navigate to the directory containing **`wordcount.go`** in your terminal and execute:
    
    ```bash
    go run wordcount.go
    ```
    
    The output will display the frequency of each word in the sample text.
    

### **Conclusion**

With just a few lines of Go code, you've crafted a robust word counter using the map data structure. This exercise not only showcases the power of maps in Go but also introduces you to some of Go's string manipulation capabilities. As you continue exploring Go, you'll find that its combination of simplicity and power makes it a top choice for a wide range of applications, from web servers to data processing pipelines.