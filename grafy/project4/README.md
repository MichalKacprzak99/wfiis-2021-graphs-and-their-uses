# Projekt nr. 4

## Autorzy - Letnie Dranie

- Michał Kacprzak
- Michał Ambroży
- Kacper Łuka
- Bartek Mikołajczyk

## Wymagania

- Python wersja 3.6
- pobranie dodatkowych bibliotek potrzebnych do realizacji programu możliwe za pomocą komend:
    ```commandline
    cd grafy/project4/
    grafy/project4/ pip3 install -r requirements.txt
    ```
- w przypadku problemów z zainstolawaniem vpythona należy zrobić upgrade pip3 za pomocą poniższej komendy, a następnie
  ponowić próbe instalacji:
    ```commandline
    grafy/project4/ pip3 install --upgrade pip
    grafy/project4/ pip3 install -r requirements.txt
    ```

## Opis Projektu

Projekt jest realizacją zestawu nr 4 z przedmiotu "Grafy i ich zastowania". W pliku `__main__.py` znajduje się
przykładowe użycie zaimplementowanych funkcji.

## Przykłady użycia

* Generowanie digrafu na podstawie ilości wierzchołków i prawdopodobieństwa:
  ```python
  from grafy.project4 import digraph_generation

  vertice_number = 7
  probability = 0.5
  
  adj_matrix = digraph_generation.generate_N_P_digraph(vertice_number, probability)
  ```
* Wykorzystanie algorytmu Kosaraju - do znajdowania składowych w grafie:
  ```python
  from grafy.project4 import kosaraju
  
  graph_connected_components = kosaraju.kosaraju(adj_matrix)
  ```

* Sprawdzenie czy w grafie znajduje się ujemny cykl:
  ```python
  from grafy.project4 import bellman_ford
  from grafy.project4 import digraph_generation

  
  adj_matrix = digraph_generation.generate_N_P_digraph(7, 0.5)
  weighted_adj_matrix = bellman_ford.assign_weights_to_adj_matrix(adj_matrix)
  cycle_info = bellman_ford.bellman_ford(adj_matrix, weighted_adj_matrix, 0)
  ```

* Utworzenie macierzy odległości na podstawie grafu:
  ```python
  from grafy.project4 import bellman_ford
  from grafy.project4 import digraph_generation
  from grafy.project4 import johnson

  adj_matrix = digraph_generation.generate_N_P_digraph(7, 0.5)
  weighted_adj_matrix = bellman_ford.assign_weights_to_adj_matrix(adj_matrix)
  D = johnson.johnson(adj_matrix, weighted_adj_matrix)
  ```

    
    