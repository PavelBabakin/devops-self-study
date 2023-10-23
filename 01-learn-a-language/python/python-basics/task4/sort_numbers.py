def sort_numbers(numbers):
    """
    Sorts a list of numbers in ascending order.

    Args:
    - numbers (list): A list of numbers to be sorted.

    Returns:
    - list: A sorted list of numbers.
    """
    return sorted(numbers)

def main():
    # Sample list of numbers
    numbers = [23, 1, 4, 67, 32, 98, 12, 7]

    # Sort the numbers
    sorted_numbers = sort_numbers(numbers)

    # Display the sorted numbers
    print(f"Original List: {numbers}")
    print(f"Sorted List: {sorted_numbers}")

if __name__ == "__main__":
    main()
