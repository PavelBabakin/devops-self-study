# Task 15: Write a script to query the database and fetch logs for a specific date range.

## **Fetching Server Logs for a Specific Date Range using SQLite and Python**

In the world of server management, logs are invaluable. They provide insights, help diagnose issues, and can be crucial for security and performance audits. But as logs accumulate, sifting through them can become a daunting task. One common requirement is to fetch logs from a specific date range. In this article, we'll explore how to achieve this using SQLite and Python on macOS.

### **Why Date Range Queries Matter**

Imagine you're troubleshooting a server issue that occurred last week, or you're conducting a monthly performance review. In such scenarios, you don't need the entire log history but just a specific slice of it. Date range queries allow you to narrow down your focus and retrieve only the relevant logs, making the analysis more efficient and manageable.

### **Setting the Stage**

Before diving into the solution, ensure you have:

- Python installed on your macOS.
- An SQLite database set up with a table for logs (as discussed in our previous articles).

### **Crafting the Solution**

**1. Libraries in Play**

- **`sqlite3`**: Enables interaction with SQLite databases in Python.
- **`datetime`**: Facilitates working with dates and times.

**2. The Script**

Our solution revolves around a script named **`query_logs_by_date.py`**. This script provides a function to fetch logs from the database within a specified date range.

```python
import sqlite3
import datetime

def fetch_logs_by_date(start_date, end_date):
    conn = sqlite3.connect('server_logs.db')
    cursor = conn.cursor()
    start_date_str = start_date.strftime('%Y-%m-%d %H:%M:%S')
    end_date_str = end_date.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("SELECT timestamp, log_message FROM logs WHERE timestamp BETWEEN ? AND ?", (start_date_str, end_date_str))
    logs = cursor.fetchall()
    conn.close()
    return logs

# Example usage:
start_date = datetime.datetime(2022, 9, 1)
end_date = datetime.datetime(2022, 9, 30)
for log in fetch_logs_by_date(start_date, end_date):
    print(f"[{log[0]}] {log[1]}")
```

**3. Executing the Script**

- Save the script in a file named **`query_logs_by_date.py`**.
- Navigate to the directory containing the script using the terminal.
- Run the script with:

```bash
python3 query_logs_by_date.py
```

This will display logs from the database that fall within the specified date range.

### **Conclusion**

Date range queries are a powerful tool in the arsenal of a server administrator or DevOps engineer. By leveraging SQLite's capabilities and Python's simplicity, we can efficiently retrieve logs for specific periods, aiding in analysis and troubleshooting. As you continue your journey in server management, consider the myriad ways in which tailored log queries can enhance your operations.