# Task 19: Use Python decorators to measure the execution time of your functions.

## **Harnessing Python Decorators for Precise Function Timing**

In the vast landscape of programming, the efficiency of code often takes center stage. For developers, understanding the duration a particular function takes to execute can be the difference between a snappy application and a sluggish one. Python, renowned for its versatility, offers an elegant mechanism to gauge this: decorators. In this guide, we'll walk through creating a decorator to measure the execution time of any function.

### **Diving into Decorators**

Decorators in Python are a design pattern that allows the addition of new functionality to an existing object without altering its structure. Essentially, they are a powerful tool that enables the modification of function or class behaviors seamlessly.

### **Crafting Our Timing Decorator**

**Filename:** **`timing_decorator.py`**

```python
import time

def time_it(func):
    """
    A decorator function to measure the time taken
    by a function to execute.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper
```

This decorator, when applied, will print the time taken by the decorated function to execute.

### **Implementing the Decorator**

**Filename:** **`main.py`**

```python
from timing_decorator import time_it
import time

@time_it
def some_function():
    """A sample function that simulates a 2-second delay."""
    time.sleep(2)
    print("Function executed!")

some_function()
```

### **How to Run the Code**

1. Ensure both **`timing_decorator.py`** and **`main.py`** are in the same directory.
2. Open your terminal or command prompt and navigate to the directory containing the files.
3. Execute the **`main.py`** script:

```bash
$ python3 main.py
```

Upon running, you should witness an output akin to:

```bash
Function executed!
some_function executed in 2.0021 seconds
```

### **The Power of Decorators**

- **Modularity**: By segregating the timing logic from the primary function, our code remains modular.
- **Reusability**: The timing decorator is versatile and can be applied to numerous functions.
- **Clarity**: The code remains uncluttered from timing logistics, ensuring it's more legible.

### **Wrapping Up**

Python's decorators are a testament to the language's commitment to clean and efficient coding. By leveraging them, developers can embed auxiliary functionalities like precise timing into functions, ensuring they have a clear understanding of their code's performance.