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

func main() {
	text := "This is a sample text. This text contains some sample words. Words like sample, text, and this."
	frequencies := wordFrequency(text)

	fmt.Println("Word Frequencies:")
	for word, count := range frequencies {
		fmt.Printf("%s: %d\n", word, count)
	}
}
