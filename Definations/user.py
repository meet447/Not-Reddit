import json

def load_user_credentials():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users

def save_user_credentials(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)