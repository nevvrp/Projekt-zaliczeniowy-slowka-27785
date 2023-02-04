import json
from datetime import datetime
from User import User


class WordService:
    pass

    def run_test(self, user: User):
        passed_successfully = True
        temp_last_exam = user.last_exam
        if user.passed_successfully == True:
            if isinstance(temp_last_exam, str):
                temp_last_exam = datetime.strptime(temp_last_exam, "%Y-%m-%d").date()
            since_last_exam = datetime.today().date() - temp_last_exam
            days_to_next_exam = 7 - since_last_exam.days
            if days_to_next_exam > 0:
                print(
                    "Gratulacje, mozesz dzisiaj odpoczywac - nastepna powtorka za: ",
                    7 - since_last_exam.days,
                    " dni.",
                )
                return passed_successfully

        file = open(user.path)
        words = json.load(file)
        print("------------------------------")
        print("TEST ZE SLOWEK")
        print("------------------------------")
        for word in words:
            # if word['mastered'] == False:
            print("podaj tlumaczenie dla: ", word["pl"])
            user_input = input()
            print("------------------------------")
            if user_input == word["en"]:
                word["mastered"] = True
                print("Poprawna odpowiedz, gratulacje!")
            else:
                word["mastered"] = False
                passed_successfully = False
                print("Niestety, ale musisz jeszcze poćwiczyć")
            print("------------------------------")
        with open(user.path, "w") as json_file:
            json.dump(words, json_file, indent=4)
        file.close
        if passed_successfully == True:
            print("Gratulacje, test zaliczony :)")
        else:
            print("Niestety, test niezaliczony :(")
        return passed_successfully
