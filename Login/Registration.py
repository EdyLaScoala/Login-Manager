import sqlite3
from SQLite.connection import createTable
import bcrypt

# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

createTable()


def registerUser():
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")
    secondpass = input("Please re-enter the password: ")

    salt = bcrypt.gensalt()

    if bcrypt.hashpw(password.encode('utf-8'), salt) == bcrypt.hashpw(secondpass.encode('utf-8'), salt) :
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        cursor.execute('INSERT INTO users (username, hashed_password, salt) VALUES (?, ?, ?)',
                       (username, hashed_password.decode('utf-8'), salt.decode('utf-8')))
        conn.commit()
        return True
    else:
        print("Passwords do not match. Please try again.\n")
        registerUser()

def loginUser():
    username = input("Please enter the username: ")
    cursor.execute('SELECT salt FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    if not row:
        response = input("User not found. Do you want to create an account now?\n")
        if response == "yes":
            registerUser()
        else:
            print("Ok.\n")
            loginUser()
            return True

    password = input("Please enter the password: ")

    # Query the database to check if the user exists
    cursor.execute('SELECT hashed_password, salt FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    hashed_password = row[0].encode('utf-8')
    salt = row[1].encode('utf-8')

    # Verify the password by hashing it with the retrieved salt
    if bcrypt.hashpw(password.encode('utf-8'), salt) == hashed_password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password. Please try again.")
        loginUser()





def verifyPassword(username, password):
    # Retrieve the hashed password and salt from the database
    cursor.execute('SELECT hashed_password, salt FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    if row:
        hashed_password = row[0].encode('utf-8')
        salt = row[1].encode('utf-8')

        # Verify the password by hashing it with the retrieved salt
        return bcrypt.hashpw(password.encode('utf-8'), salt) == hashed_password
    else:
        return False

