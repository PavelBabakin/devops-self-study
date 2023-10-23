package main

import (
	"fmt"
)

type AppError struct {
	Code    int
	Message string
}

func (e *AppError) Error() string {
	return fmt.Sprintf("AppError [Code: %d, Message: %s]", e.Code, e.Message)
}
