import os
import numpy as np

class Character:
    def __init__(self, id, filename, generations):
        self.id = id
        self.filename = filename
        self.generations = generations
        self.matrix = []

def next_state(curr_state):
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
    return new_state

def print_state(state):
    for y in range(13):
        for x in range(13):
            print(state[y, x], end=' ')
        print()
    print()

def read_initial_states(character):
    filepath = os.path.join(script_directory, character.filename)
    print(filepath)
    with open(filepath, 'r') as file:
        lines = file.readlines()
        state = []
        for line in lines:
            state.append([int(x) for x in line.strip()])
        character.matrix = np.array(state)

script_directory = os.path.dirname(os.path.abspath(__file__))

characters = [
    Character('p', 'letra_pez.txt', 3),
    Character('o', 'letra_o.txt', 3),
    Character('e', 'letra_delta.txt', 3),
    Character('d', 'letra_d.txt', 3),
    Character('b', 'letra_b.txt', 3)
]
for char in characters:
    read_initial_states(char)
    print_state(char.matrix)

