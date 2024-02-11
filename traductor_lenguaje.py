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
    
        curr_state = new_state
        print('Generation: ' + str(ng+1))
        print_state(curr_state)
    return curr_state

def print_state(state):
    width, height = state.shape
    for y in range(width):
        for x in range(height):
            if state[y, x] == 1:
                print('■', end=' ')
            else:
                print('░', end=' ')
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
        Character('o', 'letra_o.txt', 17),
        Character('a', 'letra_a.txt', 1),
        Character('i', 'letra_i.txt', 9),
        Character('e', 'letra_e.txt', 9),
        Character('n', 'letra_n.txt', 2),
        Character('t', 'letra_t.txt', 5),
        Character('s', 'letra_s.txt', 2),
        Character('c', 'letra_c.txt', 13),
        Character('q', 'easter_egg.txt', 10),
    ]
    
    while True:
        print("Ingrese una letra para visualizar en el juego de la vida:")
        print("[o] - Letra O")
        print("[a] - Letra A")
        print("[i] - Letra I")
        print("[e] - Letra E")
        print("[n] - Letra N")
        print("[t] - Letra T")
        print("[s] - Letra S")
        print("[c] - Letra C")
        print("[q] - Quit")
        
        choice = input().lower()

        if choice == 'q':
            for char in characters:
                if char.id == choice:
                    read_initial_states(char, script_directory)
                    print_state(char.matrix)
                    next_state(char.matrix, char.generations)
                    break
            break
        else:
            word = []
            for letter in choice:
                if letter in  ['o', 'e', 'a', 'i', 'n', 't', 'c', 's']:
                    for char in characters:
                        if char.id == letter:
                            read_initial_states(char, script_directory)
                            print_state(char.matrix)
                            char.matrix = next_state(char.matrix, char.generations)
                            word.append(char.matrix)
                else:
                    print(f"Caracter {letter} no encontrado. Por favor, seleccione una letra válida.")
                    break
            if len(word) > 0:
                print('Palabra final: ')
                word = np.hstack(word)
                print_state(word)
if __name__ == "__main__":
    main()
