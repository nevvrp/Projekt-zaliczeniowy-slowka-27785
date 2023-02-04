import json


class User:
    def __init__(
        self, username="", password="", path="", last_exam="", passed_successfully=False
    ):
        self.username = username
        self.password = password
        self.path = path
        self.last_exam = last_exam
        self.passed_successfully = passed_successfully


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        return [obj.username, obj.password]
