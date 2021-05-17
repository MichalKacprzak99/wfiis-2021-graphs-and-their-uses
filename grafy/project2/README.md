# Projekt nr. 2

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
    cd grafy/project2/
    grafy/project2/ pip3 install -r requirements.txt
    ```
- w przypadku problemów z zainstolawaniem vpythona należy zrobić upgrade pip3 za pomocą poniższej komendy,
  a następnie ponowić próbe instalacji:
    ```commandline
    grafy/project2/ pip3 install --upgrade pip
    grafy/project2/ pip3 install -r requirements.txt
    ```
## Opis Projektu
Projekt jest realizacją zestawu nr 2 z przedmiotu "Grafy i ich zastowania". 
W pliku `grafy/project2/__main__.py` znajduje się przykładowe użycie zaimplementowanych funkcji. 


## Przykłady użycia
  * Wygenerowanie grafu zawierającego cykl Eulera i 5 wierzchołków oraz wypisanie tegoż cyklu:
    ```python    
    from grafy.project2.check_if_euler import get_euler_graph, print_euler_cycle
        
    print_euler_cycle(get_euler_graph(5))
    ```

  * Sprawdzenie, czy dany graf (w postaci listy sąsiedztwa) zawiera cykl Hamiltona:
    ```python
    from grafy.project2.check_if_hamiltonian import check_graph, is_hamiltonian
        
    sample_adj_list = {
            0: [1, 3, 4],
            1: [0, 2, 4, 5],
            2: [1, 3, 6],
            3: [0, 2, 5, 6],
            4: [0, 1, 7],
            5: [1, 3, 7],
            6: [2, 3, 7],
            7: [4, 5, 6]
    }
    
    check_graph(sample_adj_list)
    ```
    
  * Sprawdzenie, czy dany ciąg jest ciągiem graficznym:
    ```python
    from grafy.project2.degree_sequence import degree_sequence_checker
    
    example_correct = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    
    degree_sequence_checker(example_correct)
    ```
    
  * Znalezienie największej spójnej składowej na grafie:
    ```python
    from grafy.project1.graph_conversion import adj_matrix_to_list
    from grafy.project2.graph_components import find_biggest_graph_component
    
    graph_N_L = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 ]

    adj_list = adj_matrix_to_list(graph_N_L)

    find_biggest_graph_component(adj_list)
    ```
    
  * Generowanie losowych grafów k-regularnych:
    ```python
    from grafy.project2.graph_randomization import generate_regular_graph
    
    generate_regular_graph(7, 2)
    ```
    
  * Konstruowanie grafu prostego o stopniach wierzchołków zadanych przez ciąg graficzny:
    ```python
    from grafy.project2.degree_sequence import degree_sequence_checker
    from grafy.project2.graph_randomization import create_graph_from_degree_sequence
    
    degree_sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    print(degree_sequence_checker(degree_sequence))
    graph = create_graph_from_degree_sequence(degree_sequence)
    ```
    
  * Randomizacja grafów prostych o zadanych stopniach wierzchołków:
    ```python
    from grafy.project2.degree_sequence import degree_sequence_checker
    from grafy.project2.graph_randomization import create_graph_from_degree_sequence, randomize_graph
    
    degree_sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    print(degree_sequence_checker(degree_sequence))
    graph = create_graph_from_degree_sequence(degree_sequence)
    random_graph = randomize_graph(degree_sequence, 2)
    ```

    
    