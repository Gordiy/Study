import json


def write_json_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_json_file(path):
    file = open(path, 'r')
    data = json.loads(file.read())
    return data
