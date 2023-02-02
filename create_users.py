import json
import random

users_num = 1000000

with open("users_temp.json", "r") as file:
    temp_users = json.loads(file.read())
    all_users = []

    for i in range(users_num):
        random_1 = random.randint(0, 999)
        random_2 = random.randint(0, 999)
        new_name = str(temp_users[random_1]["first_name"]).replace("'", "")
        new_lname = str(temp_users[random_2]["last_name"]).replace("'", "")
        new_email = new_name.lower() + new_lname.lower() + str(random.randint(1, 1000)) + "@email.com"
        new_gender = str(temp_users[random_1]["gender"]).replace("'", "")
        all_users.append({"fname" : new_name, "lname" : new_lname, "email" : new_email, "gender" : new_gender})

with open("users.json", "w") as file:
    json.dump(all_users, file, indent = 6)

