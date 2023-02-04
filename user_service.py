from datetime import datetime
import json
from typing import List
from User import User


class UserService:
    pass

    def delete_user(self, logged_user: User):
        file = open("users.json")
        data: List[User] = json.load(file)
        for idx, x in enumerate(data):
            if x["username"] == logged_user.username:
                del data[idx]
                with open("users.json", "w") as json_file:
                    json.dump(data, json_file, indent=4, default=str)

    def save_last_test_log(self, logged_user: User):
        file = open("users.json")
        data: List[User] = json.load(file)
        for user in data:
            if user["username"] == logged_user.username:
                user["last_exam"] = datetime.today().date()
                logged_user.last_exam = user["last_exam"]
                user["passed_successfully"] = logged_user.passed_successfully
                with open("users.json", "w") as json_file:
                    json.dump(data, json_file, indent=4, default=str)
        file.close
        return logged_user

    def save_path_to_file(self, logged_user: User):
        print("------------------------------")
        print("Podaj ściezke do pliku ze slowkami")
        print("------------------------------")
        path = input()
        file = open("users.json")
        data: List[User] = json.load(file)
        for user in data:
            if user["username"] == logged_user.username:
                user["path"] = path
                with open("users.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
        file.close
        return path

    def check_credentials(self, username, password):
        file = open("users.json")
        data: List[User] = json.load(file)
        for user in data:
            if username == user["username"] and password == user["password"]:
                return User(**user)
        print("Niepoprawne dane, spróbuj ponownie.")
        file.close
        return self.log_in()

    def check_if_user_already_exist(self):
        username = input()
        file = open("users.json")
        data: List[User] = json.load(file)
        for user in data:
            if username == user["username"]:
                print("Uzytkownik juz istnieje, podaj inną nazwę")
                file.close
                return self.check_if_user_already_exist()
        file.close
        return username

    def write_user_to_file(self, user: User):
        file = open("users.json")
        data: List[User] = json.load(file)

        data.append(user.__dict__)

        with open("users.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        file.close

    def create_user(self):
        print("Podaj nazwę uzytkownika")
        username = self.check_if_user_already_exist()
        print("Podaj haslo")
        password = input()
        user = User(username, password)
        self.write_user_to_file(user)

    def log_in(self):
        print("------------------------------")
        print("LOGOWANIE")
        print("------------------------------")
        print("Podaj nazwę uzytkownika")
        username = input()
        print("Podaj haslo")
        password = input()
        return self.check_credentials(username, password)
