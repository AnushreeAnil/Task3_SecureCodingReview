import sqlite3

# Hardcoded credentials (Security Issue)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter Username: ")
password = input("Enter Password: ")

# Vulnerable SQL Query (SQL Injection)
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

try:
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        print("Login Successful!")
    else:
        print("Invalid Username or Password")

except Exception as e:
    # Reveals internal error details
    print("Database Error:", e)

conn.close()