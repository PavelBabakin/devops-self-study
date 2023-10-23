# Task 15: Write a basic bash script to automate a repetitive task, such as cleaning up old log files.

Hello, dear readers! Automation is a cornerstone of efficient system administration and DevOps practices. Today, we'll explore how to write a basic bash script to automate a common task: cleaning up old log files. This can help free up disk space and ensure your system remains organized. Let's get started!

### **Creating a Bash Script**

1. **Script Header**:
Every bash script should start with a shebang (**`#!`**) followed by the path to the bash interpreter. This tells the system that the script should be executed with bash.
    
    ```bash
    #!/bin/bash
    ```
    
2. **Comments**:
Use the **`#`** symbol to add comments to your script. Comments help explain the purpose and functionality of your code.

### **Automating Log Cleanup**

Here's a basic script to clean up log files older than 30 days from a specified directory:

```bash
bashCopy code
#!/bin/bash

# Directory containing log files
LOG_DIR="/var/log/myapp/"

# Number of days to retain log files
RETENTION_DAYS=30

# Print starting message
echo "Starting cleanup of old log files in $LOG_DIR..."

# Find and delete log files older than the specified retention period
find "$LOG_DIR" -name "*.log" -type f -mtime +$RETENTION_DAYS -exec rm -f {} \;

# Print completion message
echo "Cleanup completed. Old log files older than $RETENTION_DAYS days have been deleted."
```

### **How the Script Works**:

1. **Variables**: The script defines two variables: **`LOG_DIR`** (the directory containing the log files) and **`RETENTION_DAYS`** (the number of days to retain log files).
2. **`find` Command**: The script uses the **`find`** command to search for **`.log`** files in the specified directory that are older than the retention period. The **`exec`** flag is used to execute the **`rm`** command on each old log file to delete it.

### **Running the Script**:

1. **Make the Script Executable**: Before you can run the script, you need to make it executable. Assuming you saved the script as **`cleanup_logs.sh`**, you can use the following command:
    
    ```bash
    chmod +x cleanup_logs.sh
    ```
    
2. **Execute the Script**:
    
    ```bash
    ./cleanup_logs.sh
    ```
    

### **Tips for Effective Scripting**:

1. **Error Handling**: Add error handling to your scripts to manage unexpected situations. For instance, check if the log directory exists before attempting cleanup.
2. **Logging**: Instead of just printing messages to the console, consider writing them to a log file for future reference.
3. **Cron Jobs**: To automate the execution of your script, you can set it up as a cron job to run at regular intervals (e.g., daily or weekly).

### **Conclusion**

Bash scripting offers a powerful way to automate repetitive tasks, making system management more efficient. By writing scripts like the log cleanup example above, you can ensure routine tasks are handled consistently and reliably. As we continue our series, we'll explore more advanced scripting techniques and topics. Stay tuned!