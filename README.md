# GoIt_homework_11
Zadanie 11

Zadania
W tym zadaniu domowym będziemy

Dodawać pole Birthday. To pole jest opcjonalne, ale może być tylko jedno.
Dodamy też funkcjonalność do pracy z Birthday w klasie Record, a mianowicie funkcję days_to_birthday, która zwraca liczbę dni do następnych urodzin.
Dodamy funkcjonalności sprawdzania poprawności wartości dla pól Phone, Birthday.
Dodamy paginacji (wyjście strona po stronie) dla AddressBook dla sytuacji, gdy książka jest bardzo duża i trzeba pokazać zawartość w częściach, a nie wszystkie naraz. Implementujemy to poprzez utworzenie iteratora nad rekordami.
Kryteria akceptacji:
- Klasa AddressBook implementuje metodę iterator, która zwraca generator przez rekordy AddressBook i zwraca widok dla N rekordów w jednej iteracji.
- Klasa Record przyjmuje jeszcze jeden dodatkowy (opcjonalny) argument klasy Birthday
- Klasa Record implementuje metodę days_to_birthday, która zwraca liczbę dni do następnych urodzin kontaktu, jeśli podano datę urodzin.
- Logika setter i getter dla atrybutów value dziedziczących po Field.
- Sprawdzenie poprawności podrzędnego setter numeru telefonu dla value klasy Phone.
- Sprawdzenie poprawności podrzędnego settera daty urodzin dla wartości klasy Birthday.


---------------------------------------------------------------
Zadanie 10 (praca domowa do poprzedniego tematu)

W tym zadaniu domowym będziemy nadal rozwijać naszego wirtualnego asystenta z interfejsem CLI.

Nasz asystent jest już w stanie wchodzić w interakcję z użytkownikiem za pośrednictwem wiersza poleceń, odbierając polecenia i argumenty oraz wykonując wymagane działania. W tym zadaniu będziesz musiał popracować nad wewnętrzną logiką asystenta, nad tym, jak przechowywane są dane, jakiego rodzaju dane i co można z nimi zrobić.

W tym celu wykorzystamy programowanie obiektowe. Najpierw wybierzmy kilka encji (modeli), z którymi będziemy pracować.

Użytkownik będzie posiadał książkę adresową lub książkę kontaktów. Ta książka kontaktów zawiera wpisy. Każdy wpis zawiera zestaw pól.

W ten sposób opisaliśmy encje (klasy), które muszą zostać zaimplementowane. Następnie rozważmy wymagania dla tych klas i ustalmy ich relacje, zasady, według których będą współdziałać.

Użytkownik wchodzi w interakcję z książką kontaktów poprzez dodawanie, usuwanie i edytowanie wpisów. Użytkownik powinien mieć również możliwość przeszukiwania katalogu w poszukiwaniu wpisów według jednego lub więcej kryteriów (pól).

Pola mogą być wymagane (imię i nazwisko) lub opcjonalne (numer telefonu lub adres e-mail). Ponadto rekordy mogą zawierać wiele pól tego samego typu (na przykład wiele numerów telefonów). Użytkownik powinien mieć możliwość dodawania/usuwania/edycji pól w każdym rekordzie.

W tym zadaniu domowym powinieneś zaimplementować następujące klasy:

    Klasę AddressBook, która dziedziczy po UserDict, a następnie dodamy do niej logikę wyszukiwania rekordów.
    Klasa Record, która jest odpowiedzialna za logikę dodawania/usuwania/edycji opcjonalnych pól i przechowywanie wymaganego pola Name.
    Klasa Field, która będzie rodzicem dla wszystkich pól, w której następnie zaimplementujemy logikę wspólną dla wszystkich pól.
    Klasa Name, wymagane pole z nazwą.
    Klasa Phone, opcjonalne pole z numerem telefonu, a jeden rekord (Record) może zawierać ich kilka.

Kryteria przyjęcia

    Wszystkie klasy z zadania zostały zaimplementowane.
    Rekordy Record w AddressBook są przechowywane jako wartości w słowniku. Wartość Record.name.value jest używana jako klucze.
    Rekord Record przechowuje obiekt Name w osobnym atrybucie.
    Rekord Record przechowuje listę obiektów Phone w osobnym atrybucie.
    Record implementuje metody do dodawania/usuwania/edycji obiektów Phone.
    AddressBook implementuje metodę add_record, która dodaje Record do self.data.
 
