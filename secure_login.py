import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter Username: ").strip()
password = input("Enter Password: ").strip()

# Input Validation
if not username or not password:
    print("Username and Password cannot be empty.")
    exit()

# Hash Password
hashed_password = hashlib.sha256(password.encode()).hexdigest()

try:
    # Parameterized Query (Prevents SQL Injection)
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, hashed_password)
    )

    user = cursor.fetchone()

    if user:
        print("Login Successful!")
    else:
        print("Invalid Username or Password.")

except sqlite3.Error:
    # Generic error message
    print("An unexpected error occurred. Please try again later.")

finally:
    conn.close()