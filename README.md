# Databases Statistics
### Measuring real statisctics from different database management systems

- ### MySql database table:
  ##### Create table SQL database query
  ```CREATE TABLE users(userid INT NOT NULL AUTO_INCREMENT, fname VARCHAR(255), lname VARCHAR(255), email VARCHAR(255), gender VARCHAR(30), PRIMARY KEY(userid));```

- ### Postgres database table:
  ##### Create table SQL database query
  ```CREATE TABLE users(userid SERIAL, fname VARCHAR(255), lname VARCHAR(255), email VARCHAR(255), gender VARCHAR(30), PRIMARY KEY(userid));```

- ### Mongo database:
  ##### Create mongo user:
    ```use usersdb```
    ```
    db.createUser({
        user: "root",
        pwd: "root",
        roles: [
           { role: "readWrite", db: "usersdb" }
        ]
      }
    )
    ```
    
  ##### Create mongo collection:
    ```
    db.createCollection("users")
    ```

- ### Redis database:
    Use <key, value> format
    ```
    <index, {
        "fname": "<user first name>",
        "lname": "<user last name>",
        "email": "<user email>",
        "gender": "<user gender>"
    }>
    ```

- ### Blockchain database:
  ###### Blockchain database based on Inery Blockchain System, using **value contract** written in **C++**
  ##### Steps for setting a value contract on the blockchain:
    **1.** *Compile C++ value contract*
    ```inery-cpp -abigen dbtest.cpp -o dbtest.wasm```
    
    **2.** *Create a key for a blockchain account*
    ```cline create key --to-console```
    
    **3.** *Create the blockchain account*
    ```
    cline system newaccount <blockchain create account name> <account name> <public key> <public key> 
    --stake-net="1 INR" --stake-cpu="1 INR" --buy-mem-bytes="1048576"
    ```
    
    **3.** *Unlock the blockchain wallet*
    ```cline wallet unlock --password <wallet_password>```
    
    **4.** *Import the account private key to the blockchain wallet*
    ```cline wallet import --private-key <private key>```
    
    **5.** *Set value contract on the blockchain account*
    ```cline set contract dbtest ./ dbtest.wasm dbtest.abi```
    
    **6.** *Push **insert** action to the value contract on the blockchain*
    ```
    cline push action <account name> insert '["<user first name>", "<user last name>", "<user email>", "<user gender>"]' -p <account name>@active
    ```
    
    **7.** *Push **update** action to the value contract on the blockchain*
    ```
    cline push action <account name> update '[<user id>, "<user first name>", "<user last name>", "<user email>", "<user gender>"]' -p <account name>@active
    ```
    
    **8.** *Push **delete** action to the value contract on the blockchain*
    ```
    cline push action <account name> remove '[<user id>]' -p <account name>@active
    ```
    
    **9.** *Preview the blockchain table **users** on the blockchain account*
    ```cline get table <account name> <account name> users```
    
#### Install required python3 libraries
- MySql connector: **pip3 install mysql-connector-python**
- PostgreSql connector: **pip3 install psycopg2-binary**
- MongoDB connector: **pip3 install pymongo**
- Redis library: **pip3 install redis**
