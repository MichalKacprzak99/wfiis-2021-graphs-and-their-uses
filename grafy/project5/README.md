# Projekt nr. 5

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
    cd grafy/project5/
    grafy/project5/ pip3 install -r requirements.txt
    ```
- w przypadku problemów z zainstolawaniem vpythona należy zrobić upgrade pip3 za pomocą poniższej komendy,
  a następnie ponowić próbe instalacji:
    ```commandline
    grafy/project5/ pip3 install --upgrade pip
    grafy/project5/ pip3 install -r requirements.txt
    ```
  
## Opis Projektu
Projekt jest realizacją zestawu nr 5 z przedmiotu "Grafy i ich zastowania". 
W pliku `__main__.py` znajduje się przykładowe użycie zaimplementowanych funkcji. 

## Przykłady użycia
* Wygenerowanie losowej sieci przepływowej z liczbą pośrednich warstw równą N=2. Dodatkowo wizualizacja sieci.
  ```python
  from grafy.project5.flow_network import generate_flow_network
  from grafy.project1.graph_visualization import visualize_graph
  
  flow_network = generate_flow_network(N=2)
  visualize_graph(flow_network, weighted_graph=True, digraph=True)
  ```
* Zastosowanie algorytmu Forda-Fulkersona do znalezienia maksymalnego
przepływu na sieci
  ```python

  ```