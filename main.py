import sys
from User import User

from user_service import UserService
from word_service import WordService

user_service = UserService()
word_service = WordService()


def panel(user: User):
    print("------------------------------")
    print("Panel uzytkownika")
    print("------------------------------")
    print("Wybierz opcję wpisując jej numer:")
    print("1. Uruchom test ponownie")
    print("2. Usuń konto")
    print("3. Zakończ program")

    selected_option = input()

    try:
        string_int = int(selected_option)
    except ValueError:
        print("Wprowadź liczbę całkowitą")
        return get_options()

    if string_int == 1:
        run_test(user)

    elif string_int == 2:
        user_service.delete_user(user)

    elif string_int == 3:
        sys.exit()


def run_test(user: User):
    user.passed_successfully = word_service.run_test(user)
    user = user_service.save_last_test_log(user)
    panel(user)


def log_in():
    user: User = user_service.log_in()
    if user.path == "":
        user.path = user_service.save_path_to_file(user)

    run_test(user)


def get_options():
    print("------------------------------")
    print("WITAJ W PROGRAMIE DO NAUKI SLOWEK! | autor Zuzanna Paluszczak")
    print("------------------------------")
    print("------------------------------")
    print("Wybierz opcję wpisując jej numer:")
    print("------------------------------")
    print("1. Utwórz konto")
    print("2. Zaloguj się")
    print("3. Zakończ program")

    selected_option = input()

    try:
        string_int = int(selected_option)
    except ValueError:
        print("Wprowadź liczbę całkowitą")
        return get_options()

    return string_int


selected_option = get_options()


if selected_option == 1:
    print("------------------------------")
    print("Tworzenie konta")
    print("------------------------------")

    user_service.create_user()
    log_in()

elif selected_option == 2:
    log_in()

elif selected_option == 3:
    sys.exit()
