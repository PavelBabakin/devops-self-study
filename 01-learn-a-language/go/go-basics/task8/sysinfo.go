package main

import (
	"fmt"
	"os"
	"runtime"
	"syscall"
)

func main() {
	// OS Type
	osType := runtime.GOOS
	fmt.Println("Operating System:", osType)

	// Disk Usage
	fs := syscall.Statfs_t{}
	err := syscall.Statfs("/", &fs)
	if err != nil {
		fmt.Println("Error fetching disk usage:", err)
		return
	}
	totalSpace := fs.Blocks * uint64(fs.Bsize)
	freeSpace := fs.Bfree * uint64(fs.Bsize)
	fmt.Printf("Total Disk Space: %d bytes\n", totalSpace)
	fmt.Printf("Free Disk Space: %d bytes\n", freeSpace)

	// Environment Variables
	envVars := os.Environ()
	fmt.Println("Environment Variables:")
	for _, env := range envVars {
		fmt.Println(env)
	}
}
