import os
from .file_controllers import write_json_file, read_json_file


def find_user_db(user_id):
    path = f"{os.getcwd()}/temp/users.json"
    data = read_json_file(path)
    user = None
    if data and 'users' in data:
        for i in range(len(data)):
            if user_id in data['users'][i]:
                user = data['users'][i]

    return user

def create_user_db(user):
    path = f"{os.getcwd()}/temp/users.json"
    data = read_json_file(path)
    if data and 'users' in data:
        data['users'].append(user.get_user())
    else: 
        data = {'users': [user.get_user()]}

    write_json_file(path, data)

def remove_user_db(user_id):
    pass
