import json


def write_json_file(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()


def read_json_file(path):
    with open(path) as f:
        data = json.load(f)
        if data:
            return data
        else:
            return {}
