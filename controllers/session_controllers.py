import os
from .file_controllers import write_json_file, read_json_file

def find_session_db(session_id):
    path = f"{os.getcwd()}/user_session/sessions.json"
    data = read_json_file(path)
    session = None
    if data and 'sessions' in data:
        for i in range(len(data)): 
            if session_id in data['sessions'][i]:
                session = data[i]
    
    return session
    

def create_session_db(session):
    path = f"{os.getcwd()}/user_session/sessions.json"
    data = read_json_file(path)
    if data and ['sessions'] in data:
        sessions = data['sessions'].append(session.session_obj())
    else:
        sessions = {'sessions': [session.session_obj()]}
    write_json_file(path, sessions)


def remove_session_db(session_id):
    path = f"{os.getcwd()}/user_session/sessions.json"
    status = False
    sessions = read_json_file(path)
    if sessions and ['sessions'] in sessions:
        sessions = sessions['sessions']
        for i in range(sessions):
            if sessions[i][session_id]:
                del sessions[i]
                status = True
                break

        write_json_file(path)
