# Opis programu cf
  * Program do nauki słówek, autor Zuzanna Paluszczak. Kod programu został
  sprawdzony pod kątem reguł gramatycznych PEP8.

# Funkcjonalności
  * Tworzenie konta (dane o koncie zapisywane są w pliku users.json w formacie
    JSON)
  * Logowanie
  * Usuwanie konta
  * Algorytm weryfikujący znajomość słówek oraz wyliczający czas do następnej
    sesji nauki.

# Opis algorytmu nauki słówek
  * Program przy pierwszym logowaniu prosi o podanie ściezki do pliku ze slowkami.
    Slowka przyjmowane sa w formacie JSON, w postaci listy obiektów. Pojedynczy obiekt ze slowkiem przyjmuje
    takie pola jak: pl: string, en: string; mastered: boolean, gdzie:

    pl - polskie tłumaczenie,
    en - angielskie tlumaczenie,
    mastered - flaga z informacją, czy słówko w poprzedniej sesji zostało opanowane.

    Przykładowy plik ze słówkami załączony został do programu, znajduje się w pliku slowka.json (jesli chcemy wskazac ten plik, wpisujemy: slowka.json)

  * Po wczytaniu listy słówek uruchamiany jest test. Uzytkownik odpytywany jest ze wszystkich slowek, jeśli na któreś
    odpowie poprawnie, flaga mastered przy slowku ustawiana jest jako 'True' (w przeciwnym wypadku jako 'False').

    Po zakonczonym tescie zapisywane są informacje o tescie nauki. Test uznawany jest jako zaliczony, jeśli uzytkownik na wszystkie slowka odpowie prawidlowo. Informacje o sesji trafiają do pliku users.json, pod rekord odpowiadajacy zalogowanemu uzytkownikowi. Poza informacją o zaliczeniu (lub niezaliczeniu testu) zapisywana jest równiez data sesji.

    Przy ponownej probie uruchomienia testu,sprawdzana jest data poprzedniej sesji oraz informacja o zaliczeniu testu.

    - Jeśli uzytkownik niezaliczyl poprzedniej sesji nauki, sesja poprawkowa uruchamia sie od razu - niezaleznie od daty poprzedniej sesji.

    - Jeśli uzytkownik zaliczyl poprzednia sesje nauki i minelo od niej mniej niz 7 dni, wyliczany jest czas do nastepnej sesji powtorkowej (7 dni - liczba dni od poprzedniej sesji), oraz komunikat z informacja, ze uzytkownik moze jeszcze odpoczywac

    - Jesli uzytkownik zaliczyl poprzednia sesje nauki i minelo od niej przynajmniej 7 dni uruchamiana jest sesja powtorkowa.

# Menu glowne
  * niezalogowany uzytkownik ma w panelu trzy opcje:
    - Utworzenie konta (odpytuje uzytkownika o nazwe oraz haslo, nastepnie dodaje wpis do pliku users.json)
    - Logowanie (odpytuje uzytkownika o nazwe oraz haslo, nastepnie przeszukuje plik users.json pod katem pasującej pary nazwa/haslo - jesli odnajduje wpis, loguje uzytkownika)
    - Zamkniecie programu

# Panel uzytkownika
  * Zalogowany uzytkownik ma w panelu trzy opcje:
    - Uruchomienie testu (w zaleznosci od wyniku poprzedniej sesji, test albo sie uruchomi albo zostanie wyswietlony komunikat z gratulacjami oraz informacją za ile dni powinien powtorzyc sesje nauki)
    - Wylogowanie sie (zakonczenie programu)
    - Usunięcie konta (usuwa wpis z informacjami o uzytkowniku w pliku users.json)

# Klasa User, UserEncoder
  * zawiera konstruktor tworzący obiekt o polach:
    - username: string - nazwa uzytkownika, domyslnie pusty string
    - password: string - haslo uzytkownika, domyslnie pusty string
    - path: string - sciezka do pliku ze slowkami, domyslnie pusty string
    - last_exam: string - data ostatniej sesji nauki, domyslnie pusty string
    - passed_successfully: boolean - wynik ostatniej sesji nauki, domyslnie False

  * User encoder posiada metode do encodowania wpisu wczytanego z pliku zawierajacego informacje o uzytkowniku w formacie JSON.
    Encoder zostal przedstawiony czysto demonstracyjnie, aby pokazac mozliwosc odwolywania sie do pól klasy za pomocą operatora "." np. user.username,
    zamiast odwoływac się do pól dictionary, np. user['username']

# Klasa UserService
  * Zawiera szereg metod manipulujących plikiem users.json:
   - create_user - metoda tworząca uzytkownika (obiekt)
   - check_if_user_already_exist - metoda sprawdzajaca, czy nazwa uzytkownika podana przy tworzeniu konta jest unikalna
   - write_user_to_file - metoda zapisujaca uzytkownika w pliku users.json
   - check_credentials - metoda weryfikujaca czy podane przez uzytkownika username oraz password pasuja do bazy uzytkownikow
   - save_path_to_file - metoda zapisujaca sciezke do pliku ze slowkami do rekordu zalogowanego uzytkownika
   - save_last_test_log - metoda zapisujaca log z ostatniej sesji nauki (wynik testu, date przeprowadzania testu)
   - delete_user - metoda usuwajaca zalogowanego uzytkownika

# Klasa WordService
  * Klasa wspomagajaca manipulacje pliku ze slowkami, zawiera metode z algorytmem przeprowadzania sesji nauki

 # Klasa main
  * Klasa opakowujaca wszystkie funkconalnosci, zawiera panel uzytkownika zalogowanego oraz niezalogowanego. Udostepnia wszystkie    funkcjonalnosci programu

# Wymagania

  * Python 3.6+


# Uruchomienie programu
Program uruchamiamy metoda
```
python3 main.py
```