import mysql.connector
import psycopg2
from pymongo import MongoClient
import redis
import json
import sys

def fill_mysql():
    try:
        num = 0
        with open("users.json", "r") as file:
            users = json.loads(file.read())
            db = mysql.connector.connect(
                host="localhost",
                user="<username>",
                password="<password>", 
                database="usersdb"
            )

            with db.cursor() as cursor:
                for user in users:
                    command = "INSERT INTO users (fname, lname, email, gender) VALUES ('" + user["fname"] + "', '" + user["lname"] + "', '" + user["email"] + "', '" + user["gender"] + "')"
                    cursor.execute(command)
                    db.commit()
                    print("[" + str(num) + "] " + str(user))
                    num += 1
            db.close()
    except Exception as ex:
        print(ex)
        return False

def fill_postgres():
    try:
        num = 0
        with open("users.json", "r") as file:
            users = json.loads(file.read())
            db = psycopg2.connect(
                host="localhost",
                user="<username>",
                password="<password>", 
                database="usersdb"
            )

            with db.cursor() as cursor:
                for user in users:
                    command = "INSERT INTO users (fname, lname, email, gender) VALUES ('" + user["fname"] + "', '" + user["lname"] + "', '" + user["email"] + "', '" + user["gender"] + "')"
                    cursor.execute(command)
                    db.commit()
                    print("[" + str(num) + "] " + str(user))
                    num += 1
            db.close()
    except Exception as ex:
        print(ex)
        return False

def fill_mongos(db_name, collection_name):
    try:
        num = 0
        connection_string = "mongodb://<username>:<password>@127.0.0.1/" + db_name
        with open("users.json", "r") as file:
            users = json.loads(file.read())
            client = MongoClient(connection_string)
            db = client.get_database(db_name)
            collection = db.get_collection(collection_name)
            for user in users:
                out = collection.insert_one(user)
                print(out)
                print("[" + str(num) + "] " + str(user))
                num += 1
    except Exception as ex:
        print(ex)
        return False

def fill_redis():
    try:
        num = 0
        r_host = "127.0.0.1"
        r_port = 6379
        with open("users.json", "r") as file:
            users = json.loads(file.read())
            rd = redis.StrictRedis(host = r_host, port = r_port, decode_responses = True)
            for user in users:
                rd.set(num, str(user))
                print("[" + str(num) + "] " + str(user))
                num += 1
    except Exception as ex:
        print(ex)
        return False


if __name__ == "__main__":
    if sys.argv[1] == "mysql":
        fill_mysql()
    elif sys.argv[1] == "psql":
        fill_postgres()
    elif sys.argv[1] == "mongos":
        fill_mongos("usersdb", "users")
    elif sys.argv[1] == "redis":
        fill_redis()
    else:
        print(f"Wrong argument code {sys.argv[1]}.")
