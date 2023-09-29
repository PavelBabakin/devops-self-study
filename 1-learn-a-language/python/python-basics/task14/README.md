# Task 14: Use the sqlite3 library to create a local database, add a table for storing server logs, and write a script to insert logs into the database.

## **A Comprehensive Guide to Managing Server Logs with SQLite in Python on macOS**

In the realm of server management and DevOps, logging is paramount. It provides insights into server operations, helps diagnose issues, and can be crucial for security audits. While there are many logging solutions available, sometimes a lightweight, local solution is all you need. Enter SQLite, a serverless SQL database, perfect for local storage. In this article, we'll explore how to harness the power of SQLite and Python to manage server logs on macOS.

### **Why SQLite?**

SQLite offers a lightweight, serverless, self-contained, and full-featured SQL database engine. It's an excellent choice for local storage, especially when you don't need the overhead of a full server database system.

### **Setting Up Your Environment**

Before diving into the code, ensure you have Python installed on your macOS. You can check this by running:

```bash
python3 --version
```

If Python is not installed, you can install it using Homebrew:

```bash
brew install python3
```

### **Creating the Database**

**Step 1:** Create a new script named **`setup_database.py`**. This script will set up the SQLite database and create the necessary table for our logs.

**Step 2:** Run the script using:

```bash
python3 setup_database.py
```

This will create a new file named **`server_logs.db`** in the same directory, which is our SQLite database.

### **Inserting Logs**

For this, we'll use a script named **`insert_logs.py`**. This script provides a function to insert logs into our database. To add a log, simply run:

```bash
python3 insert_logs.py
```

### **Fetching and Displaying Logs**

To validate our logging system, we can fetch and display the stored logs using the **`fetch_logs.py`** script. Navigate to the directory containing the script and run:

```bash
python3 fetch_logs.py
```

### **Conclusion**

By following the steps outlined in this guide, you've set up a simple yet effective local logging system using SQLite and Python on macOS. This foundation can be expanded upon with features like log filtering, user authentication, or even integrating with web frameworks like Flask or Django for a web-based log viewer. As you delve deeper into server management and DevOps, consider the myriad ways a robust logging system can enhance your operations.