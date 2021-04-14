# Projekt nr. 1

## Autorzy - Letnie Dranie
- Michał Kacprzak
- Michał Ambroży
- Kacper Łuka
- Bartek Mikołajczyk

## Wymagania
- Python wersja <=3.6
- pobranie dodatkowych bibliotek potrzebnych do realizacji programu możliwe za pomocą komendy:
    ```
    python3 pip install -r requirements.txt
    ```
## Opis Projektu
Projekt jest realizacją zestawu nr 1 z przedmiotu "Grafy i ich zastowania". 
W pliku `__main__.py` znajduje się przykładowe użycie zaimplementowanych funkcji. 
Wyjściem programu jest przedstawienie 3 reprezentacji(macierz sąsiedztwa,lista sąsiedztwa,macierz incydencji) 
wylosowanego grafu G(n, l),dla n = 10 oraz  l = 5 oraz jego wizualizacja.
## Poprawność rozwiązania
W celu weryfikacji poprawności rozwiązania został użyty przykład udostępniony w materiałach na Upelu. 
W folderze `test/` znajdują się testy, które weryfikują sposób generowania grafów 
oraz poprawność konwersji pomiędzy poszczególnymi reprezentacjami.
W celu uruchomienia testów, będąc w głównym folderze, należy wpisać:

    ```
    python3 -m unittest
    ```
