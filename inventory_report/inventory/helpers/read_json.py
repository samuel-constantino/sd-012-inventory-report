import json


def read_json(path):
    with open(path) as file:
        content = json.load(file)

    return content
