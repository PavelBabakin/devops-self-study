package main

import (
	"fmt"
	"time"
)

func sendData(ch chan string) {
	time.Sleep(1 * time.Second)
	ch <- "Hello from sendData goroutine!"
}

func main() {
	messageChannel := make(chan string)

	go sendData(messageChannel)

	message := <-messageChannel
	fmt.Println("Received:", message)
}
