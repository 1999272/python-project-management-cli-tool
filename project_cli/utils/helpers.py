import json, os

def load_data(filepath):
    if not os.path.exists(filepath):
        return {"users": []}
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"users": []}

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)