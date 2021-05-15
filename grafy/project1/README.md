# Projekt nr. 1

## Autorzy - Letnie Dranie
- Michał Kacprzak
- Michał Ambroży
- Kacper Łuka
- Bartek Mikołajczyk

## Wymagania
- Python wersja 3.6
- pobranie dodatkowych bibliotek potrzebnych do realizacji programu możliwe
  za pomocą komend:
    ```commandline
    cd grafy/project1/
    grafy/project1/ pip3 install -r requirements.txt
    ```
- w przypadku problemów z zainstolawaniem vpythona należy zrobić upgrade pip3 za pomocą poniższej komendy,
  a następnie ponowić próbe instalacji:
    ```commandline
    grafy/project1/ pip3 install --upgrade pip
    grafy/project1/ pip3 install -r requirements.txt
    ```
## Opis Projektu
Projekt jest realizacją zestawu nr 1 z przedmiotu "Grafy i ich zastowania". 
W pliku `grafy/project1/__main__.py` znajduje się przykładowe użycie zaimplementowanych funkcji. 
Wyjściem programu jest przedstawienie 3 reprezentacji(macierz sąsiedztwa,lista sąsiedztwa,macierz incydencji) 
wylosowanego grafu G(n, l),dla n = 10 oraz  l = 5 oraz jego wizualizacja.

## Przykłady użycia

  * Wygenerowanie losowego grafu o x wierchołkach i y krawędziach
    ```python
    from graph_generation import generate_N_L_graph
    
    adj_matrix = generate_N_L_graph(x, y)
    ```
  * Wygenerowanie losowego grafu o x wierchołkach i prawdopodobieństwie
    krawędzi pomiędzy parą wierzchołków równym y%
    ```python
    from graph_generation import generate_N_P_graph
    
    adj_matrix = generate_N_P_graph(x, y//100)
    ```
  * Przykładowa konwersja z macierzy sąsiedzctwa do listy sąsiedzctwa
    ```python
    from graph_conversion import adj_matrix_to_list
    
    adj_matrix = generate_N_L_graph(x, y)
    adj_list = adj_matrix_to_list(adj_matrix)
    ```
  * Wizualizacja losowego grafu o x wierzchołkach i y krawędziach
    ```python
    from graph_visualization import visualize_graph
    from graph_generation import generate_N_L_graph
    
    adj_matrix = generate_N_L_graph(x, y)
    visualize_graph(adj_matrix)
    ```
## Poprawność rozwiązania
W celu weryfikacji poprawności rozwiązania został użyty przykład udostępniony w materiałach na Upelu. 
W folderze `grafy/test/project1/` znajdują się testy, które weryfikują sposób generowania grafów 
oraz poprawność konwersji pomiędzy poszczególnymi reprezentacjami.
W celu uruchomienia testów, należy użyć następujących komend:
  ```commandline
  cd grafy/
  grafy/ python -m unittest discover test.project1
  ```
    
    
    
