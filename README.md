
# Opis programu
* Program do nauki słówek, autor Zuzanna Paluszczak. Kod programu został sprawdzony pod kątem reguł gramatycznych PEP8.

# Funkcjonalności
* Tworzenie konta (dane o koncie zapisywane są w pliku users.json w formacie JSON)
* Logowanie
* Usuwanie konta
* Algorytm weryfikujący znajomość słówek oraz wyliczający czas do następnej sesji nauki.

# Opis algorytmu nauki słówek
* Program przy pierwszym logowaniu prosi o podanie ścieżki do pliku ze słówkami. Słówka przyjmowane są w formacie JSON, w postaci listy obiektów. Pojedynczy obiekt ze słówkiem przyjmuje takie pola jak: pl: string, en: string; mastered: boolean, gdzie:

    pl - polskie tłumaczenie,
    en - angielskie tłumaczenie,
    mastered - flaga z informacją, czy słówko w poprzedniej sesji zostało opanowane.

Przykładowy plik ze słówkami załączony został do programu, znajduje się w pliku słówka.json (jeśli chcemy wskazać ten plik, wpisujemy: słówka.json)

* Po wczytaniu listy słówek uruchamiany jest test. Użytkownik odpytywany jest ze wszystkich słówek, jeśli na któreś odpowie poprawnie, flaga mastered przy słówku ustawiana jest jako 'True' (w przeciwnym wypadku jako 'False').

Po zakończonym teście zapisywane są informacje o teście nauki. Test uznawany jest jako zaliczony, jeśli użytkownik na wszystkie słówka odpowie prawidłowo. Informacje o sesji trafiają do pliku users.json, pod rekord odpowiadający zalogowanemu użytkownikowi. Poza informacją o zaliczeniu (lub niezaliczeniu testu) zapisywana jest również data sesji.

Przy ponownej próbie uruchomienia testu, sprawdzana jest data poprzedniej sesji oraz informacja o zaliczeniu testu.

- Jeśli użytkownik nie zaliczył poprzedniej sesji nauki, sesja poprawkowa uruchamia się od razu niezależnie od daty poprzedniej sesji.

- Jeśli użytkownik zaliczył poprzednia sesje nauki i minęło od niej mniej niż 7 dni, wyliczany jest czas do następnej sesji powtórkowej (7 dni - liczba dni od poprzedniej sesji), oraz komunikat z informacja, że użytkownik może jeszcze odpoczywać

- Jeśli użytkownik zaliczył poprzednia sesje nauki i minęło od niej przynajmniej 7 dni uruchamiana jest sesja powtórkowa.

# Menu główne
* niezalogowany użytkownik ma w panelu trzy opcje:
- Utworzenie konta (odpytuje użytkownik o nazwę oraz hasło, następnie dodaje wpis do pliku users.json)
- Logowanie (odpytuje użytkownika o nazwę oraz hasło, następnie przeszukuje plik users.json pod kątem pasującej pary nazwa/hasło-jeśli odnajduje wpis, loguje użytkownika)
- Zamknięcie programu

# Panel użytkownika
* Zalogowany użytkownik ma w panelu trzy opcje:
- Uruchomienie testu (w zależności od wyniku poprzedniej sesji, test albo się uruchomi albo zostanie wyświetlony komunikat z gratulacjami oraz informacją za ile dni powinien powtórzyć sesje nauki)
- Wylogowanie się (zakończenie programu)
- Usunięcie konta (usuwa wpis z informacjami o użytkowniku w pliku users.json)

# Klasa User, UserEncoder
* zawiera konstruktor tworzący obiekt o polach:

- username: string - nazwa użytkownika, domyślnie pusty string
- password: string - haslo użytkownika, domyślnie pusty string
- path: string - sciezka do pliku ze słówkami, domyślnie pusty string
- last_exam: string - data ostatniej sesji nauki, domyślnie pusty string
- passed_successfully: boolean - wynik ostatniej sesji nauki, domyślnie False
* User encoder posiada metode do encodowania wpisu wczytanego z pliku zawierającego informacje o użytkowniku w formacie JSON. Encoder został przedstawiony czysto demonstracyjnie, aby pokazać możliwość odwoływanie się do pól klasy za pomocą operatora "." np. user.username, zamiast odwoływać się do pól dictionary, np. user['username']

# Klasa UserService
* Zawiera szereg metod manipulujących plikiem users.json:
- create_user - metoda tworząca użytkownika (obiekt)
- check_if_user_already_exist - metoda sprawdzająca, czy nazwa użytkownika podana przy tworzeniu konta jest unikalna
- write_user_to_file - metoda zapisująca użytkownika w pliku users.json
- check_credentials - metoda weryfikująca czy podane przez użytkownika username oraz password pasują do bazy użytkowników
- save_path_to_file - metoda zapisująca ścieżkę do pliku ze słówkami do rekordu zalogowanego użytkownika
- save_last_test_log - metoda zapisująca log z ostatniej sesji nauki (wynik testu, date przeprowadzania testu)
- delete_user - metoda usuwająca zalogowanego użytkownika

# Klasa WordService
* Klasa wspomagająca manipulacje pliku ze słówkami, zawiera metodę z algorytmem przeprowadzania sesji nauki

# Klasa main
* Klasa opakowująca wszystkie funkcjonalności, zawiera panel użytkownika zalogowanego oraz niezalogowanego. Udostępnia wszystkie funkcjonalności programu

# Wymagania
* Python 3.6+

# Uruchomienie programu
* Program uruchamiamy metodą
```
python3 main.py
```