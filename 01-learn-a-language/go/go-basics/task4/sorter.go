package main

import (
	"fmt"
	"sort"
)

// sortIntegers sorts a slice of integers in ascending order.
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
