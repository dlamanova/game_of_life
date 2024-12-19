import json

def save_to_file(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file)

def load_from_file(file_name):
    with open(file_name, "r") as file:
        return json.load(file)
