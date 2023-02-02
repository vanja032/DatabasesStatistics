import mysql.connector
import psycopg2
import json
import sys

def fill_mysql():
    with open("users.json", "r") as file:
        users = json.loads(file.read())
        db = mysql.connector.connect(
            host="localhost",
            user="user",
            password="useruser", 
            database="usersdb"
        )

        with db.cursor() as cursor:
            for user in users:
                command = "INSERT INTO users (fname, lname, email, gender) VALUES ('" + user["fname"] + "', '" + user["lname"] + "', '" + user["email"] + "', '" + user["gender"] + "')"
                cursor.execute(command)
                db.commit()
                print(user)
        db.close()

def fill_postgres():
    with open("users.json", "r") as file:
        users = json.loads(file.read())
        db = psycopg2.connect(
            host="localhost",
            user="root",
            password="root", 
            database="usersdb"
        )

        with db.cursor() as cursor:
            for user in users:
                command = "INSERT INTO users (fname, lname, email, gender) VALUES ('" + user["fname"] + "', '" + user["lname"] + "', '" + user["email"] + "', '" + user["gender"] + "')"
                cursor.execute(command)
                db.commit()
                print(user)
        db.close()

if __name__ == "__main__":
    if sys.argv[1] == "mysql":
        fill_mysql()
    elif sys.argv[1] == "psql":
        fill_postgres()
    else:
        print(f"Wrong argument code {sys.argv[1]}.")