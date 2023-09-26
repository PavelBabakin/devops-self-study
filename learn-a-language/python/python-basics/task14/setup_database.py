import sqlite3

# Connect to a new local database file named 'server_logs.db'
conn = sqlite3.connect('server_logs.db')
cursor = conn.cursor()

# Create a new table named 'logs'
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY,
    timestamp TEXT NOT NULL,
    log_message TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()