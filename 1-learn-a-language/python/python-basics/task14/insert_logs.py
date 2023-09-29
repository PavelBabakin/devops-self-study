import sqlite3
import datetime

def insert_log(log_message):
    conn = sqlite3.connect('server_logs.db')
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO logs (timestamp, log_message) VALUES (?, ?)", (timestamp, log_message))
    conn.commit()
    conn.close()

# Example usage:
insert_log("Server started successfully.")