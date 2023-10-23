package main

func divide(a, b int) (int, error) {
	if b == 0 {
		return 0, &AppError{
			Code:    400,
			Message: "Division by zero is not allowed",
		}
	}
	return a / b, nil
}
