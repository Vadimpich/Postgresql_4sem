import hashlib

from modules.db import Database


class UserManager:
    def __init__(self):
        self.db = Database()

    def login(self, username, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        users = self.db.select(
            f"select * from users "
            f"where username = '{username}' and password = '{password}';",
        )
        if len(users) == 0:
            return False
        return users[0]

    def register(self, username, password, role):
        password = hashlib.sha256(password.encode()).hexdigest()
        return self.db.insert(
            f'insert into users (username, password, role) '
            f"values ('{username}', '{password}', '{role}');",
        )

    def change_password(self, username, new_password):
        password = hashlib.sha256(new_password.encode()).hexdigest()
        return self.db.insert(
            f"update users set password = '{password}' "
            f"where username = '{username}';"
        )
