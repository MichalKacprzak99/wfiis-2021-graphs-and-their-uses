# Projekt nr. 3

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
    cd grafy/project3/
    grafy/project3/ pip3 install -r requirements.txt
    ```
- w przypadku problemów z zainstolawaniem vpythona należy zrobić upgrade pip3 za pomocą poniższej komendy,
  a następnie ponowić próbe instalacji:
    ```commandline
    grafy/project3/ pip3 install --upgrade pip
    grafy/project3/ pip3 install -r requirements.txt
    ```
## Opis Projektu
Projekt jest realizacją zestawu nr 3 z przedmiotu "Grafy i ich zastowania". 
W pliku `__main__.py` znajduje się przykładowe użycie zaimplementowanych funkcji. 


## Przykłady użycia
  * Wygenerowanie losowego spójnego grafu o x wierchołkach i wagach krawędzi z zakresu (1,11)
    ```python
    from connected_graph_generation import generate_connected_graph
    
    adj_matrix = generate_connected_graph(x)
    ```
  * Użycie algorytmu Dijkstry na spójnym grafie o dodatnich krawędziach w celu znalezienie najkrótszych ścieżek 
    od wierzchołka nr x do reszty. Dodatkowo, wypisanie rezultatów działania algorytmu
    ```python
    from dijkstra_algorithm import print_dijkstra_algorithm_result, dijkstra_algorithm
    
    distance_matrix, previous_matrix = dijkstra_algorithm(adj_matrix, x)
    print_dijkstra_algorithm_result(distance_matrix, previous_matrix)
    ```
    
  * Wygenerowanie macierzy odległośći dla spójnego grafu 
    ```python
    from graph_center import generate_vertices_distance_matrix
    
    vertices_distance_matrix = generate_vertices_distance_matrix(adj_matrix)
    ```
    
  * Znalezienie centrum i centrum minimax spójnego grafu 
    ```python
    from graph_center import find_graph_center, find_graph_minimax_center
    
    graph_center = find_graph_center(adj_matrix)

    graph_minimax_center = find_graph_minimax_center(adj_matrix)
    ```
    
  * Znalezienie i wypisanie minimalnego drzewa rozpinającego dla grafu 
    ```python
    from kruskal_mst import kruskal_mst
    
    kruskal_mst(random_connected_graph)
    ```

    
## Poprawność rozwiązania
W celu weryfikacji poprawności rozwiązania został użyty przykład udostępniony w materiałach na Upelu. 
W folderze `grafy/test/project3/` znajdują się testy.
W celu uruchomienia testów, należy użyć następujących komend:
  ```commandline
  cd grafy/
  grafy/ python -m unittest discover test.project3
  ```
    
    