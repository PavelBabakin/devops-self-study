# Task 14: Sort and filter unique lines in a file with sort and uniq.

Hello, dear readers! Today, we're focusing on two essential text processing commands that often go hand in hand: **`sort`** and **`uniq`**. When dealing with large datasets, logs, or any text files, the ability to sort data and filter out duplicates can be incredibly useful. Let's delve into how you can utilize these tools to bring order and uniqueness to your data.

### 1. **`sort` (Order Lines in Text Files)**

The **`sort`** command arranges lines in a text file either in ascending or descending order, based on various criteria.

**Usage**:

```bash
sort [options] [file...]
```

**Key Features**:

- **Alphanumeric Sorting**: By default, **`sort`** arranges lines alphanumerically.
- **Custom Sorting**: You can sort based on specific columns, numeric values, and more.

**Examples**:

- Sort a file in ascending order:
    
    ```bash
    sort file.txt
    ```
    
- Sort a file in descending order:
    
    ```bash
    sort -r file.txt
    ```
    
- Sort a file based on the second column (assuming space-separated values):
    
    ```bash
    sort -k2 file.txt
    ```
    

### 2. **`uniq` (Report or Omit Repeated Lines)**

The **`uniq`** command is used to filter out repeated lines in a sorted file. It's often used in conjunction with **`sort`**.

**Usage**:

```bash
uniq [options] [input [output]]
```

**Key Features**:

- **Remove Duplicates**: By default, **`uniq`** removes duplicate adjacent lines.
- **Count Occurrences**: You can use **`uniq`** to count how many times each line appears.

**Examples**:

- Filter out duplicate lines:
    
    ```bash
    sort file.txt | uniq
    ```
    
- Count occurrences of each line:
    
    ```bash
    sort file.txt | uniq -c
    ```
    

### **Combining `sort` and `uniq`:**

One of the most common use cases is to combine **`sort`** and **`uniq`** to sort data and then remove duplicates. Here's how you can achieve this:

- Sort a file and remove duplicates:
    
    ```bash
    sort file.txt | uniq > sorted_unique.txt
    ```
    
- Find the most common lines in a file:
    
    ```bash
    sort file.txt | uniq -c | sort -nr
    ```
    

### **Tips for Effective Data Processing:**

1. **Always Sort Before Using `uniq`**: The **`uniq`** command works on adjacent lines, so always ensure your data is sorted before using it.
2. **Explore Other Options**: Both **`sort`** and **`uniq`** come with a plethora of options. Explore the man pages (**`man sort`** and **`man uniq`**) to discover more functionalities.
3. **Large Datasets**: For very large datasets, consider tools like **`awk`** for more advanced processing or scripting to automate repetitive tasks.

### **Conclusion**

The ability to sort and filter data is fundamental when working with text files. With **`sort`** and **`uniq`**, you can easily bring order to your data and ensure uniqueness. These tools, while simple, are powerful and form the backbone of many text processing tasks. In our upcoming articles, we'll delve deeper into more advanced topics and tools. Stay tuned!