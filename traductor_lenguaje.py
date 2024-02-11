import os
import numpy as np

class Character:
    def __init__(self, id, filename, generations):
        self.id = id
        self.filename = filename
        self.generations = generations
        self.matrix = []

def next_state(curr_state, num_generations):
    for ng in range(num_generations):
        height, width = curr_state.shape
        new_state = np.zeros((height, width), dtype=int)
        for y in range(height):
            for x in range(width):
                neighbors_sum = np.sum(curr_state[max(0, y-1):min(height, y+2), max(0, x-1):min(width, x+2)]) - curr_state[y, x]
                if curr_state[y, x] == 1 and not (2 <= neighbors_sum <= 3):
                    new_state[y, x] = 0
                elif neighbors_sum == 3:
                    new_state[y, x] = 1
                else:
                    new_state[y, x] = curr_state[y, x]
        print('Generation: ' + str(ng))
        print_state(curr_state)
        curr_state = new_state
    return curr_state

def print_state(state):
    width, height = state.shape
    for y in range(width):
        for x in range(height):
            print(state[y, x], end=' ')
        print()
    print()

def read_initial_states(character, script_directory):
    filepath = os.path.join(script_directory, character.filename)
    print(filepath)
    with open(filepath, 'r') as file:
        lines = file.readlines()
        state = []
        for line in lines:
            state.append([int(x) for x in line.strip()])
        character.matrix = np.array(state)

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    characters = [
        Character('p', 'letra_pez.txt', 3),
        Character('o', 'letra_o.txt', 18),
        Character('de', 'letra_delta.txt', 3),
        Character('d', 'letra_d.txt', 3),
        Character('b', 'letra_b.txt', 3),
        Character('a', 'letra_a.txt', 3),
        Character('i', 'letra_i.txt', 10),
        Character('e', 'letra_e.txt', 10),
        Character('n', 'letra_n.txt', 3),
        Character('c', 'letra_c.txt', 14),
        Character('t', 'letra_t.txt', 6),
        Character('s', 'easter_egg.txt', 11),
    ]
    
    while True:
        print("Ingrese una letra para visualizar en el juego de la vida:")
        print("[p] - Pez")
        print("[de] - Letra Delta")
        print("[o] - Letra O")
        print("[d] - Letra D")
        print("[b] - Letra B")
        print("[a] - Letra A")
        print("[i] - Letra I")
        print("[e] - Letra E")
        print("[n] - Letra N")
        print("[t] - Letra T")
        print("[c] - Letra C")
        print("[s] - Salir")
        
        choice = input().lower()

        if choice == 's':
            for char in characters:
                if char.id == choice:
                    read_initial_states(char, script_directory)
                    print_state(char.matrix)
                    next_state(char.matrix, char.generations)
                    break
            break
        elif choice in ['p', 'o', 'e', 'de', 'b', 'a', 'd', 'i', 'n', 't', 'c']:
            for char in characters:
                if char.id == choice:
                    read_initial_states(char, script_directory)
                    print_state(char.matrix)
                    next_state(char.matrix, char.generations)
                    break
        else:
            print("Opción inválida. Por favor, seleccione una letra válida.")

if __name__ == "__main__":
    main()
