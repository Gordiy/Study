import os

from .file_controllers import read_json_file, write_json_file


def find_user_db(user_id):
    path = f"{os.getcwd()}/temp/users.json"
    data = read_json_file(path)
    user = None
    if data and "users" in data:
        for i in range(len(data)):
            if user_id in data["users"][i]:
                user = data["users"][i]

    return user


def find_user_by_username_db(username):
    path = f"{os.getcwd()}/temp/users.json"
    data = read_json_file(path)
    user = None
    if data and "users" in data:
        data = data["users"]
        for i in range(len(data)):
            found = False
            for k in data[i]:
                u_name = data[i][k]["username"]
                if u_name.lower() == username.lower():
                    user = data[i]
                    found = True
                    break
            if found:
                break
    return user


def create_user_db(user):
    path = f"{os.getcwd()}/temp/users.json"
    data = read_json_file(path)
    if data and "users" in data:
        data["users"].append(user.get_user())
    else:
        data = {"users": [user.get_user()]}

    write_json_file(path, data)


def remove_user_db(user_id):
    pass
