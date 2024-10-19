# src/data/UserCredentialsConfig.py
import json
import os

class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User(username={self.username}, role={self.role})"

class UserCredentialsConfig:
    def __init__(self):
        self.credentials = self.load_credentials()

    def load_credentials(self):
        """Loads user credentials from a JSON file."""
        filepath = 'src/data/users.json'
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Credentials file not found: {filepath}")

        with open(filepath) as json_file:
            return json.load(json_file)

    def get_valid_user(self):
        """Returns the valid user credential."""
        valid_users = self.credentials.get("valid_users", [])
        if valid_users:
            user_data = valid_users[0]
            return User(username=user_data['username'], password=user_data['password'])
        return None

    def get_invalid_user(self, index=0):
        """Returns the invalid user credential by index."""
        invalid_users = self.credentials.get("invalid_users", [])
        if index < len(invalid_users):
            user_data = invalid_users[index]
            return User(username=user_data['username'], password=user_data['password'])
        return None

    def get_invalid_users(self):
        """Returns a list of invalid user credentials."""
        return [
            User(username=user['username'], password=user['password']) 
            for user in self.credentials.get("invalid_users", [])
        ]