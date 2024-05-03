import hashlib

from modules.db import Database


class UserManager:
    def __init__(self):
        self.db = Database()

    def login(self, username, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        users = self.db.select(
            'select * from users where username = ?, password = ?',
            (username, password)
        )
        if len(users) == 0:
            return False
        return users[0]

    def register(self, username, password, role):
        password = hashlib.sha256(password.encode()).hexdigest()
        return self.db.insert(
            'insert into users (username, password, role) values (?, ?, ?)',
            (username, password, role)
        )
