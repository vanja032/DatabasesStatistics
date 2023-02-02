# Databases Statistics
### Measuring real statisctics from different database management systems

#### Create SQL database query
- MySql database table:

```CREATE TABLE users(userid INT NOT NULL AUTO_INCREMENT, fname VARCHAR(255), lname VARCHAR(255), email VARCHAR(255), gender VARCHAR(30), PRIMARY KEY(userid));```
- Postgres database table:

```CREATE TABLE users(userid SERIAL, fname VARCHAR(255), lname VARCHAR(255), email VARCHAR(255), gender VARCHAR(30), PRIMARY KEY(userid));```
#### Install required python3 libraries
- MySql connector: **pip3 install mysql-connector-python**
- PostgreSql connector: pip3 install psycopg2-binary
