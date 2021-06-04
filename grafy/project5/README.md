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
  
## Opis Projektu
Projekt jest realizacją zestawu nr 5 z przedmiotu "Grafy i ich zastowania". 
W pliku `__main__.py` znajduje się przykładowe użycie zaimplementowanych funkcji. 

## Przykłady użycia
* Wygenerowanie losowej sieci przepływowej z liczbą pośrednich warstw równą N=2 oraz pojemność krawędzi należy do 
  przedziału (1, 10). Dodatkowo wizualizacja sieci.
  ```python
  from grafy.project5.flow_network import generate_flow_network
  from grafy.project5.visualize_flow_network import visualize_flow_network
  
  flow_network, layers = generate_flow_network(2, 1, 10)
  visualize_flow_network(flow_network, layers)
  ```
* Zastosowanie algorytmu Forda-Fulkersona do znalezienia maksymalnego
przepływu na sieci oraz wizualizacja maksymalnego przepływu. Dodatkowo wizualizacja sieci.
  ```python
  from grafy.project5.ford_fulkerson import ford_fulkerson
  max_flow_network = ford_fulkerson_algorithm(flow_network, 0, 5)
  visualize_flow_network(flow_network, layers, max_flow_network)
  ```