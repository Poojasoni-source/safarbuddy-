import json
import os
from models.users import User

FILE_NAME = "data.json"


def load_users():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    users_data = data.get("users", [])
    return [User.from_dict(u) for u in users_data]


def save_users(users):
    data = {
        "users": [u.to_dict() for u in users]
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)