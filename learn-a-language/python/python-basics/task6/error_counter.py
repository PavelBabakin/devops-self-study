def count_errors(filename):
    with open(filename, 'r') as file:
        # Read the file content
        content = file.readlines()

        # Count the error messages
        error_count = sum(1 for line in content if '[ERROR]' in line)

        return error_count

def main():
    filename = "sample_log.log"
    error_count = count_errors(filename)
    print(f"The log file contains {error_count} error messages.")

if __name__ == "__main__":
    main()