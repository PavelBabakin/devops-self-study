# Task 16: Use conditional statements (if, else) and loops (for, while) in a script.

Hello, dear readers! Scripting is all about making decisions and automating repetitive tasks. Two fundamental constructs that enable this are conditional statements (**`if`**, **`else`**) and loops (**`for`**, **`while`**). Today, we'll delve into these constructs and see how they can be used in bash scripting to add logic and iteration to your scripts.

### **1. Conditional Statements in Bash**

Conditional statements allow your script to make decisions based on certain conditions.

**Basic `if` Statement**:

```bash
if [ condition ]; then
    # commands to execute if condition is true
fi
```

**`if-else` Statement**:

```bash
if [ condition ]; then
    # commands to execute if condition is true
else
    # commands to execute if condition is false
fi
```

**Example**:
Check if a file exists and print a message accordingly.

```bash
FILE="/path/to/file.txt"
if [ -f "$FILE" ]; then
    echo "The file $FILE exists."
else
    echo "The file $FILE does not exist."
fi
```

### **2. Loops in Bash**

Loops allow you to execute a set of commands multiple times.

**`for` Loop**:
Iterate over a sequence of numbers or items in a list.

```bash
for i in {1..5}; do
    echo "Iteration number $i"
done
```

**`while` Loop**:
Execute commands as long as a condition remains true.

```bash
count=1
while [ $count -le 5 ]; do
    echo "Iteration number $count"
    ((count++))
done
```

### **Combining Conditionals and Loops**:

Here's an example that combines both constructs. This script checks for the existence of multiple files and prints a message for each:

```bash
#!/bin/bash

# List of files to check
FILES="/path/to/file1.txt /path/to/file2.txt /path/to/file3.txt"

# Loop through each file and check for its existence
for file in $FILES; do
    if [ -f "$file" ]; then
        echo "The file $file exists."
    else
        echo "The file $file does not exist."
    fi
done
```

### **Tips for Effective Scripting with Conditionals and Loops**:

1. **Use Clear Conditions**: Ensure that the conditions in your **`if`** statements and loops are clear and understandable. This makes your script easier to read and maintain.
2. **Limit Loop Iterations**: Especially with **`while`** loops, ensure there's a clear exit condition to prevent infinite loops.
3. **Test Thoroughly**: Before deploying a script, especially one that makes changes to the system, test it thoroughly to ensure it behaves as expected.

### **Conclusion**

Conditional statements and loops are foundational constructs in bash scripting. They allow you to add logic, make decisions, and automate repetitive tasks in your scripts. By mastering these constructs, you can write more powerful and efficient scripts to handle a wide range of tasks. In our upcoming articles, we'll delve deeper into more advanced scripting topics. Stay tuned!