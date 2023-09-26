import sqlite3
import datetime

def fetch_logs_by_date(start_date, end_date):
    # Connect to the database
    conn = sqlite3.connect('server_logs.db')
    cursor = conn.cursor()

    # Convert the dates to string format for comparison
    start_date_str = start_date.strftime('%Y-%m-%d %H:%M:%S')
    end_date_str = end_date.strftime('%Y-%m-%d %H:%M:%S')

    # Fetch logs within the date range
    cursor.execute("SELECT timestamp, log_message FROM logs WHERE timestamp BETWEEN ? AND ?", (start_date_str, end_date_str))
    logs = cursor.fetchall()

    # Close the connection
    conn.close()

    return logs

# Example usage:
start_date = datetime.datetime(2022, 9, 1)  # 1st September 2022
end_date = datetime.datetime(2022, 9, 30)   # 30th September 2022

for log in fetch_logs_by_date(start_date, end_date):
    print(f"[{log[0]}] {log[1]}")