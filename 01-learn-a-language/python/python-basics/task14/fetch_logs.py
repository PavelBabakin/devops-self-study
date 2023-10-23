import sqlite3

def fetch_logs():
    conn = sqlite3.connect('server_logs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, log_message FROM logs")
    logs = cursor.fetchall()
    conn.close()
    return logs

# Display the logs
for log in fetch_logs():
    print(f"[{log[0]}] {log[1]}")