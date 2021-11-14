import os

from .file_controllers import read_json_file, write_json_file


def find_session_db(session_id):
    path = f"{os.getcwd()}/temp/sessions.json"
    data = read_json_file(path)
    session = None
    if data and "sessions" in data:
        for i in range(len(data["sessions"])):
            if session_id in data["sessions"][i]:
                session = data["sessions"][i]
                break

    return session


def create_session_db(session):
    path = f"{os.getcwd()}/temp/sessions.json"
    data = read_json_file(path)
    if data and "sessions" in data:
        data["sessions"].append(session.session_obj())
    else:
        data = {"sessions": [session.session_obj()]}
    write_json_file(path, data)


def remove_session_db(session_id):
    path = f"{os.getcwd()}/temp/sessions.json"
    status = False
    sessions = read_json_file(path)
    if sessions and "sessions" in sessions:
        sessions = sessions["sessions"]
        for i in range(len(sessions)):
            if session_id in sessions[i]:
                del sessions[i]
                status = True
                break

        write_json_file(path, sessions)
