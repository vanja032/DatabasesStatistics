import mysql.connector
import psycopg2
from pymongo import MongoClient
import redis
import json
import sys
import subprocess
import time

def get_mysql(st_data):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="<username>",
            password="<password>", 
            database="usersdb"
        )

        temp = {}

        with db.cursor() as cursor:
            start = time.time()
            command = "SELECT * FROM users LIMIT 100000"
            cursor.execute(command)
            result = cursor.fetchall()
            end = time.time()
            temp["100000"] = end - start

            start = time.time()
            command = "SELECT * FROM users LIMIT 200000"
            cursor.execute(command)
            result = cursor.fetchall()
            end = time.time()
            temp["200000"] = end - start

            start = time.time()
            command = "SELECT * FROM users LIMIT 500000"
            cursor.execute(command)
            result = cursor.fetchall()
            end = time.time()
            temp["500000"] = end - start

            start = time.time()
            command = "SELECT * FROM users LIMIT 1000000"
            cursor.execute(command)
            result = cursor.fetchall()
            end = time.time()
            temp["1000000"] = end - start

        st_data["MySql"] = temp
        db.close()
    except Exception as ex:
        print(ex)
        return False

def get_postgres(st_data):
    try:
        db = psycopg2.connect(
            host="localhost",
            user="<username>",
            password="<password>", 
            database="usersdb"
        )

        temp = {}

        with db.cursor() as cursor:
            start = time.time()
            command = "SELECT * FROM users LIMIT 100000"
            cursor.execute(command)
            result = cursor.fetchall()
            end = time.time()
            temp["100000"] = end - start

            start = time.time()
            command = "SELECT * FROM users LIMIT 200000"
            cursor.execute(command)
            result = cursor.fetchall()
            end = time.time()
            temp["200000"] = end - start

            start = time.time()
            command = "SELECT * FROM users LIMIT 500000"
            cursor.execute(command)
            result = cursor.fetchall()
            end = time.time()
            temp["500000"] = end - start

            start = time.time()
            command = "SELECT * FROM users LIMIT 1000000"
            cursor.execute(command)
            result = cursor.fetchall()
            end = time.time()
            temp["1000000"] = end - start

        st_data["Postgres"] = temp
        db.close()
    except Exception as ex:
        print(ex)
        return False

def get_mongos(db_name, collection_name, st_data):
    try:
        connection_string = "mongodb://<username>:<password>@127.0.0.1/" + db_name
        client = MongoClient(connection_string)
        db = client.get_database(db_name)
        collection = db.get_collection(collection_name)

        temp = {}

        start = time.time()
        result = collection.find({}).limit(100000)
        end = time.time()
        temp["100000"] = end - start

        start = time.time()
        result = collection.find({}).limit(200000)
        end = time.time()
        temp["200000"] = end - start

        start = time.time()
        result = collection.find({}).limit(500000)
        end = time.time()
        temp["500000"] = end - start

        start = time.time()
        result = collection.find({}).limit(1000000)
        end = time.time()
        temp["1000000"] = end - start

        st_data["Mongos"] = temp
    except Exception as ex:
        print(ex)
        return False

def get_redis(st_data):
    try:
        r_host = "127.0.0.1"
        r_port = 6379
        rd = redis.StrictRedis(host = r_host, port = r_port, decode_responses = True)

        temp = {}

        start = time.time()
        result = rd.get(0)
        end = time.time()
        temp["1"] = end - start
        
        start = time.time()
        for i in range(100000):
            result = rd.get(i)
        end = time.time()
        temp["100000"] = end - start

        start = time.time()
        for i in range(200000):
            result = rd.get(i)
        end = time.time()
        temp["200000"] = end - start

        start = time.time()
        for i in range(500000):
            result = rd.get(i)
        end = time.time()
        temp["500000"] = end - start

        start = time.time()
        for i in range(1000000):
            result = rd.get(i)
        end = time.time()
        temp["1000000"] = end - start

        st_data["Redis"] = temp

    except Exception as ex:
        print(ex)
        return False

def get_blockchain_database(account_name, table_name, st_data):
        try:
            temp = {}

            start = time.time()
            i = 0
            result = subprocess.Popen(["cline", "get", "table", account_name, account_name, table_name, "--limit", "1"], stdout=subprocess.PIPE).communicate()[0]
            #result = json.loads(result)
            end = time.time()
            temp["1"] = end - start
            
            start = time.time()
            i = 0
            while i < 100000:
                result = subprocess.Popen(["cline", "get", "table", account_name, account_name, table_name, "--limit", "10000", "--lower", str(i)], stdout=subprocess.PIPE).communicate()[0]
                result = json.loads(result)
                i += len(result["rows"])
                #print(len(result["rows"]))
                #print(result["rows"][253])
            end = time.time()
            temp["100000"] = end - start

            start = time.time()
            i = 0
            while i < 200000:
                result = subprocess.Popen(["cline", "get", "table", account_name, account_name, table_name, "--limit", "10000", "--lower", str(i)], stdout=subprocess.PIPE).communicate()[0]
                result = json.loads(result)
                i += len(result["rows"])
                #print(len(result["rows"]))
                #print(result["rows"][253])
            end = time.time()
            temp["200000"] = end - start

            start = time.time()
            i = 0
            while i < 500000:
                result = subprocess.Popen(["cline", "get", "table", account_name, account_name, table_name, "--limit", "10000", "--lower", str(i)], stdout=subprocess.PIPE).communicate()[0]
                result = json.loads(result)
                i += len(result["rows"])
                #print(len(result["rows"]))
                #print(result["rows"][253])
            end = time.time()
            temp["500000"] = end - start

            start = time.time()
            i = 0
            while i < 1000000:
                result = subprocess.Popen(["cline", "get", "table", account_name, account_name, table_name, "--limit", "10000", "--lower", str(i)], stdout=subprocess.PIPE).communicate()[0]
                result = json.loads(result)
                i += len(result["rows"])
                #print(len(result["rows"]))
                #print(result["rows"][253])
            end = time.time()
            temp["1000000"] = end - start

            st_data["Inery"] = temp
        except Exception as ex:
            print(ex)
            pass

if __name__ == "__main__":
    with open("statistics.json", "w+") as file:
        data = {}
        if sys.argv[1] == "mysql":
            get_mysql(data)
        elif sys.argv[1] == "psql":
            get_postgres(data)
        elif sys.argv[1] == "mongos":
            get_mongos("usersdb", "users", data)
        elif sys.argv[1] == "redis":
            get_redis(data)
        elif sys.argv[1] == "inery":
            get_blockchain_database("dbtest", "users", data)
        elif sys.argv[1] == "all":
            get_mysql(data)
            get_postgres(data)
            get_mongos("usersdb", "users", data)
            get_redis(data)
            get_blockchain_database("dbtest", "users", data)
        else:
            print(f"Wrong argument code {sys.argv[1]}.")
        json.dump(data, file, indent = 6)
